import numpy as np
import sys
sys.path.insert(0, 'evoman')
sys.path.insert(0, 'other')

from environment import Environment
from demo_controller import player_controller
import numpy as np
import os

DEBUG = True
EXTRA_DETAILS = True

class Play_best:

    def run_best_solutions(path, ex): #TODO make
        mean_of_best_individuals = np.array([])
        #ADD ARRAYS FOR OTHER INTERESTING DATA HERE? LIKE TIME ETC.
        sol = np.loadtxt(path)
        
        os.environ["SDL_VIDEODRIVER"] = "windib" #WINDIB for windows... no clue for mac.... might have to remove this..
        #SET ENVIRONMENT BASED ON ALGO.
        env = ex.evolutionary_algorithm.env

        for i in range(5):
            temp_fitness, temp_player_life, temp_enemy_life, temp_time = env.play(sol) #MIGHT HAVE TO USE SIMULATE AND NOT PLAY HERE!
            mean_of_best_individuals = np.append(mean_of_best_individuals, temp_fitness)
            if (DEBUG == True): 
                print("The temp fitness for run ", i, " is ", temp_fitness)
                if(EXTRA_DETAILS == True):
                    print("Player life: ", temp_player_life, " -- Enemy life: ", temp_enemy_life, " -- Time: ", temp_time)
        
        return np.average(mean_of_best_individuals)