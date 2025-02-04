import numpy as np


class Fitness:
    # This class contains diffrent selection implementations

    # (0,1> the bigger it is the more genomers are considered neighbours
    niche_ratio = 0.1

    @staticmethod
    def basic(population, env, genome_adaptive):
        fitness = np.array([])

        if(genome_adaptive):
            population = population[:, :-1]

        for individual in population:
            f, pl, el, ti = env.play(pcont=individual)
            fitness = np.append(fitness, f)

        return fitness

    def niche(population, env, genome_adaptive):
        genome_length = population.shape[1]
        max_norm = np.linalg.norm(np.full((genome_length), 2))
        niche_size = Fitness.niche_ratio * max_norm

        distances = np.array([])

        fitness = Fitness.basic(population, env, genome_adaptive)

        for individual in population:

            distance = 0
            for neighbour in population:
                if np.linalg.norm(individual - neighbour) < niche_size:
                    distance += 1 - np.linalg.norm(individual - neighbour) / max_norm
            distances = np.append(distances, distance)
        return fitness / distances
