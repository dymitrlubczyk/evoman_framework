import numpy as np
from numba import jit
from timer import Timer

class Fitness:
    # This class contains diffrent selection implementations

    # (0,1> the bigger it is the more genomers are considered neighbours
    niche_ratio = 0.1

    

    @staticmethod
    def basic(population, env):
        fitness = np.array([])

        for individual in population:
            f, pl, el, t = env.play(pcont=individual)
            fitness = np.append(fitness, f)

        return fitness

    # @jit(nopython=False, parallel=True)
    def niche(population, env):
        t = Timer() # import Timer
        genome_length = population.shape[1]
        max_norm = np.linalg.norm(np.full((genome_length), 2))
        niche_size = Fitness.niche_ratio * max_norm

        distances = np.array([])

        t.start() # Time how long fitness calculation takes

        fitness = Fitness.basic(population, env) # Throws unsupported dtype for numba

        time_elapsed = t.stop()
        print(f"Calculating fitness took {time_elapsed:0.4f} seconds")
        print('=' * 45)

        for individual in population: # numba doesn't support direct iteration
            distance = 0
            for neighbour in population:
                if np.linalg.norm(individual - neighbour) < niche_size:
                    distance += 1 - np.linalg.norm(individual - neighbour) / max_norm
            distances = np.append(distances, distance)
        return fitness / distances
