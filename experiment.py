import numpy as np


DEBUG = True


class Experiment:

    best_solutions = np.array([[]])  # 2D array which stores best member/solution of every run
    best_solutions_fitness = np.array([])  # array of best solution's fitness of every run

    def __init__(self, _evolutionary_algorithm):
        self.evolutionary_algorithm = _evolutionary_algorithm

    def run_experiment(self, number_of_runs):

        # store average fitness per generation in array
        avg_fitness_gen = np.array([])
        max_fitness_gen = np.array([])

        # store the mean of the best from each generations in array

        for i in range(number_of_runs):
            best, temp_fitness, temp_avg, temp_max = self.evolutionary_algorithm.run()  # RUN ALGORITHM
            self.best_solutions_fitness = np.append(self.best_solutions_fitness, temp_fitness)
            self.best_solutions = np.append(self.best_solutions, best)
            avg_fitness_gen = np.append(avg_fitness_gen, temp_avg)
            max_fitness_gen = np.append(max_fitness_gen, temp_max)

            # save best solution for each run to .txt file (sorry marc)
            runname = self.evolutionary_algorithm.experiment_name + "/run" + str(i) + ".txt"
            # if not os.path.exists(runname):
            np.savetxt(runname, best, delimiter=",")
            # else:
            #     np.savetxt(runname, best, delimiter=",")

            if DEBUG:
                print(
                    f'RUN {i+1}: Average generation fitness: {avg_fitness_gen, avg_fitness_gen.shape} \n\n\n Fitness of the best solutions {self.best_solutions_fitness}')
        # Plot the results of all experimental runs
        return avg_fitness_gen, max_fitness_gen
