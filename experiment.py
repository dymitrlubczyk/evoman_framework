"""
Handles experiment data

"""


class Experiment:
    """
    Class used to represent the experiment.

    Attributes
    ----------
    None.

    Methods
    -------
    plot_data : takes in values of the current run (e.g. fitness, average_mean, std_dev) & plots the data
    store_data : store data for current generation 
    save_best_solutions : saves best solution from an experimental run
    """

    def store_data(self, fitness):
        """
        Stores the data from each generation
        Also stores data after all generations --> HOW?


        """
        pass

    def plot_data(self):
        """
        Uses matplotlib to visualize data collected during the experiment: not sure about the idea of "current" vs. "total" data.
        Use of parameters will depend on time when we decide to plot the data - after all generations have passed? NO - need to plot mean for each generation.

        Params
        ------
        n_gen : number of generations
            - hyperparams
        c_gen : current generation
            - i.e. f'gen{current iteration}' becomes label for x axis
        c_mean : mean fitness of current generation
            - c_mean = total_fitness/n_pop
        c_std_dev : standard deviation from the mean of the current generation
            - c_std_dev = np.std(population)
        c_max : max fitness value of current generation
            - c_max = best_fitness
        c_algo : name of current solution
        c_experiment : experiment name
        c_enemy : current enemy type
        (optional) t_mean : total mean of the whole evolutionary cycle (after all generations)
            - t_mean = sum c_mean of all gen
        """
        # 1. Store the data
        # 2. Plot the data

        pass

    def save_solution(self, solution, solution_fitness, experiment_name):
        pass
