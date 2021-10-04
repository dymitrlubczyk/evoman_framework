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
        basic(selected_group)           : draws perturbation value (int) from a discrete uniform distribution
        uniform_mutation(selected_group): draws perturbation value (float) from a uniform distribution
        success_rate(mutant, parent)    : TODO: proportion of successful mutations where child is superior to parent; helps evaluate mutation_rate parameter

    """
    mutation_ratio = 0.05

    @staticmethod
    def basic(selected_group):
        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        selected_group_count = selected_group.shape[0]
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] = np.random.randint(-1, 1)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)


    def uniform_mutation(selected_group):
        """
            Perturbs the value of a gene by drawing a value from a uniform distribution
            with values between [-1.0, 1.0]

            Params
            ------
            selected_group: the set of individuals returned by the mutation_selection
        """
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

    def gaussian_mutation(selected_group):
        sigma = 0.3
        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        selected_group_count = selected_group.shape[0]
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] += min(max(np.random.normal(0, sigma), -1), 1)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)
