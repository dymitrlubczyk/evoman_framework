import numpy as np
import matplotlib.pyplot as plt
import math
import glob, os

from numpy.ma.extras import average
from base_evolutionary_algorithm import EvolutionaryAlgorithm
from plotter import Plotter

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

Mutation.mutation_ratio = 0.08
Selection.selction_ratio = 1
MutationSelection.selction_ratio = 0.3

# HYPERPARAMS
population_size = 5
generations_number = 5
number_of_runs = 4 #FOR THE REPORT THIS IS TO BE SET TO 10

evolutionary_algorithm = EvolutionaryAlgorithm(_experiment_name='solution_1',
                                               _population_size=population_size,
                                               _generations_number=generations_number,
                                               _hidden_layer_size=10,
                                               _fitness=Fitness.niche,
                                               _selection=Selection.basic,
                                               _crossover=Crossover.basic,
                                               _mutation=Mutation.basic,
                                               _mutation_selection=MutationSelection.only_parents,
                                               _insertion=Insertion.basic)


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
            runname = evolutionary_algorithm.experiment_name+"/run"+str(i)+".txt"
            if not os.path.exists(runname):
                f = open(runname, "x")
                f.write(str(best))
                f.close()
            else:
                f = open(runname, "w")
                f.write(str(best))
                f.close()

            if DEBUG: print(f'EXPERIMENT NUMBER {i+1}: Average generation fitness: {avg_fitness_gen, avg_fitness_gen.shape} \n\n\n Fitness of the best solutions {self.best_solutions_fitness}')
        # Plot the results of all experimental runs
        return avg_fitness_gen, max_fitness_gen
        # Save best of best_solutions to wonderful CSV file <3

    def run_best_solutions(path): #TODO make
        mean_of_best_individuals = np.array([])
        sol = np.loadtext(path)
        #TODO: SET UP ENVIRONMENT!
        for i in range(5):
            print("bruh") #remove this later
            #temp_fitness = env.play(sol)
            #mean_of_best_individuals = np.append(mean_of_best_individuals, temp_fitness)
        
        return np.average(mean_of_best_individuals)
        

#Pick your algorithms
ex1 = Experiment(evolutionary_algorithm)
#ex2 = Experiment(evo_alg2)

#Init generational data arrays
avg_fitness_gen_ex1 = np.array([])
best_fitness_gen_ex1 = np.array([])
avg_fitness_gen_ex2 = np.array([]) 
best_fitness_gen_ex2 = np.array([])

#Run the experiment on the two different algos
avg_fitness_gen_ex1, best_fitness_gen_ex1 = ex1.run_experiment(number_of_runs)
#avg_fitness_gen2, best_fitness_gen2=ex2.run_experiment(number_of_runs)

#TODO: REPLACE THIS WITH TUNING? OR ADD TUNING HERE? Or above??

#Plot the results
Plotter.line_plot(avg_fitness_gen_ex1, best_fitness_gen_ex1, generations_number)
#Plotter.line_plot(avg_fitness_gen_ex2, best_fitness_gen_ex2, generations_number)
"""
#TODO run the best individuals 5 times and track
best_solution_run_ex1 = np.array([])
best_solution_run_ex2 = np.array([])

sol_path_ex1 = ex1.evolutionary_algorithm.experiment_name+"/run"
#sol_path_ex2 = ex2.evolutionary_algorithm.experiment_name+"/run"

for i in range(number_of_runs):
    temp_fitness_avg_ex1 = ex1.run_best_solution(sol_path_ex1+"i")
    #temp_fitness_avg_ex2 = ex2.run_best_solution(sol_path_ex1+"i")
    best_solution_run_ex1 = np.append(best_solution_run_ex1, temp_fitness_avg_ex1)
    #best_solution_run_ex2 = np.append(best_solution_run_ex2, temp_fitness_avg_ex2)

#TODO sort the best results data so that it can be plotted correctly

#TODO run boxplots of the results of the best solutions from each run
#Plotter.box_plot(best_solution_run_ex1, best_solution_run_ex2)
"""