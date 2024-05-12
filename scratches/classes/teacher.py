from scratches.classes import person


class Teacher(person.Person):
    def __init__(self, name, age, gender, subject, is_headteacher=False):
        super().__init__(name, age, gender)
        self.subject = subject
        self.is_headteacher = is_headteacher

    def introduce(self):
        print(f"Hello, I'm {self.name}, and I'm {self.age} years old. I teach "
              f"{self.subject}.")

    def check_if_headteacher(self):
        if self.is_headteacher:
            print(f"{self.name} is the headteacher.")
        else:
            print(f"{self.name} is not the headteacher.")
        return self.is_headteacher

    def set_headteacher_status(self, status):
        self.is_headteacher = status
        if self.is_headteacher:
            print(f"{self.name} is now the headteacher.")
        else:
            print(f"{self.name} is no longer the headteacher.")
