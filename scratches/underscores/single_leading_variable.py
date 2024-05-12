class Test:
    def __init__(self):
        self.foo = 11
        # intended for internal use, but not enforced by the language
        self._bar = 23


if __name__ == '__main__':
    t = Test()
    print(t.foo)
    print(t._bar)
