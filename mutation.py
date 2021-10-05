import numpy as np


class Mutation:
    """
        Performs the mutation on the individuals in the Mating set


        Mutation ratio shows highest
        Params:
        -------
        mutation_ratio : set by specialist.py


        Methods:
        --------
        uniform(selected_group): draws perturbation value (float) from a uniform distribution
        success_rate(mutant, parent)    : TODO: proportion of successful mutations where child is superior to parent; helps evaluate mutation_rate parameter

    """
    mutation_ratio = 0.05
    sigma = 0.3
    reduction = 0.9

    @staticmethod
    def uniform(selected_group, generation, generation_count, pop_size):
        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        selected_group_count = selected_group.shape[0]
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] = np.random.uniform(-1.0, 1.0)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)

    @staticmethod
    def gaussian(selected_group, generation, generation_count, pop_size):

        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        selected_group_count = selected_group.shape[0]
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] = min(max(np.random.normal(
                    0, Mutation.sigma) + mutant[gene_index], -1), 1)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)
    
    @staticmethod
    def generation_adaptive(selected_group, generation, generation_count, pop_size):
        Mutation.sigma = Mutation.sigma * Mutation.reduction * (1 - (generation / generation_count))

        return Mutation.gaussian(selected_group, generation, generation_count, pop_size)
    
    @staticmethod
    def genome_adaptive(selected_group, generation, generation_count, pop_size):
        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        selected_group_count = selected_group.shape[0]
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            sigma = mutant[genome_length - 1]
            new_sigma = sigma * np.exp(np.random.normal(0, 1) / np.sqrt(pop_size))
            mutant[genome_length - 1] = new_sigma

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] = min(max(np.random.normal(0, abs(new_sigma)) +
                                             mutant[gene_index], -1), 1)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)
