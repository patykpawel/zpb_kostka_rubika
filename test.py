from rubik.cube import Cube
# from MyRubic2 import MyRubic
from MyRubick2 import MyRubic
from constants_tutorial import *
import random
from utlis_genetic import *


start_state = "WOGWWORYWGOYBRRBGYRYOGOWBGBYRBOBWOBYBGRGROBRYOYWRYGGWW"
start_state = state_stage2


selection_mode = "best"

stages = [0,1,2, 3]
print("start")
max_generation = 500

no_population = 100

def run(gen):
    population = [MyRubic(Cube(start_state)) for i in range(no_population)]
    for stage in stages:
        generation = 0
        min_fitness = 100
        i = 0
        while not population_ready(population, stage):
            if generation >= max_generation:
                return False
            generation += 1
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

                elif stage == 1:
                    if cube.good_state2 == False:
                        no_moves = random.randint(1, max_moves_stage1)

                        moves = genrate_moves(stage1_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves

                elif stage == 2:
                    if cube.good_state3 == False:
                        no_moves = random.randint(1, max_moves_stage2)

                        moves = genrate_moves(stage2_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves

                elif stage == 3:
                    if cube.good_state4 == False:
                        no_moves = random.randint(1, max_moves_stage3)

                        moves = genrate_moves(stage3_moves, no_moves)
                        moves = cube.make_moves(moves, stage)
                        cube.moves += moves
                elif stage == 4:
                    print(cube.cube)
                    print(cube.fitness)
                    print("Koniec")
                    return True

            # min_fitness = min(fitness_population)
            # print("FIT ", min_fitness)
            population = sorted(population)

            parents_candiate = choose_parent(population)
            # parents = parents_candiate[0:no_parents]
            parents = selection(parents_candiate, 8, mode=selection_mode)

            parents = sorted(parents)

            # print(gen, generation, stage, parents)
            # print(parents[0].cube2str())

            # print("RUCHY ", len(parents[0].moves))
            new_population = generate_population(parents, no_population, 8)

            population = new_population


gen = 0
while not run(gen):
    gen += 1
