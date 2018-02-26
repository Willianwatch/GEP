import numpy as np

class Test:
    def __init__(self, length):
        self.elements = np.zeros(length)

    def __getitem__(self, position):
        return self.elements[position]

    def change(self, position):
        print(self[position::])


def main():
    test = Test(5)
    test.change(3)

if __name__ == "__main__":
    main()

    