import numpy as np
import sys
sys.path.insert(0, 'evoman')
sys.path.insert(0, 'other')

from environment import Environment
from demo_controller import player_controller
import numpy as np
import os

class play_best:

    def run_best_solutions(path): #TODO make
        mean_of_best_individuals = np.array([])
        sol = np.loadtext(path)
        #TODO: SET UP ENVIRONMENT!
        env = Environment(experiment_name="Final_Runs",
            enemies=[2],
            playermode="ai",
            player_controller=player_controller(10),
            enemymode="static",
            level=2,
            speed="fastest")
        for i in range(5):
            print("bruh") #remove this later
            temp_fitness, temp_player_life, temp_enemy_life, temp_time = env.play(sol) #MIGHT HAVE TO USE SIMULATE AND NOT PLAY HERE!
            mean_of_best_individuals = np.append(mean_of_best_individuals, temp_fitness)
        
        return np.average(mean_of_best_individuals)