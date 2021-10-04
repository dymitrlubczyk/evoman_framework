from base_evolutionary_algorithm import EvolutionaryAlgorithm
from plotter import Plotter
from play_best import Play_best
import numpy as np

from experiment import Experiment
import specialist_1
import specialist_2

number_of_runs = 2

# SCRIPT ON BOTTOM RUNNING INDEPENDENTLY
# TODO:ADD TUNING HERE... will pick algos for us
# Pick your algorithms

for enemy_id in [2]:
    alg1 = specialist_1.get_algorithm(enemy_id, f"EA1_enemy{enemy_id}")
    alg2 = specialist_2.get_algorithm(enemy_id, f"EA2_enemy{enemy_id}")

    ex1 = Experiment(alg1)
    ex2 = Experiment(alg2)
    # Init generational data arrays
    avg_fitness_gen_ex1 = np.array([])
    best_fitness_gen_ex1 = np.array([])
    avg_fitness_gen_ex2 = np.array([])
    best_fitness_gen_ex2 = np.array([])

    # Run the experiment on the two different algos
    avg_fitness_gen_ex1, best_fitness_gen_ex1 = ex1.run_experiment(number_of_runs)
    avg_fitness_gen_ex2, best_fitness_gen_ex2 = ex2.run_experiment(number_of_runs)

    # Plot the results
    Plotter.line_plot(avg_fitness_gen_ex1, best_fitness_gen_ex1,
                      alg1.generations_number, enemy_id, 1)
    Plotter.line_plot(avg_fitness_gen_ex2, best_fitness_gen_ex2,
                      alg2.generations_number, enemy_id, 2)

    # TODO run the best individuals 5 times and track
    best_solution_run_ex1 = np.array([])
    best_solution_run_ex2 = np.array([])

    sol_path_ex1 = ex1.evolutionary_algorithm.experiment_name + "/run"
    sol_path_ex2 = ex2.evolutionary_algorithm.experiment_name + "/run"

    for i in range(number_of_runs):
        temp_fitness_avg_ex1 = Play_best.run_best_solutions(sol_path_ex1 + str(i) + ".txt", ex1)
        temp_fitness_avg_ex2 = Play_best.run_best_solutions(sol_path_ex2 + str(i) + ".txt", ex2)
        best_solution_run_ex1 = np.append(best_solution_run_ex1, temp_fitness_avg_ex1)
        best_solution_run_ex2 = np.append(best_solution_run_ex2, temp_fitness_avg_ex2)

    # TODO sort the best results data so that it can be plotted correctly

    # TODO run boxplots of the results of the best solutions from each run
    Plotter.box_plot(best_solution_run_ex1, best_solution_run_ex2, enemy_id)


print("Experiment over...")
# Experiment over...
