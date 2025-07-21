from flask import Flask,jsonify,request
from models import db, User,ContactMessage
from flask_login import login_user,logout_user,LoginManager
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact message.db'
app.config['SECRET_KEY'] = ' '
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/register',methods=['POST'])
def register():
    try:
        data = request.get_json()
        print(data)
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'message':'Please fill in all forms'}),404

        hashed_pw = generate_password_hash(data['password'])
        user = User(username=username,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message':'You have successfully registered!! Now login.'}),201
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/login',methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'message':'This details are wrong please try again'}),404

        user = User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message':'You have successfully logged in'}),200
        return jsonify({'message':'Your details are wrong. Please try again'}),404
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/logout',methods=['GET'])
def logout():
    try:
        logout_user()
        return jsonify({'message':'You have successfully deleted'}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/contact_message',methods =['POST'])
def contact_message():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        if not name or not email or not subject or not message:
            return jsonify({'message':'Please fill in all the details provided'}),400

        user = ContactMessage(name=name,email=email,subject=subject,message=message)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message':'Your message has been added'}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/get_contact_message',methods=['GET'])
def get_contact_message():
    try:
        contacts = ContactMessage.query.all()
        contact_list = [
            {
                'name': contact.name,
                'email':contact.email,
                'subject':contact.subject,
                'message':contact.message
            }
            for contact in contacts
        ]
        return jsonify({'data':contact_list}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/single_contact_message/<int:contact_message_id>',methods = ['GET'])
def single_contact_message(contact_message_id):
    try:
        contact = ContactMessage.query.get(contact_message_id)
        if not contact:
            return jsonify({'message':'Contact does not exist'}),400

        contact_data = {
            'name':contact.name,
            'email':contact.email,
            'subject':contact.subject,
            'message':contact.message
        }
        return jsonify({'message':'This is the contact data','data':contact_data}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500


@app.route('/edit_contact_message/<int:contact_message_id>',methods=['PUT'])
def edit_contact_message(contact_message_id):
    try:
        contact = ContactMessage.query.get(contact_message_id)
        if not contact:
            return jsonify({'message':'This contact cant be found'})

        data = request.get_json()
        contact.name = data .get('name')
        contact.email = data.get('email')
        contact.subject = data.get('subject')
        contact.message = data.get('message')
        db.session.commit()
        return jsonify({'message':'You have successfully edited your contact message'}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500

@app.route('/delete_contact_message/<int:contact_message_id>',methods=['DELETE'])
def delete_contact_message(contact_message_id):
    try:
        contact = ContactMessage.query.get(contact_message_id)
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message':'Your contact message has been deleted'}),200
    except Exception as e:
        return jsonify({'message':'Internal server error','error':str(e)}),500



if __name__=='__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)