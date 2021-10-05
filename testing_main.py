from base_evolutionary_algorithm import EvolutionaryAlgorithm
from plotter import Plotter
from play_best import Play_best
import numpy as np
import cProfile
import pstats
from pstats import SortKey

from experiment import Experiment
import specialist_1
import specialist_2

number_of_runs = 2

# SCRIPT ON BOTTOM RUNNING INDEPENDENTLY
# TODO:ADD TUNING HERE... will pick algos for us
# Pick your algorithms


def main():
    for enemy_id in [2]:
        alg1 = specialist_1.get_algorithm(enemy_id, f"EA1_enemy{enemy_id}")

        ex1 = Experiment(alg1)
        avg_fitness_gen_ex1 = np.array([])
        best_fitness_gen_ex1 = np.array([])


        # Run the experiment on the two different algos
        avg_fitness_gen_ex1, best_fitness_gen_ex1 = ex1.run_experiment(number_of_runs)

        best_solution_run_ex1 = np.array([])

        sol_path_ex1 = ex1.evolutionary_algorithm.experiment_name + "/run"

        # for i in range(number_of_runs):
        #     temp_fitness_avg_ex1 = Play_best.run_best_solutions(sol_path_ex1 + str(i) + ".txt", ex1)
        #     best_solution_run_ex1 = np.append(best_solution_run_ex1, temp_fitness_avg_ex1)

    print("Experiment over...")
    # Experiment over...

if __name__ == "__main__":
    cProfile.run("main()", 'output.dat')
    # convert cProfile dat file to readable output
    with open('output_time.txt', 'w') as f:
        p = pstats.Stats('output.dat', stream=f)
        p.sort_stats('time').print_stats()
    
    with open('output_calls.txt', 'w') as f:
        p = pstats.Stats('output.dat', stream=f)
        p.sort_stats('calls').print_stats()
