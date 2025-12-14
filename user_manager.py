from user import User

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, name, last_name, email, password):
        for user in self.users:
            if user.email == email:
                return False
        new_user = User(name, last_name, email, password)
        self.users.append(new_user)
        return True

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None
