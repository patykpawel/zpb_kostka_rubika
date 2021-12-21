from rubik.cube import Cube
from myRubic import MyRubic
from time import sleep
from constants_tutorial import *
from utlis_genetic import *
from copy import deepcopy
import random
import numpy as np
import pandas as pd
import sys

# badanie:
# max ilość generacji na stage
# metody selekcji
# średnia ilość iteracji dla każdego z etapów
# wielkość populacji
# ilość rodziców


# do zrobienia
#       optymalizacja czasowa algorytmu
#       optymalizacja funkcji
#       badania dotyczące selekcji
#       art
#       a*
#       czemu nie rozwiązuje w stage 3
#       inne implementacje algorytmów (kociemba beginner)
#       znalezienie innych zastosowań algorytmów genetycznych dla kostki rubika


# strategia mi-lambda - rozmiar populacji, rodzicow
start_stage = state_stage0
max_per_generation = 10
no_parents = 10
no_population = 100
max_generations = 2
stages = [0, 1, 2, 3, 4]
stages_attempt = [0, 0, 0, 0]
selection_mode = "best"
file_name = "xd.json"

def run(generation):
    population = [MyRubic(Cube(start_stage)) for i in range(no_population)]
    best_cube_scramble = ""
    best_cube_fitness = None
    # print("start")
    for stage in stages:
        i = 0
        while not population_ready(population, stage):
            if i >= max_per_generation:
                return [best_cube_scramble, best_cube_fitness, False]
            i = i + 1
            new_population = []

            for cube in population:
                if stage == 0:
                    if cube.good_state1 == False:
                        no_moves = random.randint(1, max_moves_stage0)
                        moves = genrate_moves(stage0_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                        stages_attempt[stage] = i

                elif stage == 1:
                    if cube.good_state2 == False:
                        no_moves = random.randint(1, max_moves_stage1)

                        moves = genrate_moves(stage1_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                        stages_attempt[stage] = i

                elif stage == 2:
                    if cube.good_state3 == False:
                        no_moves = random.randint(1, max_moves_stage2)

                        moves = genrate_moves(stage2_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                        stages_attempt[stage] = i

                elif stage == 3:
                    if cube.good_state4 == False:
                        no_moves = random.randint(1, max_moves_stage3)

                        moves = genrate_moves(stage3_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                        stages_attempt[stage] = i
                    else:
                       stage = stage + 1 
                elif stage == 4:
                    # print(cube.cube)
                    # print(cube.fitness)
                    best_cube_scramble = cube.cube2str()
                    best_cube_fitness = cube.fitness
                    # print("Koniec")
                    return [best_cube_scramble, best_cube_fitness, True]

            population = sorted(population)
            best_cube_scramble = cube.cube2str()
            best_cube_fitness = cube.fitness
            parents_candiate = choose_parent(population)
            parents = selection(parents_candiate, no_parents, selection_mode)
            # print(stage, parents, i, generation)
            new_population = generate_population(parents, no_population, no_parents)
            population = new_population


# start_stage = state_stage0
# max_per_generation = 10
# no_parents = 10
# no_population = 100
# max_generations = 2
# stages = [0, 1, 2, 3, 4]
# stages_attempt = [0, 0, 0, 0]
# selection_mode = "best"
# file_name = "xd.json"

start_stage = sys.argv[1] 
max_generations = int(sys.argv[2])
max_per_generation = int(sys.argv[3])
no_parents = int(sys.argv[4])
no_population = int(sys.argv[5])
selection_mode = sys.argv[6]
file_name = sys.argv[7]

generation = 1
data = {'generation_id':[],'max_per_generation':[],'no_parents':[],'no_population':[],'stage_attempts':[],'selection_mode':[],'start_scramble':[],'best_scramble':[], 'best_fitness':[],'is_cube_solved':[]}
df = pd.DataFrame(data)

while generation <= max_generations:
    [best_scramble, best_fitness, is_cube_solved] = run(generation)
    df = df.append({'generation_id':generation,'max_per_generation':max_per_generation,'no_parents':no_parents,'no_population':no_population,'stage_attempts':stages_attempt,'selection_mode':selection_mode,'start_scramble':start_stage,'best_scramble':best_scramble,'best_fitness':best_fitness,'is_cube_solved':is_cube_solved}, ignore_index=True)
    stages_attempt = [0, 0, 0, 0]
    print("Test nr "+str(generation)+ " zakończony")
    generation += 1
print(df)
df.to_json(file_name)