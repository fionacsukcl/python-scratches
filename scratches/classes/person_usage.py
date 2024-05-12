from scratches.classes import person

if __name__ == '__main__':
    p = person.Person('Alice', 25, 'Female')
    p.introduce()
    print(p.age)
    p.celebrate_birthday()
    print(p.age)
    print(str(p))
    print(repr(p))
