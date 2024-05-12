from scratches.classes import person

if __name__ == '__main__':
    p = person.Person('Alice', 25, 'F')
    p.introduce()
    print(p.age)
    p.celebrate_birthday()
    print(p.age)
