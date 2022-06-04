from flask_jwt import jwt_required
from myapp import db,rest,api
from models import Puppy

class PuppyNames(rest):

    def get(self,name):
        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.json()
        else:
            return None,404

    def post(self,name):
        pup = Puppy(name)

        db.session.add(pup)
        db.session.commit()

        return pup, 201


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

class AllPuppies(rest):
    @jwt_required()
    def get(self):
        puppies = Puppy.query.all()

        if puppies:
            return [pup.json() for pup in puppies]
        else:
            return None, 401


#### Configuring Flask Restful Api and it's resources
api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllPuppies,'/puppies')

