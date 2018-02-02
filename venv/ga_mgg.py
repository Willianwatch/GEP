import random
import numpy as np
from tree import Tree
from node_visitor import Evaluator
from math import sin


training_data_set = [(i, sin(i)) for i in range(50)]

class Population:
    def __init__(self, size=50, restriction=50, crossover=0.9, mutate=0.1, gap=40):
        self.population_size = size
        self.individual_restriction = restriction
        self.crossover_ratio = crossover
        self.mutate_ratio = mutate
        self.generation_gap = gap
        self._population = None
        self.fitness = np.zeros((1,self.population_size))
        self.training_data_set_input = np.array([i[0] for i in training_data_set])
        self.training_data_set_output = np.array([i[1] for i in training_data_set])

    def __len__(self):
        return len(self._population)

    def __iter__(self):
        return iter(self._population)

    def generate_initial_population(self):
        length_of_head = self.individual_restriction
        length_of_tail = length_of_head + 1
        length_of_chromosome = length_of_head + length_of_tail
        self._population = np.column_stack((np.random.randint(0,6,(50,50)),np.zeros((50,51))))

    def parse_individual(self, position):
        '''
        First, assert that position must be an unsigned integer.
        After you make sure the position argument is an integer, 
        get the result of expression tree and then the fitenss.
        '''
        assert 0 <= position < self.population_size
        assert isinstance(position, int)
        e = Evaluator()
        with Tree(self._population(position)) as individual:
            self.fitness[position] = e.visit(individual)