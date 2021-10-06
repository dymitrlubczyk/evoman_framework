import numpy as np

from crossover import Crossover
from selection import Selection
from mutation import Mutation
from mutation_selection import MutationSelection


class Tuner:

    steps_count = 3
    evolutionary_algorithm_runs = 3

    def __init__(self, _evolutionary_algorithm):
        self.evolutionary_algorithm = _evolutionary_algorithm

    def run(self):
        for alpha in [0.8, 0.6, 0.4, 0.3, 0.1]:

            print(f'Range: +/-{100*alpha}%')
            self.tune_parameter(Mutation.sigma, alpha, self.set_mutation_sigma)

            print('Mutation ratio - ', Mutation.sigma)

            print('\n\n\n')

    def tune_parameter(self, current_value, alpha, setter):
        bottom = (1 - alpha) * current_value
        top = (1 + alpha) * current_value
        best_value = 0
        best_score = 0

        for value in np.linspace(bottom, top, Tuner.steps_count):
            setter(value)
            score = self.test_algorithm()
            if(score > best_score):
                best_value = value
                best_score = score

        setter(best_value)

    def test_algorithm(self):
        score = 0
        for i in range(Tuner.evolutionary_algorithm_runs):
            _, best_fitness, _ = self.evolutionary_algorithm.run()
            score += best_fitness

        return score

    def set_mutation_ratio(self, value):
        Mutation.mutation_ratio = value

    def set_mutation_sigma(self, value):
        Mutation.sigma = value

    def set_selection_ratio(self, value):
        Selection.selection_ratio = value

    def set_mutation_selection_ratio(self, value):
        MutationSelection.selection_ratio = value

    def set_offspring_ratio(self, value):
        Crossover.offspring_ratio = value
