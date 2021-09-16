import numpy as np
import matplotlib.pyplot as plt
import math


class Experiment:

    # avg_fitness = np.array([])  # arrays of average fitnesses of every run of generation
    best_solutions = np.array([])  # array of best solution of every run
    best_solutions_fitness = np.array([])  # array of best solution's fitness of every run

    def __init__(self, _evolutionary_algorithm):
        self.evolutionary_algorithm = _evolutionary_algorithm

    def run_experiment(self, experiments):
        avg_fitness_gen = np.array([])
        for i in range(experiments):
            best, best_fitness, avg_generation_fitness = self.evolutionary_algorithm.run()
            avg_fitness_gen = np.concatenate(self.avg_fitness, avg_generation_fitness)
            self.best_solutions = np.concatenate(self.best_solutions, best)
            self.best_solutions_fitess = np.concatenate(self.best_solutions_fitess, best_fitness)

        # Plot all you need to plot
        self.line_plot(avg_fitness_gen, experiments)
        # Save best of best_solutions to wonderful CSV file <3

    def line_plot(self, average_fitness_generation, num_experiments):
        """
            Implements the plotting of the generational average fitness value & the highest fitness value
            Is called after each experiment

        """
        # 1. ASSIGN ARRAY OF AVERAGE FITNESSES OF ALL GENERATIONS TO DATAPOINTS
        data_points = average_fitness_generation
        
        # 2. PLOT DATAPOINTS AGAINST EXPERIMENT_NUMBER
        plt.plot(num_experiments, data_points, label="average generation fitness per experiment")

        # 3. PLOT PARAMS
        xint = range(min(num_experiments), math.ceil(max(num_experiments)) + 1)
        plt.xticks(xint)  # set y-axis to only integer values
        plt.xlabel('generation')
        plt.ylabel('average fitness')

        plt.show()

