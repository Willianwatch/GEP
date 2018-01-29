from node import Add, Sub, Mul, Div, Negate, Number

char_operator = {'+': Add,
                 '-': Sub,
                 '*': Mul,
                 '/': Div,
                 '1': Number}


class Tree:
    def __init__(self, string):
        self.root = char_operator[string[0]]()
        queue = [self.root]

        generator = iter(string)
        next(generator)

        for i in queue:
            for j in range(len(i)):
                current_node = char_operator[next(generator)]()
                queue.append(current_node)
                i.add_child(current_node)