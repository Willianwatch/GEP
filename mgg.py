from individual import Individual
from operator import itemgetter, methodcaller
import random
from functools import reduce
import numpy as np


class Population:

    def __init__(self, size=50, restriction=50, crossover=0.9, mutate=0.1, gap=40):
        self.population_message = {
            "population_size": size,
            "individual_restriction": restriction,
            "crossover_ratio": crossover,
            "mutate_ratio": mutate,
            "generation_gap": gap
        }
        self.population = [Individual(restriction) for _ in range(size)]

    def __len__(self):
        return self.population_message["population_size"]

    def __iter__(self):
        return iter(self.population)

    def __getitem__(self, position):
        return self.population[position]

    def mgg(self, max_generation):
        for i in range(max_generation):
            parents_pos = random.sample(self.__len__(), 2)

            father = self[parents_pos[0]]
            mother = self[parents_pos[1]]

            sub_population = [father, mother]
            reduce(Population.merge, (father.crossover(mother) for _ in range(int(self.population_message["generation_gap"]/2))), sub_population)
            Population.get_fitness(sub_population[2::])
            best_and_roulette_pos = Population.best_and_roulette(sub_population)

    @staticmethod
    def merge(x: list, y: list):
        x.extend(y)
        return x

    @staticmethod
    def search_for_best(sequence):
        return max(enumerate(sequence), key=lambda compound: compound[1].fitness)[0]

    @staticmethod
    def get_fitness(sequence):
        calculate_fitness = methodcaller("parse_individual")
        map(calculate_fitness, sequence)

    @staticmethod
    def best_and_roulette(sequence):
        best_pos = Population.search_for_best(sequence)
        rest_fitness = np.array([i[1].fitness for i in enumerate(sequence) if i[0] != best_pos])
        roulette_pos = Population.roulette(rest_fitness)
        return best_pos, roulette_pos

    @staticmethod
    def roulette(sequence: np.array):
        sequence /= sum(sequence)
        current_sum = 0
        part_sum = []

        for i in sequence:
            current_sum += i
            part_sum.append(current_sum)

        rand = random.random()
        roulette_pos = 0
        for i in enumerate(part_sum):
            if rand <= i[1]:
                roulette_pos = i[0]
                break

        return roulette_pos
