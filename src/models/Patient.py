class Patient:

    def __init__(self, age: int, gender: int):
        self.age = age
        self.gender = gender

    def update_age(self, age: int):
        self.age = age

    def update_gender(self, gender: int):
        self.gender = gender