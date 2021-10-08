from base_evolutionary_algorithm import EvolutionaryAlgorithm

from fitness import Fitness
from crossover import Crossover
from init_population import InitPopulation
from selection import Selection
from insertion import Insertion
from mutation import Mutation
from mutation_selection import MutationSelection


def get_algorithm(enemies, experiment_name):
    population_size = 25
    generations_number = 2

    Mutation.mutation_ratio = 0.24
    Crossover.offspring_ratio = 1.42
    Selection.selection_ratio = 0.31
    MutationSelection.selection_ratio = 0.338

    evolutionary_algorithm = EvolutionaryAlgorithm(_experiment_name=experiment_name,
                                                   _multiple_mode="yes",
                                                   _population_size=population_size,
                                                   _generations_number=generations_number,
                                                   _enemies=enemies,
                                                   _hidden_layer_size=10,
                                                   _init_population=InitPopulation.basic,
                                                   _fitness=Fitness.niche,
                                                   _selection=Selection.tournament,
                                                   _crossover=Crossover.basic,
                                                   _mutation=Mutation.genome_adaptive,
                                                   _mutation_selection=MutationSelection.only_parents,
                                                   _insertion=Insertion.basic,
                                                   _genome_adaptive=True)
    return evolutionary_algorithm
