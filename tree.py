from node import Add, Sub, Mul, Negate, Number

char_operator = {'0': Number,
                 '1': Negate,
                 '2': Add,
                 '3': Sub,
                 '4': Mul}


class Tree:
    def __init__(self, sequence):
        self.sequence = sequence
        self.root = None
        
    def __iter__(self):
        return iter(self.sequence)
        
    def __enter__(self):
        self.root = char_operator[self.sequence[0]]()
        queue = [self.root]

        generator = iter(self.sequence)
        next(generator)

        for i in queue:
            for _ in range(len(i)):
                current_node = char_operator[next(generator)]()
                queue.append(current_node)
                i.add_child(current_node)
        
        return self.root

    def __exit__(self, exc_ty, exc_val, tb):
        self.root = None
        self.string = None
        
    def __str__(self):
        pass
    
    def depth_first(self):
        yield self