from rubik.cube import Cube
from myRubic import MyRubic
from constants_tutorial import *
import random
from utlis_genetic import *




start_state = "WOGWWORYWGOYBRRBGYRYOGOWBGBYRBOBWOBYBGRGROBRYOYWRYGGWW"

population = [MyRubic(Cube(start_state)) for i in range(no_population)]



selection_mode = "best"

stages = [0, 1, 2]
print("start")
max_generation = 1000
for stage in stages:
    
    min_fitness = 100
    i = 0
    while not population_ready(population, stage):
        
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

                else:
                    print("ułozona")
                pass

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
        parents = selection(parents_candiate, mode=selection_mode)
        
        parents = sorted(parents)
        
        print(stage, parents)
        # print(parents[0].cube2str())

        # print("RUCHY ", len(parents[0].moves))
        new_population = generate_population(parents, no_population)

        population = new_population