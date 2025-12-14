class User:
    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.email}"
