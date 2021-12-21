from rubik.cube import Cube
import numpy as np
from constants_tutorial import *


class MyRubic:
    def __init__(self, cube: Cube):
        self.cube = cube
        self.moves = []
        self.good_state1 = False
        self.good_state2 = False
        self.good_state3 = False
        self.good_state4 = False
        self.fitness = None

    def __lt__(self, other):
        return self.fitness < other.fitness

    def fitness_1(self):
        cube_str = self.cube2str()
        cnt = 0
        # for idx, ss in enumerate(slices_stage0):
        # for s in ss:
        # if cube_str[s] not in available_colors_stage0[idx]:
        # cnt += 1

        for idx in range(len(slices_stage00)):
            if cube_str[slices_stage00[idx]] not in available_colors_stage00:
                cnt += 1

        for idx in range(len(slices_stage01)):
            if cube_str[slices_stage01[idx]] not in available_colors_stage01:
                cnt += 1

        if cnt == 0:
            self.good_state1 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * 2 * cnt
        self.fitness = J

    def fitness_2(self):
        cube_str = self.cube2str()
        cnt = 0

        for idx in range(len(slices_stage10)):
            if cube_str[slices_stage10[idx]] not in available_colors_stage10:
                cnt += 1

        for idx in range(len(slices_stage11)):
            if cube_str[slices_stage11[idx]] not in available_colors_stage11:
                cnt += 1

        for idx in range(len(slices_stage12)):
            if cube_str[slices_stage12[idx]] not in available_colors_stage12:
                cnt += 1

        if cnt == 0:
            self.good_state2 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * 2 * cnt

        self.fitness = J

    def fitness_3(self):
        cube_str = self.cube2str()
        x = 0
        for s in range(len(slices_stage2[0])):
            cond1 = cube_str[slices_stage2[0][s]] not in available_colors_stage2[0]
            cond2 = cube_str[slices_stage2[1][s]] not in available_colors_stage2[1]
            cond3 = cube_str[slices_stage2[2][s]] not in available_colors_stage2[2]
            if cond1 or cond2 or cond3:
                x += 1
        y = 0
        for s in range(len(slices_stage2[3])):
            if cube_str[slices_stage2[3][s]] not in available_colors_stage2[3]:
                y += 1
        for s in range(len(slices_stage2[4])):
            if cube_str[slices_stage2[4][s]] not in available_colors_stage2[4]:
                y += 1
        if x == 0 and y == 0:
            self.good_state3 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * (x + 2 * y)

        self.fitness = J

    def fitness_4(self):
        cube_str = self.cube2str()
        cnt = 0
        for s in range(len(slices_stage3[0])):
            if cube_str[slices_stage3[0][s]] not in available_colors_stage3[0]:
                cnt += 1
            if cube_str[slices_stage3[1][s]] not in available_colors_stage3[1]:
                cnt += 1
            if cube_str[slices_stage3[2][s]] not in available_colors_stage3[2]:
                cnt += 1
            # if cube_str[slices_stage3[3][s]] not in available_colors_stage3[3]:
            #     cnt += 1
            # if cube_str[slices_stage3[4][s]] not in available_colors_stage3[4]:
            #     cnt += 1
            # if cube_str[slices_stage3[5][s]] not in available_colors_stage3[5]:
            #     cnt += 1

        if cnt == 0:
            self.good_state4 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * 2 * cnt
        self.fitness = J

    def cube2str(self):
        return str(self.cube).replace(" ", "").replace("\n", "")

    def make_move(self, move):
        if move == "L":
            self.cube.L()
        elif move == "U":
            self.cube.U()
        elif move == "B":
            self.cube.B()
        elif move == "F":
            self.cube.F()
        elif move == "D":
            self.cube.D()
        elif move == "R":
            self.cube.R()
        elif move == "L2":
            self.cube.L()
            self.cube.L()
        elif move == "D2":
            self.cube.D()
            self.cube.D()
        elif move == "B2":
            self.cube.B()
            self.cube.B()
        elif move == "R2":
            self.cube.R()
            self.cube.R()
        elif move == "U2":
            self.cube.U()
            self.cube.U()
        elif move == "F2":
            self.cube.F()
            self.cube.F()

    def make_moves(self, moves, stage):
        done_moves = []
        for m in moves:
            self.make_move(m)
            done_moves.append(m)
            if stage == 0:
                self.fitness_1()
            elif stage == 1:
                self.fitness_2()
            elif stage == 2:
                self.fitness_3()
            elif stage == 3:
                self.fitness_4()

            if self.fitness == 0:
                return done_moves

        return done_moves

    def __str__(self):
        return str(self.fitness)

    def __repr__(self):
        return str(self.fitness)


def flatten(nasted_list):
    """
    input: nasted_list - this contain any number of nested lists.
    ------------------------
    output: list_of_lists - one list contain all the items.
    """

    list_of_lists = []
    for item in nasted_list:
        list_of_lists.extend(item)
    return list_of_lists
