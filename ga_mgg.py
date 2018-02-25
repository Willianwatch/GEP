import random
import numpy as np
from tree import Tree, char_operator
from node_visitor import Evaluator
from data import training_data_set


class Population:
    def __init__(self, size=50, restriction=50, crossover=0.9, mutate=0.1, gap=40):
        self.population_size = size
        self.individual_restriction = restriction
        self.chromosome_size = None
        self.crossover_ratio = crossover
        self.mutate_ratio = mutate
        self.generation_gap = gap
        self._population = None
        self.fitness = np.zeros((1,self.population_size))
        self.training_data_set_output = np.array([i[1] for i in training_data_set])
        self.best_individual = None

    def __len__(self):
        return len(self._population)

    def __iter__(self):
        return iter(self._population)

    def generate_initial_population(self):
        length_of_head = self.individual_restriction
        length_of_tail = length_of_head + 1
        self.chromosome_size = length_of_head + length_of_tail
        self._population = np.column_stack((np.random.randint(0, len(char_operator.items),(self.population_size,length_of_head)),
                                            np.zeros((self.population_size,length_of_tail))))

    def parse_individual(self, position):
        '''
        First, assert that position must be an unsigned integer.
        After you make sure the position argument is an integer, 
        get the result of expression tree and then the fitenss.
        '''
        assert 0 <= position < self.population_size and isinstance(position, int)
        e = Evaluator()
        with Tree(self._population(position)) as individual:
            self.fitness[position] = np.exp(-np.var(self.training_data_set_output - e.visit(individual)))

    def crossover(self, position_one, position_two):
        '''
        Use two-point crossover strategy.
        '''
        assert all(map(lambda x: 0<= x <= self.population_size and isinstance(x, int), [position_one, position_two]))
        crossover_point_one = random.randint(0, self.individual_restriction - 1)
        crossover_gene_length = random.randint(1, self.individual_restriction - crossover_point_one)
        crossover_point_two = random.randint(0, self.individual_restriction - crossover_gene_length)
        temp_array = self._population[position_one][crossover_point_one:crossover_point_one+crossover_gene_length].copy()
        self._population[position_one][crossover_point_one:crossover_point_one+crossover_gene_length] = \
        self._population[position_two][crossover_point_two:crossover_point_two+crossover_gene_length]
        self._population[position_two][crossover_point_two:crossover_point_two+crossover_gene_length] = temp_array
        
    def mutate(self, pos):
        pass
    
    def search_for_best(self, max_generation=10000):
        pass
        