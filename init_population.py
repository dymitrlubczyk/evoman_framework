import numpy as np


class InitPopulation:

    @staticmethod
    def basic(hidden_layer_size, input_size, population_size):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1)

        population = np.random.uniform(-1, 1, population_size * genome_length)
        return population.reshape(population_size, genome_length)

    def genome_adaptive(hidden_layer_size, input_size, population_size):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1) + 1

        population = np.random.uniform(-1, 1, population_size * genome_length)
        return population.reshape(population_size, genome_length)
