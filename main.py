from plotter import Plotter
from play_best import PlayBest
import numpy as np


from experiment import Experiment
#import specialist_1
#import specialist_2
import generalist_1
import generalist_2

number_of_runs = 2
enemy_group1=[5,7,8]
enemy_group2=[1,3,4] 

alg1 = generalist_1.get_algorithm(enemy_group1, f"EA1_group1")
alg2 = generalist_2.get_algorithm(enemy_group1, f"EA2_group1")
'''DIMA USE THESE - COMMENT AWAY THOSE ABOVE
alg3 = generalist_1.get_algorithm(enemy_group2, f"EA1_group2")
alg4 = generalist_2.get_algorithm(enemy_group2, f"EA2_group2")
'''
ex1 = Experiment(alg1)
ex2 = Experiment(alg2)
'''DIMA USE THESE - COMMENT AWAY THOSE ABOVE
ex3 = Experiment(alg3)
ex4 = Experiment(alg4)
'''

# Init generational data arrays
avg_fitness_gen_ex1 = np.array([])
best_fitness_gen_ex1 = np.array([])
avg_fitness_gen_ex2 = np.array([])
best_fitness_gen_ex2 = np.array([])
'''DIMA USE THESE - COMMENT AWAY THOSE ABOVE
avg_fitness_gen_ex3 = np.array([])
best_fitness_gen_ex3 = np.array([])
avg_fitness_gen_ex4 = np.array([])
best_fitness_gen_ex4 = np.array([])
'''

# Run the experiment on the two different algos
avg_fitness_gen_ex1, best_fitness_gen_ex1 = ex1.run_experiment(number_of_runs)
avg_fitness_gen_ex2, best_fitness_gen_ex2 = ex2.run_experiment(number_of_runs)
'''DIMA USE THESE - COMMENT AWAY THOSE ABOVE
avg_fitness_gen_ex3, best_fitness_gen_ex3 = ex3.run_experiment(number_of_runs)
avg_fitness_gen_ex4, best_fitness_gen_ex4 = ex4.run_experiment(number_of_runs)
'''

# Plot the results
Plotter.line_plot(avg_fitness_gen_ex1, best_fitness_gen_ex1,
                    alg1.generations_number, 1, 1)
Plotter.line_plot(avg_fitness_gen_ex2, best_fitness_gen_ex2,
                    alg2.generations_number, 1, 2)
'''DIMA USE THESE - COMMENT AWAY THOSE ABOVE
Plotter.line_plot(avg_fitness_gen_ex3, best_fitness_gen_ex3,
                    alg3.generations_number, 2, 1)
Plotter.line_plot(avg_fitness_gen_ex4, best_fitness_gen_ex4,
                    alg4.generations_number, 2, 2)                    
'''

best_gain_run_ex1 = np.array([])
best_gain_run_ex2 = np.array([])

'''DIMA USE THESE COMMENT AWAY THOSE ABOVE
best_gain_run_ex3 = np.array([])
best_gain_run_ex4 = np.array([])
'''
best_sol = -100 #max minimum
best_sol_str = ""

sol_path_ex1 = ex1.evolutionary_algorithm.experiment_name + "/run"
sol_path_ex2 = ex2.evolutionary_algorithm.experiment_name + "/run"
'''DIMA USE THESE COMMENT AWAY THOSE ABOVE
sol_path_ex3 = ex3.evolutionary_algorithm.experiment_name + "/run"
sol_path_ex4 = ex4.evolutionary_algorithm.experiment_name + "/run"
'''
objj = PlayBest()

for i in range(number_of_runs):
    temp_gain_avg_ex1 = objj.run_best_solutions(sol_path_ex1 + str(i) + ".txt", "name1")
    temp_gain_avg_ex2 = objj.run_best_solutions(sol_path_ex2 + str(i) + ".txt", "name2")
    
    '''DIMA USE THESE
    temp_gain_avg_ex3 = objj.run_best_solutions(sol_path_ex2 + str(i) + ".txt", "name3")
    temp_gain_avg_ex4 = objj.run_best_solutions(sol_path_ex2 + str(i) + ".txt", "name4")
    '''

    best_gain_run_ex1 = np.append(best_gain_run_ex1, temp_gain_avg_ex1)
    best_gain_run_ex2 = np.append(best_gain_run_ex2, temp_gain_avg_ex2)
    
    '''DIMA USE THESE
    best_gain_run_ex3 = np.append(best_gain_run_ex3, temp_gain_avg_ex3)
    best_gain_run_ex4 = np.append(best_gain_run_ex4, temp_gain_avg_ex4)
    '''

    if(temp_gain_avg_ex1 > best_sol):
        best_sol = temp_gain_avg_ex1
        best_sol_str = sol_path_ex1+str(i)+".txt"
        print("BEST SOL FOUND 1")
    if(temp_gain_avg_ex2 > best_sol):
        best_sol = temp_gain_avg_ex2
        best_sol_str = sol_path_ex2+str(i)+".txt"
        print("best sol found 2")
    '''DIMA USE THESE
    if(temp_gain_avg_ex3 > best_sol):
        best_sol = temp_gain_avg_ex3
        best_sol_str = sol_path_ex3+str(i)+".txt"
    if(temp_gain_avg_ex4 > best_sol):
        best_sol = temp_gain_avg_ex4
        best_sol_str = sol_path_ex4+str(i)+".txt"
    '''

Plotter.box_plot(best_gain_run_ex1, best_gain_run_ex2, 1)

best_individual = np.loadtxt(best_sol_str)
'''DIMA USE THESE
Plotter.box_plot(best_gain_run_ex3, best_gain_run_ex4, 2)
'''

np.savetxt("gains/gains1.txt", best_gain_run_ex1, delimiter=',')
np.savetxt("gains/gains2.txt", best_gain_run_ex2, delimiter=',')
'''DIMA USE THESE - comment out those above
np.savetxt("gains/gains3.txt", best_gain_run_ex3, delimiter=',')
np.savetxt("gains/gains4.txt", best_gain_run_ex4, delimiter=',')
'''

np.savetxt("best_sol/gigachad.txt", best_individual, delimiter=',')

print("Experiment over...")
