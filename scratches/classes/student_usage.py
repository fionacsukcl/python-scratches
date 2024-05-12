from scratches.classes import student

if __name__ == '__main__':
    s = student.Student('Bob', 20, 'M', '12345', 'Computer Science')
    s.introduce()
    s.change_course('Economics')
    s.celebrate_birthday()
    s.introduce()
