import numpy as np


class Experiment:

    def __init__(self, _evolutionary_algorithm):
        self.fitnesses = np.array([])  # arrays of average fitnesses of every run of generation
        self.best_solutions = np.array([])  # array of best solution of every run
        self.best_solutions_fitess = np.array([])  # array of best solution's fitness of every run
        self.evolutionary_algorithm = _evolutionary_algorithm

    def run_experiment(self, times):
        for i in range(times):
            best, best_fitness, fitnesses = self.evolutionary_algorithm.run()
            self.fitnesses = np.concatenate(self.fitnesses, fitnesses)
            self.best_solutions = np.concatenate(self.best_solutions, best)
            self.best_solutions_fitess = np.concatenate(self.best_solutions_fitess, best_fitness)

        # Plot all you need to plot
        # Save best of best_solutions to wonderful CSV file <3
