import numpy as np
import os


class InitPopulation:

    population = np.array([])

    @staticmethod
    def basic(hidden_layer_size, input_size, population_size, enemies):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1)

        population = np.random.uniform(-1, 1, population_size * genome_length)
        return population.reshape(population_size, genome_length)

    @staticmethod
    def same_population(hidden_layer_size, input_size, population_size, enemies):
        if(InitPopulation.population.shape[0] == 0):
            InitPopulation.population = InitPopulation.basic(
                hidden_layer_size, input_size, population_size)

        return InitPopulation.population

    @staticmethod
    def genome_adaptive(hidden_layer_size, input_size, population_size, enemies):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1) + 1

        population = np.random.uniform(-1, 1, population_size * genome_length)
        return population.reshape(population_size, genome_length)

    @staticmethod
    def with_best(hidden_layer_size, input_size, population_size, enemies):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1)
        population = np.array([])
        no_solutions = 0

        for enemyId in range(1, 10):
            for i in range(5):
                path = f'enemy{enemyId}/run{i}.txt'
                if(os.path.isfile(path)):
                    population = np.append(population, np.loadtxt(path))
                else:
                    no_solutions += 1
                    break

        remaining_size = population_size - 5 * (9 - no_solutions)
        population = population.reshape(5 * (9 - no_solutions), genome_length)
        return np.append(population, InitPopulation.basic(hidden_layer_size, input_size, remaining_size, enemies), axis=0)

    def genome_adaptive_with_best(hidden_layer_size, input_size, population_size, enemies):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1) + 1
        population = np.array([])
        no_solutions = 0

        for enemyId in range(1, 10):
            for i in range(5):
                path = f'enemy{enemyId}/run{i}.txt'

                if(os.path.isfile(path)):
                    sigma = np.random.uniform(0, 1)
                    population = np.append(population, np.append(np.loadtxt(path), sigma))
                else:
                    no_solutions += 1
                    break

        remaining_size = population_size - 5 * (9 - no_solutions)
        population = population.reshape(5 * (9 - no_solutions), genome_length)

        return np.append(population, InitPopulation.genome_adaptive(hidden_layer_size, input_size, remaining_size, enemies), axis=0)
