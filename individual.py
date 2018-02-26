import random
import numpy as np
from tree import char_operator, Tree
from node_visitor import Evaluator
from data import training_data_set


class Individual:

    training_data_set_output = np.array([i[1] for i in training_data_set])

    def __init__(self, length_of_head=50, max_num_of_input=2):
        self.individual_restriction = length_of_head
        length_of_tail = (max_num_of_input - 1)*length_of_head + 1
        self.chromosome = np.concatenate((np.random.randint(0, len(char_operator), size=length_of_head),
                                          np.zeros(length_of_tail)))
        self.fitness = 0
        
    def __len__(self):
        return len(self.chromosome)

    def __iter__(self):
        return iter(self.chromosome)

    def __getitem__(self, position):
        return self.chromosome[position]        

    def parse_individual(self):
        e = Evaluator()
        with Tree(self) as individual:
            self.fitness = np.exp(-np.var(self.training_data_set_output - e.visit(individual)))
        return self.fitness

    def crossover(self, another:Individual):
        crossover_point_one = random.randint(0, self.individual_restriction - 1)
        crossover_gene_length = random.randint(1, self.individual_restriction - crossover_point_one)
        crossover_point_two = random.randint(0, self.individual_restriction - crossover_gene_length)
        FIRST_PART = slice(crossover_point_one, crossover_point_one + crossover_gene_length)
        SECOND_PART = slice(crossover_point_two, crossover_point_two + crossover_gene_length)
        temp_array = self[FIRST_PART].copy()
        self.chromosome[FIRST_PART] = another[SECOND_PART]
        another[SECOND_PART] = temp_array

    def mutate(self):
        mutate_point_one = random.randint(0, self.individual_restriction - 1)
        mutate_gene_length = random.randint(1, self.individual_restriction - mutate_point_one)
        MUTATE_PART = slice(mutate_point_one, mutate_point_one + mutate_gene_length)
        exchange_part = np.random.randint(0, len(char_operator), size=mutate_gene_length)
        self.chromosome[MUTATE_PART] = exchange_part
        