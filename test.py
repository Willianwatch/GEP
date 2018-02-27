import random

class Test:

    count = 0

    def __init__(self):
        self.value = self.count
        Test.count += 1

    def __len__(self):
        return 2

    def __str__(self):
        return str(self.__len__())

    @classmethod
    def fromvalues(cls, value):
        cls.value = value
        return cls


def main():
    """
    test = [Test() for _ in range(10)]
    chosen = random.sample(test, 1)
    print(len(chosen))
    index = chosen[0].value
    print(index)
    print(chosen[0] is test[index])
    print(Test.count)
    """
    """
    a = Test.fromvalues(3)
    print(a.value)
    """
    a = Test()
    print(a)

if __name__ == "__main__":
    main()

    