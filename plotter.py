import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from numpy.ma.extras import average

DEBUG = True

class Plotter:
    
    
    def line_plot(average_fitness_generation_ex1, best_solutions_fitness_ex1, num_gens): #TODO: add experiment 2 data here :)
        """
            Implements the plotting of the generational average fitness value & the highest fitness value
            Is called after each experiment

        """
        # 1. PROCESS THE DATA SO THAT AVERAGES STICK NEXT TO AVERAGES
        data_points = np.array([]) #create array that will contain the means

        for i in range(num_gens):
            avg_of_a_gen = np.array([])
            for j in range(num_gens): #this has to be able to be done more efficiently... we'll figure out of that later
                if(j % num_gens == i):
                    avg_of_a_gen = np.append(avg_of_a_gen, average_fitness_generation_ex1[j])
            data_points = np.append(data_points, np.average(avg_of_a_gen))

        # 2. FILL ARRAY WITH VALUES CORRESPONDING TO NUMBER OF EXPERIMENTS
        array_gens = np.array([i+1 for i in range(num_gens)]) # list comprehension
        
        #if DEBUG: print(f'Experiments array = {array_experiments, array_experiments.shape}; Average fitnesses array = {data_points, data_points.shape}')

        # 3. PLOT DATAPOINTS AGAINST EXPERIMENT_NUMBER
        #REMOVE LATER MAYBE --- plt.plot(array_experiments, data_points, label="average generation fitness for experiment")
        plt.plot(array_gens, data_points, label="Average fitness per generation (all runs)")

        # 4. PLOT PARAMS
        xint = range(num_gens+1)
        plt.xticks(xint)  # set x-axis "ticks" to only integer values
        plt.xlabel('generation')
        plt.ylabel('average fitness')

        plt.show()

    def box_plot(performance): #Take in the results of the best individuals in the form of either: Gain Measure or Fitness
        """
        Plots the mean of the "performance" of the best individual from all runs.

        """

        pass