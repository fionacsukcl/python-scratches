from scratches.classes import teacher

if __name__ == '__main__':
    t = teacher.Teacher('Alice', 35, 'F', 'Mathematics', True)
    t.introduce()
    t.check_if_headteacher()
    t.celebrate_birthday()
    t.set_headteacher_status(False)
    t.check_if_headteacher()