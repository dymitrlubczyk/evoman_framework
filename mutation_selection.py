
class MutationSelection:
    # This class is used to select individuals to be mutated

    selection_ratio = 0.3

    def only_parents(parents, offspring, population):
        selected_count = round(MutationSelection.selection_ratio * parents.shape[0])
        return parents[:selected_count, :]

    def only_offspring(parents, offspring, population):
        selected_count = round(MutationSelection.selection_ratio * offspring.shape[0])
        return offspring[:selected_count, :]

    def whole_population(parents, offspring, population):
        selected_count = round(MutationSelection.selection_ratio * population.shape[0])
        print(f"Selected Count: {selected_count}, Population index 0: {population[0]} Selected population: {population[:selected_count, :]}")
        return population[:selected_count, :]