from myapp.user import User

# from myapp.controllers import Auth

### Create a List of Dictionary
# users = Auth.getAll()
# users = [user.json() for user in users_array]
users = [User(1,"Allen",123),User(2,"Bob",123)]

### initiate username table to use in authenticate function when checking if the user
### is present in the Db or users list

username_table = {u.username: u for u in users}

### Initiate userid table to use in identity function to get the user id if exist in our
## db or user list

userid_table = {u.id: u for u in users}

def authenticate(username,password):
    user = username_table.get(username,None)

    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']

    return userid_table.get(user_id,None)