from rubik.cube import Cube
from myRubic import MyRubic
from time import sleep
from constants_tutorial import *
from utlis_genetic import *
from copy import deepcopy
import random
import numpy as np

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


def run(generation):
    population = [MyRubic(Cube(start_stage)) for i in range(no_population)]

    stages = [0, 1, 2, 3, 4]
    print("start")
    max_generation = 500
    for stage in stages:
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

            population = sorted(population)

            parents_candiate = choose_parent(population)
            parents = selection(parents_candiate,  mode="best")

            print(stage, parents, i, generation)
            new_population = generate_population(parents, no_population)
            population = new_population


generation = 0
while run(generation) == False:
    generation += 1
