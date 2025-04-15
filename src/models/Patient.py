class Patient:
    #Funciones para gestionar Patient (age y gender)
    def __init__(self, age: int, gender: int):
        self.age = age
        self.gender = gender

    def update_age(self, age: int):
        self.age = age

    def update_gender(self, gender: int):
        self.gender = gender

    def __str__(self):
        return f"Patient: (age={self.age}, gender={self.gender})"
    
    def __repr__(self):
        return self.__str__()