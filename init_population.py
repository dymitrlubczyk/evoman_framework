import numpy as np
import os


class InitPopulation:

    population = np.array([])

    @staticmethod
    def basic(hidden_layer_size, input_size, population_size, genome_adaptive):

        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1)

        if(genome_adaptive):
            genome_length += 1

        population = np.random.uniform(-1, 1, population_size * genome_length)
        return population.reshape(population_size, genome_length)

    @staticmethod
    def same_population(hidden_layer_size, input_size, population_size, genome_adaptive):
        if(InitPopulation.population.shape[0] == 0):
            InitPopulation.population = InitPopulation.basic(
                hidden_layer_size, input_size, population_size, genome_adaptive)

        return InitPopulation.population

    @staticmethod
    def with_best(hidden_layer_size, input_size, population_size, genome_adaptive):
        genome_length = hidden_layer_size * (input_size + 1) + 5 * (hidden_layer_size + 1)
        if(genome_adaptive):
            genome_length += 1

        population = np.array([])
        no_solutions = 0
        enemies_count = 8

        for enemy_id in range(enemies_count):
            for i in range(3):
                path = f'enemy{enemy_id+1}/run{i}.txt'
                if(os.path.isfile(path)):
                    genome = np.loadtxt(path)

                    if(genome_adaptive):
                        genome = np.append(genome, np.random.uniform(0, 1))

                    population = np.append(population, genome)
                else:
                    no_solutions += 1
                    break

        remaining_size = population_size - 5 * (enemies_count - no_solutions)
        population = population.reshape(5 * (enemies_count - no_solutions), genome_length)

        return np.append(population, InitPopulation.basic(hidden_layer_size, input_size, remaining_size, genome_adaptive), axis=0)
