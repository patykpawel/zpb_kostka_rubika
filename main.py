from rubik.cube import Cube
from myRubic import MyRubic
from time import sleep
from constants_tutorial import *
from utlis_genetic import *
from copy import deepcopy
import random
import numpy as np



start_stage = state_stage0

def run(generation):
    population = [MyRubic(Cube(start_stage)) for i in range(no_population)]


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
            
            
            for cube in population:
                if stage == 0:
                    if cube.good_state1 == False:
                        no_moves = random.randint(1, max_moves_stage0)
                        moves = genrate_moves(stage0_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves


                elif stage == 1:
                    if cube.good_state2 == False:
                        no_moves = random.randint(1, max_moves_stage1)
                        moves = genrate_moves(stage1_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                    else:
                        print("ułozona")

                elif stage == 2:
                    pass

                elif stage == 3:
                    pass

                elif stage == 4:
                    pass


            population = sorted(population)
            
            parents_candiate = choose_parent(population)
            parents = selection(parents_candiate,  mode="best")
            
            print(stage, parents, i, generation)
            new_population = generate_population(parents, no_population)
            population = new_population

generation = 0
while run(generation) == False:
    pass

