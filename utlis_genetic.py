from typing import List
from rubik.cube import Cube
from MyRubick2 import MyRubic
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


def population_ready(population: 'list[MyRubic]', no_stage):
    all_ready = True
    for p in population:
        if no_stage == 0 and p.good_state1 == False:
            all_ready = False
            break
        elif no_stage == 1 and p.good_state2 == False:
            all_ready = False
            break
        elif no_stage == 2 and p.good_state3 == False:
            all_ready = False
            break
        elif no_stage == 3 and p.good_state4 == False:
            all_ready = False
            break

    return all_ready


def generate_population(parents, no_population, no_parents):
    children = []
    no_children = no_population // no_parents

    for parent in parents:
        for i in range(no_children):
            children.append(deepcopy(parent))
    return children


def choose_parent(population: 'list[MyRubic]'):
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


# def selection_rulette(population: List[MyRubic], no_parents):
#     all_fitness = [p.fitness for p in population]
#     sum_fitness = sum(all_fitness) * 1.0

#     propability_all = [1 - (1.0 * f / sum_fitness) for f in all_fitness]
#     propability_all = [(1 - (1.0 * f / sum_fitness)) /
#                        sum(propability_all) for f in all_fitness]

#     roulette = []
#     temp = 0
#     for i, p in enumerate(propability_all):
#         if i == 0:
#             roulette.append([0, p])
#         elif i == len(propability_all)-1:
#             roulette.append([temp, 1])
#         else:
#             roulette.append([temp, temp+p])

#         temp += p
#     # print(propability_all[:3])

#     shots = [random.random() for i in range(no_parents)]
#     parents = []
#     for shot in shots:
#         for i, val_list in enumerate(roulette):
#             if val_list[0] <= shot < val_list[1]:
#                 parents.append(deepcopy(population[i]))
#                 break

#     return parents


def selection(population, no_parents, mode="tournament"):
    if mode == "tournament":
        parents = []
        for i in range(no_parents):
            indexes = np.random.randint(0, len(population), 2)
            parents.append(
                min([population[indexes[0]], population[indexes[1]]]))
            parents = sorted(parents)
        return parents

    elif mode == "best":
        return population[0: no_parents]

    elif mode == "roulette":
        all_fitness = [p.fitness for p in population]
        sum_fitness = sum(all_fitness) * 1.0

        propability_all = [1 - (1.0 * f / sum_fitness) for f in all_fitness]
        propability_all = [(1 - (1.0 * f / sum_fitness)) /
                           sum(propability_all) for f in all_fitness]

        roulette = []
        temp = 0
        for i, p in enumerate(propability_all):
            if i == 0:
                roulette.append([0, p])
            elif i == len(propability_all)-1:
                roulette.append([temp, 1])
            else:
                roulette.append([temp, temp+p])

            temp += p
        # print(propability_all[:3])

        shots = [random.random() for i in range(no_parents)]
        parents = []
        for shot in shots:
            for i, val_list in enumerate(roulette):
                if val_list[0] <= shot < val_list[1]:
                    parents.append(deepcopy(population[i]))
                    break

        return parents
