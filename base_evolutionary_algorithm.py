import sys

sys.path.insert(0, 'evoman')
sys.path.insert(0, 'other')

from environment import Environment
from demo_controller import player_controller
import numpy as np
import os

DEBUG = True


class EvolutionaryAlgorithm:
    def __init__(self,
                 _experiment_name,
                 _multiple_mode,
                 _population_size,
                 _generations_number,
                 _enemies,
                 _hidden_layer_size,
                 _init_population,
                 _fitness,
                 _selection,
                 _crossover,
                 _mutation,
                 _mutation_selection,
                 _insertion,
                 _genome_adaptive=False):
        self.experiment_name = _experiment_name
        self.multiple_mode = _multiple_mode
        self.population_size = _population_size
        self.generations_number = _generations_number
        self.enemies = _enemies
        self.hidden_layer_size = _hidden_layer_size
        self.fitness = _fitness
        self.selection = _selection
        self.crossover = _crossover
        self.mutation = _mutation
        self.mutation_selection = _mutation_selection
        self.insertion = _insertion
        self.predefined = np.array([])
        self.init_population = _init_population
        self.initialise_environment()
        self.genome_adaptive = _genome_adaptive

    def run(self):
        self.population = self.init_population(
            self.hidden_layer_size, self.env.get_num_sensors(), self.population_size, self.genome_adaptive)

        self.best_fitness = float('-inf')
        avg_generation_fitness = np.array([])
        max_generation_fitness = np.array([])

        generation = 1

        while(generation <= self.generations_number):
            # fitness is an array of fitnesses of individuals.
            # fitness[i] is a fitness of population[i]
            if DEBUG:
                print("Calculating fitness...")

            fitness = self.fitness(self.population, self.env, self.genome_adaptive)

            # Checks if best candidate appeared in the newest generation
            self.update_best(fitness)

            # Add best fitness to arrayt
            max_generation_fitness = np.append(max_generation_fitness, max(fitness))

            # CROSSOVER
            if DEBUG:
                print("Selecting parents...")
            parents = self.selection(fitness, self.population)  # KEEPS ADDING SELECTION
            if DEBUG:
                print("Mating in progress...")
            offspring = self.crossover(parents)

            # MUTATION
            if DEBUG:
                print("Selecting mutants...")
            selected = self.mutation_selection(parents, offspring, self.population)

            if DEBUG:
                print("Mutating...")
            mutants = self.mutation(selected, generation,
                                    self.generations_number, self.population_size)

            # NEXT GENERATION
            if DEBUG:
                print("Creating offspring...")

            newcomers = np.concatenate((offspring, mutants))
            if DEBUG:
                print("Inserting offspring into population...")
            self.population = self.insertion(fitness, self.population, newcomers)

            if DEBUG:
                print(
                    f'Generation {generation} - Best: {self.best_fitness} Mean: {np.mean(fitness)} Std: {np.std(fitness)}')

            # INCREMENT GENERATION
            generation += 1

            # CALCULATE AVERAGE FITNESS FOR GENERATION
            avg_generation_fitness = np.append(avg_generation_fitness, np.average(fitness))

        if(self.genome_adaptive):
            return self.best[:-1], self.best_fitness, avg_generation_fitness, max_generation_fitness

        return self.best, self.best_fitness, avg_generation_fitness, max_generation_fitness

    def update_best(self, fitness):
        for i in range(self.population.shape[0]):
            if fitness[i] > self.best_fitness:
                self.best, self.best_fitness = self.population[i], fitness[i]

    def initialise_environment(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        if not os.path.exists(self.experiment_name):
            os.makedirs(self.experiment_name)

        self.env = Environment(experiment_name=self.experiment_name,
                               enemies=self.enemies,
                               multiplemode=self.multiple_mode,
                               playermode="ai",
                               player_controller=player_controller(self.hidden_layer_size),
                               enemymode="static",
                               level=2,
                               speed="fastest")
