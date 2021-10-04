import sys

from numpy.core.arrayprint import printoptions
sys.path.insert(0, 'evoman')
sys.path.insert(0, 'other')

from environment import Environment
from demo_controller import player_controller
import numpy as np
import os
from timer import Timer
from tabulate import tabulate

DEBUG = True
USE_SAME = False


class EvolutionaryAlgorithm:
    def __init__(self,
                 _experiment_name,
                 _population_size,
                 _generations_number,
                 _enemy_id,
                 _hidden_layer_size,
                 _fitness,
                 _selection,
                 _crossover,
                 _mutation,
                 _mutation_selection,
                 _insertion):
        self.experiment_name = _experiment_name
        self.population_size = _population_size
        self.generations_number = _generations_number
        self.enemy_id = _enemy_id
        self.hidden_layer_size = _hidden_layer_size
        self.fitness = _fitness
        self.selection = _selection
        self.crossover = _crossover
        self.mutation = _mutation
        self.mutation_selection = _mutation_selection
        self.insertion = _insertion
        self.predefined = np.array([])
        self.initialise_environment()

    def run(self):
        t = Timer()
        self.initialise_population()
        self.best_fitness = float('-inf')
        avg_generation_fitness = np.array([])
        max_generation_fitness = np.array([])

        generation = 1

        while(generation <= self.generations_number):
            # fitness is an array of fitnesses of individuals.
            # fitness[i] is a fitness of population[i]
            if DEBUG: print("Calculating fitness...")
            fitness = self.fitness(self.population, self.env)
            # Checks if best candidate appeared in the newest generation
            self.update_best(fitness)

            # Add best fitness to arrayt
            max_generation_fitness = np.append(max_generation_fitness, max(fitness))

            # CROSSOVER
            if DEBUG: print("Selecting parents...")
            t.start()
            parents = self.selection(fitness, self.population)  # KEEPS ADDING SELECTION
            parent_selection_time = t.stop()
            if DEBUG: print("Mating in progress...")
            t.start()
            offspring = self.crossover(parents)
            mating_time = t.stop()

            # MUTATION
            if DEBUG: print("Selecting mutants...")
            t.start()
            selected = self.mutation_selection(parents, offspring, self.population)
            mutation_selection_time = t.stop()
            if DEBUG: print("Mutating...")
            t.start()
            mutants = self.mutation(selected)
            mutation_time = t.stop()

            # NEXT GENERATION
            if DEBUG: print("Creating offspring...")
            t.start()
            offspring = np.concatenate((offspring, mutants))
            creating_offspring_time = t.stop()
            if DEBUG: print("Inserting offspring into population...")
            t.start()
            self.population = self.insertion(fitness, self.population, offspring)
            insert_offspring_time = t.stop()

            if DEBUG:
                print(
                    f'Generation {generation} - Best: {self.best_fitness} Mean: {np.mean(fitness)} Std: {np.std(fitness)}')
                
                print(tabulate([["parent_selection", parent_selection_time], ["mating", mating_time], ["mutation_selection", mutation_selection_time], 
                ["mutation", mutation_time], ["creating_offspring", creating_offspring_time], ["insert_offspring", insert_offspring_time]], headers=['Operation', 'Time'], tablefmt='github'))

            # INCREMENT GENERATION
            generation += 1

            # CALCULATE AVERAGE FITNESS FOR GENERATION
            t.start()
            avg_generation_fitness = np.append(avg_generation_fitness, np.average(fitness))
            calculate_avg_fitness = t.stop()
            print(f'Time to calculate average fitness: {calculate_avg_fitness}')

        return self.best, self.best_fitness, avg_generation_fitness, max_generation_fitness

    def update_best(self, fitness):
        for i in range(self.population.shape[0]):
            if fitness[i] > self.best_fitness:
                self.best, self.best_fitness = self.population[i], fitness[i]

    def initialise_population(self):
        if(USE_SAME and self.predefined.shape[0]):
            self.population = np.array(self.predefined)
            return
        genome_length = self.hidden_layer_size * \
            (self.env.get_num_sensors() + 1) + 5 * (self.hidden_layer_size + 1)
        # What gets created here? Array of size... ->  self.population_size * genome_length
        self.population = np.random.uniform(-1, 1, self.population_size * genome_length,)
        self.population = self.population.reshape(self.population_size, genome_length)

        if(USE_SAME):
            self.predefined = np.array(self.population)

    def initialise_environment(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        if not os.path.exists(self.experiment_name):
            os.makedirs(self.experiment_name)

        self.env = Environment(experiment_name=self.experiment_name,
                               enemies=[self.enemy_id],
                               playermode="ai",
                               player_controller=player_controller(self.hidden_layer_size),
                               enemymode="static",
                               level=2,
                               speed="fastest")
