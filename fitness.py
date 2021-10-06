import numpy as np
from timer import Timer


DEBUG = False


class Fitness:
    # This class contains diffrent selection implementations

    # (0,1> the bigger it is the more genomers are considered neighbours
    niche_ratio = 0.1

    @staticmethod
    # @ jit(nopython=True)
    def basic(population, env):
        t = Timer()
        time = np.array([])
        fitness = np.array([])

        for individual in population:
            t.start()
            f, pl, el, ti = env.play(pcont=individual)
            time_elapsed = t.stop()
            if DEBUG:
                print(f'Play of game took {time_elapsed:0.4f} seconds...')
            fitness = np.append(fitness, f)
            time = np.append(time, time_elapsed)

        return fitness, time

    def niche(population, env):
        t = Timer()  # import Timer
        genome_length = population.shape[1]
        max_norm = np.linalg.norm(np.full((genome_length), 2))
        niche_size = Fitness.niche_ratio * max_norm

        distances = np.array([])

        # t.start()  # Time how long fitness calculation takes

        fitness, time = Fitness.basic(population, env)  # Throws unsupported dtype for numba
        # time_elapsed = t.stop()

        # print(tabulate([["Average", np.average(time)], ["Max", np.max(time)], ["Min", np.min(time)], [
        #       "Total", time_elapsed]], headers=['Type', 'Time'], tablefmt='github'))

        for individual in population:  # numba doesn't support direct iteration
            distance = 0
            for neighbour in population:
                if np.linalg.norm(individual - neighbour) < niche_size:
                    distance += 1 - np.linalg.norm(individual - neighbour) / max_norm
            distances = np.append(distances, distance)
        return fitness / distances

    def genome_adaptive_niche(population, env):
        population = population[:, :-1]

        return Fitness.niche(population, env)
