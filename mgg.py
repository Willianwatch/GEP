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
        self.best_fitness_record = list()

    def __len__(self):
        return self.population_message["population_size"]

    def __iter__(self):
        return iter(self.population)

    def __getitem__(self, position):
        return self.population[position]

    def mgg(self, max_generation):
        """
        Note that here get fitness and search for best can be done at a time.
        """
        Population.get_fitness(self)
        best_pos = Population.search_for_best(self)
        self.best_fitness_record.append(self[best_pos].fitness)
        """
        此处应有打印语句
        """

        for i in range(1, max_generation):
            parents_pos = random.sample(self.__len__(), 2)

            father = self[parents_pos[0]]
            mother = self[parents_pos[1]]

            sub_population = [father, mother]
            reduce(Population.merge, (father.crossover(mother) for _ in range(int(self.population_message["generation_gap"]/2))), sub_population)
            Population.get_fitness(sub_population[2::])
            fitness_list = map(lambda i: i.fitness, self)
            best_and_roulette_pos = Population.best_and_roulette(fitness_list)
            #self.population[parents_pos[0]], self.population[parents_pos[1]] = son, daughter \
            #                                                                 = sub_population[best_and_roulette_pos[0]], sub_population[best_and_roulette_pos[1]]

            """
            现在已经知道了子代种群中最优个体和轮盘赌选择出来的个体的位置。
            接下来要实现的逻辑是：
            1、将子代种群中的最优个体和轮盘赌选择出来的个体替换掉父母个体
            2、将最优个体与原来种群中的最优个体的适应度作比较，如果这个个体的适应度更大，那么将新一代种群中的最优个体标记为该个体，
               否则，最优个体依然为原来种群中的最优个体
            3、打印出最优个体的信息
            """
            #
                                                                               

            

    @staticmethod
    def merge(x: list, y: list):
        x.extend(y)
        return x

    @staticmethod
    def search_for_best(sequence):
        return max(enumerate(sequence), key=lambda compound: compound[1])[0]

    @staticmethod
    def get_fitness(sequence):
        calculate_fitness = methodcaller("parse_individual")
        map(calculate_fitness, sequence)

    @staticmethod
    def best_and_roulette(sequence):
        """
        Note that here this function is not very efficient,choose the best one and the roulette one
        can be done in two traverse, but this one will cost at least three.If you want to improve the
        efficience, remember to use the function random.randomrange
        """
        best_pos = Population.search_for_best(sequence)
        rest_fitness = np.array([i[1].fitness for i in enumerate(sequence) if i[0] != best_pos])
        rest_roulette_pos = Population.roulette(rest_fitness)
        roulette_pos = rest_roulette_pos if rest_roulette_pos < best_pos else rest_roulette_pos + 1
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

        
