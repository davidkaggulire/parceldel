"""users.py"""


class Users:
    user_list = []

    def __init__(self, user_id, name, username, email, password):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        user_dict = {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

        return user_dict
