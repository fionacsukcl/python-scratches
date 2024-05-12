class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        # Name mangling: protects variable from being overridden in subclasses
        self.__baz = 42


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"


class ManglingTest:
    def __init__(self):
        self.__mangled = "hello"
        self.non_mangled = "world"

    def get_mangled(self):
        return self.__mangled


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


if __name__ == "__main__":
    t = Test()
    print(dir(t))

    # t2 = ExtendedTest()
    # print(f"t2.foo: {t2.foo}")
    # print(f"t2._bar: {t2._bar}")
    # print(f"t2.__baz: {t2.__baz}")  # Becomes _ExtendedTest__baz
    # print(dir(t2))

    # print(ManglingTest().get_mangled())
    # print(ManglingTest().non_mangled)
    # print(ManglingTest().__mangled)
    # print(dir(ManglingTest()))

    # print(MangledMethod().call_it())
    # print(MangledMethod().__method())
