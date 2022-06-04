from flask_jwt import jwt_required
from flask_restful import Api,Resource
from myapp import db
from myapp.models import Puppy,User

class PuppyNames(Resource):

    def get(self,name):
        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.__repr__()
        else:
            return None,404

    def post(self,name):

        if len(name) == 1:
            return {"message": f"Can't be a real name {name}"}, 400
        pup = Puppy(name)

        db.session.add(pup)
        db.session.commit()

        return pup.repr(), 201


    def update(self,id,name):
        pup = Puppy.query.filter_by(id=id).first()

        pup.name = name
        db.session.commit()

        return f"Puppy name is {name}",201

    def delete(self,name):
        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            db.session.delete(pup)
            db.session.commit()
            return f"Puppy {name} had been deleted successfully"
        else:
            return None, 404

class AllPuppies(Resource):
    @jwt_required()
    def get(self):
        puppies = Puppy.query.all()

        if puppies:
            return [pup.json() for pup in puppies]
        else:
            return None, 401

class Auth(Resource):

    def post(self,username,password):
        self.username = username
        self.password = password
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return user.__str__(), 201

    def getAll(self):
        users = User.query.all()
        return [u.json for u in users]




