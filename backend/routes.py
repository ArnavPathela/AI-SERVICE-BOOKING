from flask_restful import Api, Resource
from flask import request
from models import User, db,Admin, Professional
api = Api()

class User_Regesteration(Resource):
    def post(self):
        data = request.get_json()

        if not data or "name" not in data or not data['name']:
            return {"message":"Name is required"},401
        if not data or "password" not in data or not data['password']:
            return {"message":"Password is required"},401
        if not data or "email" not in data or not data['email']:
            return{"message":"Email ₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹is required"},401
        if not data or "address" not in data or not data['address']:
            return{"message":"Address is required"},401
        
        existing_user_check = User.query.filter_by(email = data['email']).first()
        if existing_user_check:
            return{"message":"User already exists please login"},409
        new_user = User(name = data['name'], email = data['email'], password = data['password'], address = data['address'])
        db.session.add(new_user)
        db.session.commit()
        return{"message":"User has been Added successfully"},200
api.add_resource(User_Regesteration,'/User-Registeration')

class User_Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or "email" not in data or not data['email']:
            return{"message":"Email is required to login"},401
        if not data or "password" not in data or not data['password']:
            return{"message":"Password is required to login"},401
        User_Login_Check = User(email = data['email'], password = data['password']).first()
        if User_Login_Check:
            return{"message":"User logged in successfully"},200
        else:
            return{"message":"Invalid credentials"},409

api.add_resource(User_Login, '/User-Login')


class Admin_Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or "email" not in data or not data['email']:
            return{"message":"Email is required to login"},401
        if not data or "password" not in data or not data['password']:
            return{"message":"Password is required to login"},401
        Admin_Login_Check = Admin(email = data['email'], password = data['password']).first()
        if Admin_Login_Check:
            return{"message":"Admin Logged in Successfully"},200
        else:
            return{"message":"Invalid Credentials"},409
api.add_resource(Admin_Login, '/Admin_Login')

class Professional_Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or "Name" not in data or not data['Name']:
            return{"message":"Name is required"},401
        if not data or "Email" not in data or not data['Email']:
            return{"message:":"Email is required"},401
        if not data or 'Address' not in data or not data['Address']:
            return{"message":"Address is required"},401
        if not data or 'Password' not in data or not data['Password']:
            return{"message":"Password is required"},401
        Existing_Professional_Check = Professional(email = data['email']).first()
        if Existing_Professional_Check:
            return{"message":"Professional Already Exists"},409
        else:
            New_Professional = Professional(Name = data['Name'], Email = data['Email'], Password = data['Password'],Address = data['Address'])
            db.session.add(New_Professional)
            db.session.commit()
            return{"message":"Successfully Registered"},200

api.add_resource(Professional_Register,'/Professional_Registeration')


class Professional_Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or "Email" not in data or not data['Email']:
            return{"message":"Email is required to login"},401
        if not data or 'Password' not in data or not data['password']:
            return{"message":"Password is required"},401
        Professional_Check = Professional(email = data['Email'], Password =data['Password']).first()
        if Professional_Check:
            return{"message":"Logged in successfully"},200
        else:
            return{"message":"Invalid Credentials"},409
api.add_resource(Professional_Login,'/Professional_Login')

        