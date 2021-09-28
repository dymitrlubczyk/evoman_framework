from experiment import Experiment
from base_evolutionary_algorithm import EvolutionaryAlgorithm

from fitness import Fitness
from crossover import Crossover
from selection import Selection
from insertion import Insertion
from mutation import Mutation
from mutation_selection import MutationSelection
from experiment import Experiment

# Before you run evolutionary algorithm you can adjust following variables:

# Crossover.offspring_ratio - says what's the offspring/parents ratio, default 1.5
# Selection.selection_ratio - says how many % of population should be selected, default 0.3
# Mutation.mutation_ratio - says how many % of genes will be mutated, default 0.1
# MutationSelection.selection_ratio - says how many % of given group should be selected, default 0.3

# HYPERPARAMS

population_size = 5
generations_number = 2


Mutation.mutation_ratio = 0.24
Crossover.offspring_ratio = 1.42
Selection.selection_ratio = 0.31
MutationSelection.selection_ratio = 0.338

evolutionary_algorithm = EvolutionaryAlgorithm(_experiment_name='solution_1',
                                               _population_size=population_size,
                                               _generations_number=generations_number,
                                               _hidden_layer_size=10,
                                               _fitness=Fitness.niche,
                                               _selection=Selection.tournament,
                                               _crossover=Crossover.basic,
                                               _mutation=Mutation.uniform_mutation,
                                               _mutation_selection=MutationSelection.only_parents,
                                               _insertion=Insertion.basic)
