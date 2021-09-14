import sys
sys.path.insert(0, 'evoman')

from environment import Environment
from demo_controller import player_controller
import numpy as np
import os


class EvolutionaryAlgorithm:
    def __init__(self,
                 _experiment_name,
                 _population_size,
                 _generations_number,
                 _selection,
                 _crossover,
                 _mutation,
                 _insertion):

        self.experiment_name = _experiment_name
        self.population_size = _population_size
        self.generations_number = _generations_number
        self.selection = _selection
        self.crossover = _crossover
        self.mutation = _mutation
        self.insertion = _insertion
        self.initialiseEnvironment()

    def findSolution(self):
        self.initialisePopulation()
        # exp = Experiment()
        generation = 1
        best, best_fitness = self.population[0], self.getFitness()[0]
        
        while(generation <= self.generations_number):
            fitness = self.getFitness() # Fitness of the generation; sum array to get total
            
            for i in range(self.population.shape[0]):
                if fitness[i] > best_fitness:
                    best, best_fitness = self.population[i], fitness[i]

            # Selects candidates for crossover & mutation
            selected_individuals = self.selection(fitness, self.population)
            newcomers = self.crossover(selected_individuals)
            

            # Create next generation
            self.population = self.insertion(
                fitness, self.population, newcomers)
            
            
            #TODO: call plot_data of Experiment() to calculate average fitness of current generation
            # store_data(generation, fitness, best)

            print(f'Current best: {best}, {best_fitness}')
            generation += 1

        # STORE BEST SOLUTION

        return self.selection(fitness, self.population)[0]

    def getFitness(self):
        fitness = np.array([])

        for i in range(self.population_size):
            # REPLACE WITH CUSTOM FITNESS FUNCTION
            f, pl, el, t = self.env.play(pcont=self.population[i]) # returns fitness of pcontroller at idx i
            fitness = np.append(fitness, f)

        return fitness

    def initialisePopulation(self):
        genome_length = 5 * (self.env.get_num_sensors() + 1)
        self.population = np.random.uniform(-1, 1,
                                            self.population_size * genome_length,)

        self.population = self.population.reshape(
            self.population_size, genome_length)

    def initialiseEnvironment(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        if not os.path.exists(self.experiment_name):
            os.makedirs(self.experiment_name)

        self.env = Environment(experiment_name=self.experiment_name,
                               enemies=[1],
                               playermode="ai",
                               player_controller=player_controller(0),
                               enemymode="static",
                               level=2,
                               speed="fastest")



class ActivationFunction:
    """
    Class which implements various activation functions.

    Methods
    -------
    sigmoid : return value between 0 & 1 (values towards -∞ become 0; values towards +∞ become 1)
    tanh : return value between -1 & 1 (valuable if network layers > 1)
    Gaussian : return value between 0 & 1 (probability distribution)
    """
    def sigmoid(x):
        pass

    def tanh(x):
        pass

    def Gaussian(x):
        pass

class FitnessFunction:

    def default_fitness(n_pop, env, pop):
        """
        Implements:
        f = 0.9 · (100 - e) + 0.1 * p - log t
            - e = enemy energy
            - p = player energy
            - t = time

        Params
        ------
        n_pop : population size
        env : environment object
        pop : population of solutions/genomes
        """
        fitness = np.array([])
        for i in range(n_pop):
            f, pl, el, t = env.play(pcont=pop[i])
            fitness = np.append(fitness, f)
        
        pass


class CrossOver:
    """
    Class which implements crossover methods


    """

    def crossover(self):
        pass


class Selection:
    """
    Class which implements selection methods.


    
    """

    def tournament_selection(pop, fitness, k):
        pass

    def flip_selection(pop, fitness):
        i = np.flip(np.argsort(fitness), axis=None)

        return pop[i[:(i.size // 5)], :]
