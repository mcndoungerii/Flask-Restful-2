from myapp import db

class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))

    def __init__(self,name):
        self.name = name

    def repr(self):
        return f"Puppy name is {self.name}"

    def json(self):
        return {"name":self.name}


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(80),nullable=False)

    def __init__(self, username,password):
       
        self.username = username
        self.password = password

    def __str__(self):
        return f"User Id is {self.id}"

    def json(self):
        return {"id": self.id,"username":self.username,"password":self.password}

db.create_all()