'''
SCRIPT MADE TO BE RUN INDEPENDANTLY AFTER WE HAVE EACH RUN A TRAINING GROUP EACH
'''

import numpy as np
from play_best import PlayBest
from plotter import Plotter

#Init these boys
player_life = np.array([])
enemy_life = np.array([])
objj = PlayBest()

#Run the best solution
player_life, enemy_life = objj.run_absolute_best_individual("best_sol/gigachad.txt")
Plotter.table_plot(player_life, enemy_life)

best_gain_run_ex1 = np.loadtxt("gains/gains1.txt")
best_gain_run_ex2 = np.loadtxt("gains/gains2.txt")
best_gain_run_ex3 = np.loadtxt("gains/gains3.txt")
best_gain_run_ex4 = np.loadtxt("gains/gains4.txt")

Plotter.t_test(best_gain_run_ex1, best_gain_run_ex2, best_gain_run_ex3, best_gain_run_ex4)