from myapp import db

class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name is {self.name}"

    def json(self):
        return {"name":self.name}


db.create_all()