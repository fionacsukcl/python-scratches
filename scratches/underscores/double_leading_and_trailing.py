class PrefixPostfixTest:
    def __init__(self):
        # Generally avoid using double underscores at the start and end to
        # avoid conflicts with Python special methods
        self.__bam__ = 42  # No name mangling here


if __name__ == "__main__":
    print(PrefixPostfixTest().__bam__)
