import numpy as np
from tree import char_operator


class Individual:
    def __init__(self, length_of_head=50, max_num_of_input=2):
        length_of_tail = (max_num_of_input - 1)*length_of_head + 1
        self.chromosome = np.concatenate(np.random.randint(0, len(char_operator), size=length_of_head),\
                                         np.zeros((1, length_of_tail)))
        
    def __len__(self):
        return len(self.chromosome)

    def __iter__(self):
        return iter(self.chromosome)

    def 