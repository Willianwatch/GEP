from operator import methodcaller
import random
from functools import reduce
import numpy as np
import numbers

from .individual import Individual


class Population:

    def __init__(self, li=None, size=50, restriction=50, crossover=0.9, mutate=0.1, gap=40):
        if li is None:
            self.population_message = {
                "population_size": size,
                "individual_restriction": restriction,
                "crossover_ratio": crossover,
                "mutate_ratio": mutate,
                "generation_gap": gap
            }
            self.population = [Individual(length_of_head=restriction) for _ in range(size)]
        else:
            self.population_message = {}
            self.population = li
        
        self.best_fitness_record = list()

    def __len__(self):
        return len(self.population)

    def __iter__(self):
        return iter(self.population)

    def __getitem__(self, index):
        cls = type(self)

        if isinstance(index, list) or isinstance(index, tuple):
            return tuple(self.population[position] for position in index)
        elif isinstance(index, numbers.Integral):
            return self.population[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __setitem__(self, index, value):
        cls = type(self)
        
        if isinstance(index, tuple) or isinstance(index, list):
            if len(index) != len(value):
                raise RuntimeError("Error argument!")
            else:
                for position, val in zip(index, value):
                    self.population[position] = val
        elif isinstance(index, numbers.Integral):
            self.population[index] = value
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def get_fitness(self):
        calculate_fitness = methodcaller("parse_individual")
        map(calculate_fitness, self)

    def mgg(self, max_generation):
        """
        Note that here get fitness and search for best can be done at a time.
        """
        self.get_fitness()
        first_gen_fitness = [i.fitness for i in self]
        best_pos = Population.search_for_best(first_gen_fitness)
        self.best_fitness_record.append((best_pos, self[best_pos].fitness))

        print("{generation:0>4}:{fitness:.8f}".format(generation=0, fitness=self[best_pos].fitness))

        for i in range(1, max_generation):
            parents_pos = random.sample(range(len(self)), 2)

            father, mother = self[parents_pos]

            family = [father, mother]
            reduce(Population.merge, (father.crossover(mother, self.population_message["crossover_ratio"]) for _ in range(int(self.population_message["generation_gap"]/2))), family)

            sub_population = Population(li=family)
            sub_population.get_fitness()
            fitness_list = map(lambda i: i.fitness, self)
            best_and_roulette_pos = Population.best_and_roulette(fitness_list)
            
            """
            现在已经知道了子代种群中最优个体和轮盘赌选择出来的个体的位置。
            接下来要实现的逻辑是：
            1、将子代种群中的最优个体和轮盘赌选择出来的个体替换掉父母个体
            2、将最优个体与原来种群中的最优个体的适应度作比较，如果这个个体的适应度更大，那么将新一代种群中的最优个体标记为该个体，
               否则，最优个体依然为原来种群中的最优个体
            3、打印出最优个体的信息
            """
            # 第1步
            self[parents_pos] = sub_population[best_and_roulette_pos]

            # 第2步
            if self[parents_pos][0].fitness > self.best_fitness_record[-1][1]:
                self.best_fitness_record.append((parents_pos[0], self[parents_pos][0].fitness))
            else:
                self.best_fitness_record.append(self.best_fitness_record[-1])

            print("{generation:0>4}:{fitness:.8f}".format(generation=i, fitness=self.best_fitness_record[-1][1]))

    @staticmethod
    def merge(x, y):
        x.extend(y)
        return x

    @staticmethod
    def search_for_best(sequence):
        return max(enumerate(sequence), key=lambda compound: compound[1])[0]


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

        
