from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from secure_check import authenticate,identity

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"

### Registering our flask app to Flask Api
api = Api(app) 

### initiate jwt variable, assign to JWT class and inherit from app, authenticate, and identity

jwt = JWT(app,authenticate,identity)

puppies = []

class Puppies(Resource):

    def get(self,name):
        
        for pup in puppies:
            if pup['name'] == name:
                return pup

        return {'name': None}, 404


    def post(self,name):
        pup = {'name': name}

        puppies.append(pup)

        return pup, 201
        

    def delete(self,name):

        for index,pup in enumerate(puppies):

            if pup['name'] == name:
                puppies.pop(index)
                return {'note': 'delete successful'}

        return {'name': None}, 404


class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {"puppies": puppies}

api.add_resource(Puppies,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)