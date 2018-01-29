from abc import ABCMeta, abstractmethod


class Operator(metaclass=ABCMeta):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def add_child(self, node):
        pass


class Number(Operator):
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def add_child(self, node):
        self.value = node


class UnaryOperator(Operator):
    def __init__(self):
        self.operand = None

    def __iter__(self):
        return iter([self.operand])

    def __len__(self):
        return 1

    def add_child(self, node):
        self.operand = node


class BinaryOperator(Operator):
    def __init__(self):
        self.left = None
        self.right = None

    def __iter__(self):
        return iter([self.left, self.right])

    def __len__(self):
        return 2

    def add_child(self, node):
        if self.left is None:
            self.left = node
        else:
            self.right = node


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass
