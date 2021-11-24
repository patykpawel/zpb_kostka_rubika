from rubik.cube import Cube
from myRubic import MyRubic
from time import sleep
from constants_tutorial import *
from copy import deepcopy
import random
import numpy as np


def genrate_moves(moves, number):
    end_moves = []
    for i in range(number):
        idx = random.randint(0, len(moves) - 1)
        end_moves.append(moves[idx])
    
    
    
    # new_moves = []
    # for m in moves:
    #     if end_moves.count(m) % 4 == 0:
    #         new_moves = [i for i in end_moves if i != m]

    #     end_moves = new_moves
    return end_moves


# def selection(population):
#     parents = []
#     for i in range(no_parents):
#         indexes = np.random.randint(0, len(population), 2)
#         parents.append(min([population[indexes[0]], population[indexes[1]]]))
#     return parents


def population_ready(population: list[MyRubic], no_stage):
    all_ready = True
    for p in population:
        if no_stage == 0 and p.good_state1 == False:
            all_ready = False
            break
        elif no_stage == 1 and p.good_state2 == False:
            all_ready = False
            break

    return all_ready


def generate_population(parents, no_population):
    children = []
    no_children = no_population // no_parents

    for parent in parents:
        for i in range(no_children):
            children.append(deepcopy(parent))
    return children

def choose_parent(population:list[MyRubic]):
    state_list = []
    parents = []
    for p in population:
        if p.fitness == 0:
            parents.append(deepcopy(p))
            continue

        if p.cube2str not in state_list:
            parents.append(deepcopy(p))
            state_list.append(p.cube2str)

    return parents

def selection(population):
    parents = []
    for i in range(no_parents):
        indexes = np.random.randint(0, len(population), 2)
        parents.append(min([population[indexes[0]], population[indexes[1]]]))
    return parents


state_stage0 = 'YRGGWRBYOGOWRBWBWRWGRROWOGYORYRBBGWBOBYOYBYWWYOGGYGOBR'
print(len(state_stage0))
# state_stage2 = "YYWYWYWWWOBGRGOGRRBGGRORGGBOROGBBORGRORBBOBOBYYYWYWYWW"
start_state = "WWGBOWWORYYRGGWYGRBROYYYOWBRGGBBWROOYOOBRWORYBWGBRGBYG"
print(len(start_state))
# start_state = "YYWYWYWWWOBGRGOGRRBGGRORGGBOROGBBORGRORBBOBOBYYYWYWYWW"
# start_state = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
# xd = MyRubic(Cube(state_stage2))
# xd.fitness_2()

# print(xd.fitness)

def run():
    population = [MyRubic(Cube(state_stage0)) for i in range(no_population)]


    stages = [0, 1, 2]
    print("start")
    max_generation = 1000
    for stage in stages:
        
        min_fitness = 100
        i = 0
        while not population_ready(population, stage):
            if i >= max_generation:
                return False
            i = i + 1
            new_population = []
            fitness_population = []
            
            for cube in population:
                if stage == 0:
                    if cube.good_state1 == False:
                        no_moves = random.randint(1, max_moves_stage0)
                        moves = genrate_moves(stage0_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves

                        # cube.fitness_1()

                elif stage == 1:
                    if cube.good_state2 == False:
                        no_moves = random.randint(1, max_moves_stage1)

                        moves = genrate_moves(stage1_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves.append(moves)
                        
                        

                    else:
                        print("ułozona")

                elif stage == 2:
                    pass
                    # no_moves = random.randint(1, max_moves_stage2)
                    # moves = genrate_moves(stage2_moves, no_moves)
                    # cube.moves.append(moves)
                    # make_moves(cube.cube, moves)
                    # f = fitness_3(cube)
                    # fitness_population.append(f)
                elif stage == 3:
                    pass

                    # no_moves = random.randint(1, max_moves_stage3)
                    # moves = genrate_moves(stage3_moves, no_moves)
                    # cube.moves.append(moves)
                    # make_moves(cube.cube, moves)
                    # f = fitness_4(cube)
                    # fitness_population.append(f)
                elif stage == 4:
                    pass

            # min_fitness = min(fitness_population)
            # print("FIT ", min_fitness)
            population = sorted(population)
            
            parents_candiate = choose_parent(population)
            # parents = parents_candiate[0:no_parents]
            parents = selection(parents_candiate)
            
            print(stage, parents)
            print(parents[0].cube2str())

            # print("RUCHY ", len(parents[0].moves))
            new_population = generate_population(parents, no_population)

            population = new_population

while run() == False:
    pass


# population = [MyRubic(Cube(start_state)) for i in range(no_population)]


# stages = [0, 1, 2]
# print("start")
# max_generation = 1000
# for stage in stages:
#     print(stage)
#     min_fitness = 100
#     i = 0
#     while not population_ready(population, stage):

#         i = i + 1
#         new_population = []
#         fitness_population = []
        
#         for cube in population:
#             if stage == 0:
#                 if cube.good_state1 == False:
#                     no_moves = random.randint(1, max_moves_stage0)
#                     moves = genrate_moves(stage0_moves, no_moves)
#                     cube.moves += moves
#                     cube.make_moves(moves)

#                     cube.fitness_1()

#             elif stage == 1:
#                 if cube.good_state2 == False:
#                     no_moves = random.randint(1, max_moves_stage1)

#                     moves = genrate_moves(stage1_moves, no_moves)
#                     cube.moves.append(moves)
#                     cube.make_moves(moves)
#                     cube.fitness_2()

#                 else:
#                     print("ułozona")

#             elif stage == 2:
#                 pass
#                 # no_moves = random.randint(1, max_moves_stage2)
#                 # moves = genrate_moves(stage2_moves, no_moves)
#                 # cube.moves.append(moves)
#                 # make_moves(cube.cube, moves)
#                 # f = fitness_3(cube)
#                 # fitness_population.append(f)
#             elif stage == 3:
#                 pass

#                 # no_moves = random.randint(1, max_moves_stage3)
#                 # moves = genrate_moves(stage3_moves, no_moves)
#                 # cube.moves.append(moves)
#                 # make_moves(cube.cube, moves)
#                 # f = fitness_4(cube)
#                 # fitness_population.append(f)
#             elif stage == 4:
#                 pass

#         # min_fitness = min(fitness_population)
#         # print("FIT ", min_fitness)
#         population = sorted(population)
        
#         parents_candiate = choose_parent(population)
#         parents = parents_candiate[0:no_parents]
#         print(parents)

#         # print("RUCHY ", len(parents[0].moves))
#         new_population = generate_population(parents, no_population)

#         population = new_population
