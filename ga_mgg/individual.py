import random
import numpy as np
import math

from .tree import char_operator, Tree
from .node_visitor import Evaluator
from .data import training_data_set


class Individual:

    training_data_set_output = np.array([i[1] for i in training_data_set])

    def __init__(self, sequence=None, length_of_head=50, max_num_of_input=2):
        if sequence is None:
            self.individual_restriction = length_of_head
            length_of_tail = (max_num_of_input - 1)*length_of_head + 1
            self.chromosome = np.concatenate((np.random.randint(0, len(char_operator), size=length_of_head),
                                            np.zeros(length_of_tail)))
        else:
            self.individual_restriction = len(sequence)
            length_of_tail = (max_num_of_input - 1)*length_of_head + 1
            self.chromosome = np.concatenate((np.array(sequence), np.zeros(length_of_tail)))
        
        self.fitness = 0
        
    def __len__(self):
        return len(self.chromosome)

    def __iter__(self):
        return iter(self.chromosome)

    def __getitem__(self, position):
        return self.chromosome[position]

    def __setitem__(self, index, value):
        self.chromosome[index] = value

    def parse_individual(self):
        if self.fitness != 0:
            pass
        else:
            e = Evaluator()
            with Tree(self) as individual:
                self.fitness = np.std(self.training_data_set_output - e.visit(individual))

    def crossover(self, another, crossover_ratio):
        if random.random() < crossover_ratio:
            crossover_point_one = random.randint(0, self.individual_restriction - 1)
            crossover_gene_length = random.randint(1, self.individual_restriction - crossover_point_one)
            crossover_point_two = random.randint(0, self.individual_restriction - crossover_gene_length)

            FIRST_PART = slice(crossover_point_one, crossover_point_one + crossover_gene_length)
            SECOND_PART = slice(crossover_point_two, crossover_point_two + crossover_gene_length)

            FATHER = self.chromosome.copy()
            MOTHER = another.chromosome.copy()

            temp_array = FATHER[FIRST_PART].copy()
            FATHER[FIRST_PART] = MOTHER[SECOND_PART]
            MOTHER[SECOND_PART] = temp_array

            return [Individual(sequence=i) for i in (FATHER, MOTHER)]
        else:
            return []

    def mutate(self, mutate_ratio):
        if random.random() < mutate_ratio:
            mutate_point_one = random.randint(0, self.individual_restriction - 1)
            mutate_gene_length = random.randint(1, self.individual_restriction - mutate_point_one)

            MUTATE_PART = slice(mutate_point_one, mutate_point_one + mutate_gene_length)

            exchange_part = np.random.randint(0, len(char_operator), size=mutate_gene_length)
            self[MUTATE_PART] = exchange_part

    def recombination(self, another, crossover_ratio, mutate_ratio):
        offsprings = self.crossover(another, crossover_ratio)
        map(lambda i: i.mutate(mutate_ratio), offsprings)

        return offsprings

        