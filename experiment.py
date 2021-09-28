import numpy as np
import matplotlib.pyplot as plt
import math
import glob, os

from numpy.ma.extras import average
from base_evolutionary_algorithm import EvolutionaryAlgorithm
from plotter import Plotter
from play_best import Play_best

from fitness import Fitness
from crossover import Crossover
from selection import Selection
from insertion import Insertion
from mutation import Mutation
from mutation_selection import MutationSelection

DEBUG = True

#PARAMS START
# Before you run evolutionary algorithm you can adjust following variables:

# Crossover.offspring_ratio - says what's the offspring/parents ratio, default 1.5
# Selection.selection_ratio - says how many % of population should be selected, default 0.3
# Mutation.mutation_ratio - says how many % of genes will be mutated, default 0.1
# MutationSelection.selection_ratio - says how many % of given group should be selected, default 0.3

number_of_runs = 4 #FOR THE REPORT THIS IS TO BE SET TO 10

#PARAMS END
class Experiment:

    # avg_fitness = np.array([])  # arrays of average fitnesses of every run of generation
    best_solutions = np.array([[]])  # 2D array which stores best member/solution of every run
    best_solutions_fitness = np.array([])  # array of best solution's fitness of every run

    def __init__(self, _evolutionary_algorithm):
        self.evolutionary_algorithm = _evolutionary_algorithm

    def run_experiment(self, experiments):
        
        # store average fitness per generation in array
        avg_fitness_gen = np.array([])
        max_fitness_gen = np.array([])
        
        #store the mean of the best from each generations in array

        for i in range(experiments):
            best, best_fitness, temp_avg, temp_max = self.evolutionary_algorithm.run() #RUN ALGORITHM
            
            self.best_solutions = np.append(self.best_solutions, best) #maybe unecessary
            self.best_solutions_fitness = np.append(self.best_solutions_fitness, best_fitness) #maybe unecessary
            avg_fitness_gen = np.append(avg_fitness_gen, temp_avg)
            max_fitness_gen = np.append(max_fitness_gen, temp_max)

            #save best solution for each run to .txt file (sorry marc)
            runname = self.evolutionary_algorithm.experiment_name+"/run"+str(i)+".txt"
            if not os.path.exists(runname):
                np.savetxt(runname, best, delimiter=",")
            else:
                np.savetxt(runname, best, delimiter=",")

            if DEBUG: print(f'EXPERIMENT NUMBER {i+1}: Average generation fitness: {avg_fitness_gen, avg_fitness_gen.shape} \n\n\n Fitness of the best solutions {self.best_solutions_fitness}')
        # Plot the results of all experimental runs
        return avg_fitness_gen, max_fitness_gen
