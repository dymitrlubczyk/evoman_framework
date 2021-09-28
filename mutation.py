import numpy as np


class Mutation:
    # This class contains diffrent selection implementations

    # This value should be in (0, 1) - TODO: play around with higher values
    mutation_ratio = 0.1

    @staticmethod
    def basic(selected_group):
        # selected_group is a subset of population selected to be mutated
        # Mutates mutation_ratio % of genes of selected individual, creating mutant
        # selected_group_count mutants will be created

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
        genome_length = selected_group.shape[1]
        mutated_genes_count = round(Mutation.mutation_ratio * genome_length) # 0.1 * 105 = 10.5 = 11

        selected_group_count = selected_group.shape[0] # how many individuals are selected for mutation
        mutants = np.array([])

        for i in range(selected_group_count):
            mutant = selected_group[np.random.randint(selected_group_count)]

            for j in range(mutated_genes_count):
                gene_index = np.random.randint(genome_length)
                # DRAW A RANDOM VALUE FROM A UNIFORM DISTRIBUTION 
                mutant[gene_index] = np.random.uniform(-1.0, 1.0)

            mutants = np.concatenate((mutants, mutant), axis=None)

        return mutants.reshape(selected_group_count, genome_length)
