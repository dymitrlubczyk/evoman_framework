from experiment import Experiment
from base_evolutionary_algorithm import EvolutionaryAlgorithm
from crossover import Crossover
from selection import Selection
from insertion import Insertion
from mutation import Mutation
from mutation_selection import MutationSelection


# Before you run evolutionary algorithm you can adjust following variables:

# Crossover.offspring_ratio - says what's the offspring/parents ratio, default 1.5
# Selection.selection_ratio - says how many % of population should be selected, default 0.3
# Mutation.mutation_ratio - says how many % of genes will be mutated, default 0.1
# MutationSelection.selection_ratio - says how many % of given group should be selected, default 0.3


Mutation.mutation_ratio = 0.3
MutationSelection.selection_ratio = 0.5

# HYPERPARAMS
population_size = 25
generations_number = 5
experiment_nums = 3

def run_algorithm():
    evolutionary_algorithm = EvolutionaryAlgorithm(_experiment_name='solution_1',
                                                _population_size=population_size,
                                                _generations_number=generations_number,
                                                _selection=Selection.basic,
                                                _crossover=Crossover.basic,
                                                _mutation=Mutation.uniform_mutation,
                                                _mutation_selection=MutationSelection.whole_population,
                                                _insertion=Insertion.basic)


    Experiment(evolutionary_algorithm).run_experiment(experiment_nums)

run_algorithm()
