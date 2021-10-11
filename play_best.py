import numpy as np
import os
sys.path.insert(0, 'evoman')
sys.path.insert(0, 'other')

from environment import Environment
from demo_controller import player_controller
DEBUG = True
EXTRA_DETAILS = True


class PlayBest:
    def __init__(self, _env):
        self.env = _env

    def run_best_solutions(self, path, name):
        avg_gain_measure_ex = np.array([])
        # ADD ARRAYS FOR OTHER INTERESTING DATA HERE? LIKE TIME ETC.
        sol = np.loadtxt(path)

        self.init_final_enviornment(self, name,1)

        print("RUN FOR: ", path)

        for i in range(5):
            avg_gain_measure_run = np.array([])
            for en in range(1, 9):
                self.env.update_parameter('enemies',[en])
                temp_fitness, temp_player_life, temp_enemy_life, temp_time = self.env.play(
                    sol)  # MIGHT HAVE TO USE SIMULATE AND NOT PLAY HERE!
                avg_gain_measure_run = np.append(avg_gain_measure_run, (temp_player_life-temp_enemy_life))

                if (DEBUG == True):
                    print("The temp fitness for run ", i, " is ", temp_fitness)
                    if(EXTRA_DETAILS == True):
                        print("Player life: ", temp_player_life, " -- Enemy life: ",
                            temp_enemy_life, " -- Time: ", temp_time)
            avg_gain_measure_ex = np.append(avg_gain_measure_ex, np.sum(avg_gain_measure_run))
        return np.average(avg_gain_measure_run)

    def init_final_enviornment(self, name,n):
        
        os.environ["SDL_VIDEODRIVER"] = "windib"

        self.env = Environment(experiment_name=name,
                            enemies=n,
                            multiplemode="yes",
                            playermode="ai",
                                player_controller=player_controller(10),
                                enemymode="static",
                                level=2,
                                speed="fastest")
    
    def run_absolute_best_individual(self, path):
        avg_player_life_all = np.array([])
        avg_enemy_life_all =np.array([])
        sol = np.loadtxt(path)

        self.init_final_enviornment(self, "best", 1)
        for en in range(1, 9):
            avg_player_life_1enemy = np.array([])
            avg_enemy_life_1enemy = np.array([])

            self.env.update_parameter('enemies',[en])
            for i in range(5):
                temp_fitness, temp_player_life, temp_enemy_life, temp_time = self.env.play(
                    sol)  # MIGHT HAVE TO USE SIMULATE AND NOT PLAY HERE!
                avg_gain_measure_run = np.append(avg_gain_measure_run, (temp_player_life-temp_enemy_life))

                if (DEBUG == True):
                    print("The temp fitness for run ", i, " is ", temp_fitness)
                    if(EXTRA_DETAILS == True):
                        print("Player life: ", temp_player_life, " -- Enemy life: ",
                            temp_enemy_life, " -- Time: ", temp_time)
        avg_player_life_all = np.append(avg_player_life_all, np.mean(avg_player_life_1enemy))
        avg_enemy_life_all = np.append(avg_enemy_life_all, np.mean(avg_enemy_life_1enemy))
        
