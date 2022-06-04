from myapp import app
from myapp.controllers import PuppyNames,AllPuppies,Auth
from flask_restful import Api


api = Api(app)



#### Configuring Flask Restful Api and it's resources
api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllPuppies,'/puppies')
api.add_resource(Auth,'/signup')



if __name__ == '__main__':
    app.run(debug=True)