from scratches.classes import person


class Student(person.Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old. My student "
              f"ID is {self.student_id}, and I am studying {self.course}.")

    def change_course(self, new_course):
        self.course = new_course
        print(f"{self.name} is now studying {self.course}.")
