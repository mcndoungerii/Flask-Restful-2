from myapp import app
from myapp.controllers import PuppyNames,AllPuppies
from flask_restful import Api


api = Api(app)


#### Configuring Flask Restful Api and it's resources
api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllPuppies,'/puppies')



if __name__ == '__main__':
    app.run(debug=True)