from os import altsep
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from numpy.ma.extras import average

DEBUG = True

class Plotter:
    
    
    def line_plot(average_fitness_generation, best_solutions_fitness, num_gens): #TODO: add experiment 2 data here :)
        """
            Implements the plotting of the generational average fitness value & the highest fitness value
            Is called after each experiment

        """
        # 1. PROCESS THE DATA - GET THE MEAN OF MEANS, MEAN OF MAXES AND THE STANDARD DEVIATION FOR BOTH    
        data_points_avg = np.array([]) #create array that will contain the mean of means
        data_points_max = np.array([]) #create array that will contain the mean of maxes
        standard_deviations_average = np.array([]) #create array that will contain calculated standard deviations.
        standard_deviations_max = np.array([])


        for i in range(num_gens):
            avg_of_a_gen = np.array([])
            max_of_a_gen = np.array([])
            for j in range(num_gens): #this has to be able to be done more efficiently... we'll figure out of that later
                if(j % num_gens == i):
                    #Using modulo we can sort the generations with eachother and calculate the "mean of means" and "mean of maxes"
                    avg_of_a_gen = np.append(avg_of_a_gen, average_fitness_generation[j])
                    max_of_a_gen = np.append(max_of_a_gen, best_solutions_fitness[j])
            #rounding the generation
            data_points_avg = np.append(data_points_avg, np.average(avg_of_a_gen))
            data_points_max = np.append(data_points_max, np.average(max_of_a_gen))
            standard_deviations_average = np.append(standard_deviations_average, np.std(avg_of_a_gen))
            standard_deviations_max = np.append(standard_deviations_max, np.std(max_of_a_gen))



        # 2. FILL ARRAY WITH VALUES CORRESPONDING TO NUMBER OF EXPERIMENTS
        array_gens = np.array([i+1 for i in range(num_gens)]) # list comprehension
        
        #if DEBUG: print(f'Experiments array = {array_experiments, array_experiments.shape}; Average fitnesses array = {data_points, data_points.shape}')

        # 3. PLOT DATAPOINTS AGAINST EXPERIMENT_NUMBER
        #REMOVE LATER MAYBE --- plt.plot(array_experiments, data_points, label="average generation fitness for experiment")
        figure, plot = plt.subplots()
        plot.errorbar(array_gens, data_points_avg, yerr=standard_deviations_average, marker="o", color = "blue", label="Means of means")
        plot.errorbar(array_gens, data_points_max, yerr=standard_deviations_max, marker="o", color = "red", label= "Means of maxes")
        plot.legend(loc='upper left')
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