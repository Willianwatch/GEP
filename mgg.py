from individual import Individual
from operator import itemgetter


class Population:

    def __init__(self, size=50, restriction=50, crossover=0.9, mutate=0.1, gap=40):
        self.population_message = {
            "population_size":size,
            "individual_restriction":restriction,
            "crossover_ratio":crossover,
            "mutate_ratio":mutate,
            "generation_gap":gap
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
            pass

    def search_for_best(self):
        return max(enumerate(self), key=lambda individual:individual.fitness)
