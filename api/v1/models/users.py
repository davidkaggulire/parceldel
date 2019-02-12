"""users.py"""


class Users:
    """class to describe users"""
    user_list = []

    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        """returns user_dict"""
        user_dict = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

        return user_dict
