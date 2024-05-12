class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You're now {self.age} years old.")

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, " \
               f"gender={self.gender})"
