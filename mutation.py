import numpy as np


class Mutation:
    # This class contains diffrent selection implementations

    # This value should be in (0, 1]
    mutation_ratio = 0.1

    # Keep in mind that mutants count CANNOT exceed popualtion count
    mutants_ratio = 0.3

    @staticmethod
    def basic(selected_group):
        # selected_group is a subset of population selected to be mutated
        # Mutates mutation_ratio % of genes of selected individual, creating mutant
        # mutants_ratio times selected_group_count mutants will be created

        genome_length = selected_group.shape[1]
        group_count = selected_group.shape[0]
        mutants = np.array([])
        mutants_count = round(Mutation.mutants_ratio * group_count)
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length)

        for i in range(mutants_count):
            individual = selected_group[np.random.randint(group_count)]
            mutant = np.array(individual)

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                mutant[gene_index] = np.random.randint(-1, 1)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(mutants_count, genome_length)
