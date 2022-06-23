class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def save(self, to_file):
        to_file.write(f"{self.name},{self.phone},{self.email}\n")