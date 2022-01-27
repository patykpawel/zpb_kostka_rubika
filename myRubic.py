from rubik.cube import Cube

from constants_tutorial import *
import copy


class MyRubic():
    stage4_pruning_table = None
    stage3_pruning_corners = None

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

    @staticmethod
    def generate_pruning_table(solved_states, moves, depth):
        pruning_table = {}
        for state in solved_states:
            pruning_table[state] = 0
        # testowane tylko dla G3->Solved
        for d in range(0, depth):
            keys = [k for k, v in pruning_table.items() if v == d]
            for k in keys:
                for m in moves:
                    cube = MyRubic(Cube(k))
                    cube.make_move(m)
                    cube_seed = cube.cube2str()
                    if cube_seed not in pruning_table.keys():
                        pruning_table[cube_seed] = d + 1
        return pruning_table

    def calculate_fintess(self, no_stage, mode="short"):

        if mode == "bad":
            if no_stage == 0:
                self.fitness_1()
            elif no_stage == 1:
                self.fitness_2()
            elif no_stage == 2:
                self.fitness_3()
            elif no_stage == 3:
                self.fitness_4()

        elif mode == "short":
            if no_stage == 0:
                self.fitness_dist_1()
            elif no_stage == 1:
                self.fitness_dist_2()
            elif no_stage == 2:
                self.fitness_pruning_3()
            elif no_stage == 3:
                self.fitness_pruning_4()

    def center_cube(self, face, cube_str):

        orginal = copy.copy(cube_str)

        u_f, l_f, f_f, r_f, p_f, b_f = "", "", "", "", "", ""
        u_f = orginal[0:9]
        l_f = orginal[9:12] + orginal[21:24] + orginal[33:36]
        f_f = orginal[12:15] + orginal[24:27] + orginal[36:39]
        r_f = orginal[15:18] + orginal[27:30] + orginal[39:42]
        p_f = orginal[18:21] + orginal[30:33] + orginal[42:45]
        b_f = orginal[45:48] + orginal[48:51] + orginal[51:54]

        if face == "f":
            return orginal
        elif face == "u":
            orientet_cube = p_f + l_f[0:3] + u_f[0:3] + r_f[0:3] + b_f[0:3] + l_f[3:6] + \
                u_f[3:6] + r_f[3:6] + b_f[3:6] + l_f[6:9] + \
                u_f[6:9] + r_f[6:9] + b_f[6:9] + f_f
        elif face == "b":
            orientet_cube = f_f + l_f[0:3] + b_f[0:3] + r_f[0:3] + u_f[0:3] + l_f[3:6] + \
                b_f[3:6] + r_f[3:6] + u_f[3:6] + l_f[6:9] + \
                b_f[6:9] + r_f[6:9] + u_f[6:9] + p_f
        elif face == "l":
            orientet_cube = u_f + p_f[0:3] + l_f[0:3] + f_f[0:3] + r_f[0:3] + p_f[3:6] + \
                l_f[3:6] + f_f[3:6] + r_f[3:6] + p_f[6:9] + \
                l_f[6:9] + f_f[6:9] + r_f[6:9] + b_f
        elif face == "r":
            orientet_cube = u_f + f_f[0:3] + r_f[0:3] + p_f[0:3] + l_f[0:3] + f_f[3:6] + \
                r_f[3:6] + p_f[3:6] + l_f[3:6] + f_f[6:9] + \
                r_f[6:9] + p_f[6:9] + l_f[6:9] + b_f
        elif face == "p":
            orientet_cube = u_f + r_f[0:3] + p_f[0:3] + l_f[0:3] + f_f[0:3] + r_f[3:6] + \
                p_f[3:6] + l_f[3:6] + f_f[3:6] + r_f[6:9] + \
                p_f[6:9] + l_f[6:9] + f_f[6:9] + b_f

        return orientet_cube

    def map_cube(self, centerd_cube):

        orginal = list(centerd_cube)

        cube_map = np.empty((9, 12), dtype=str)

        cube_map[0:3, 0:3] = "-"
        cube_map[6:9, 0:3] = "-"
        cube_map[0:3, 6:12] = "-"
        cube_map[6:9, 6:12] = "-"

        # up
        cube_map[0, 3:6] = orginal[0:3]
        cube_map[1, 3:6] = orginal[3:6]
        cube_map[2, 3:6] = orginal[6:9]
        ## left, front, right, post
        cube_map[3, 0:12] = orginal[9: 21]
        cube_map[4, 0:12] = orginal[21: 33]
        cube_map[5, 0:12] = orginal[33: 45]

        # bottom
        cube_map[6, 3:6] = orginal[45:48]
        cube_map[7, 3:6] = orginal[48:51]
        cube_map[8, 3:6] = orginal[51:54]

        return cube_map

    def translate_index(self, idx, face):
        if face == "f":
            return idx
        elif face == "u":
            if 0 <= idx < 3:
                new_idx = idx + 12
            elif 3 <= idx < 6:
                new_idx = idx + 21
            elif 6 <= idx < 9:
                new_idx = idx + 30
        elif face == "b":
            if 45 <= idx < 48:
                new_idx = idx - 33
            elif 48 <= idx < 51:
                new_idx = idx - 24
            elif 51 <= idx < 54:
                new_idx = idx - 15
        elif face == "l":
            if 9 <= idx < 12:
                new_idx = idx + 3
            elif 21 <= idx < 24:
                new_idx = idx + 3
            elif 33 <= idx < 36:
                new_idx = idx + 3
        elif face == "r":
            if 15 <= idx < 18:
                new_idx = idx - 3
            elif 27 <= idx < 30:
                new_idx = idx - 3
            elif 39 <= idx < 42:
                new_idx = idx - 3
        elif face == "p":
            if 18 <= idx < 21:
                new_idx = idx - 6
            elif 30 <= idx < 33:
                new_idx = idx - 6
            elif 42 <= idx < 45:
                new_idx = idx - 6

        return new_idx

    def translate_index_map(self, idx):
        if idx == 12:
            return 3, 3
        elif idx == 13:
            return 3, 4
        elif idx == 14:
            return 3, 5
        elif idx == 24:
            return 4, 3
        elif idx == 25:
            return 4, 4
        elif idx == 26:
            return 4, 5
        elif idx == 36:
            return 5, 3
        elif idx == 37:
            return 5, 4
        elif idx == 38:
            return 5, 5

    def euclides(self, x, y, indices_x: np.array, indices_y: np.array):
        a = np.power(x - indices_x, 2)
        b = np.power(y - indices_y, 2)

        return np.sqrt(a + b)

    def fitness_dist_1(self):

        cube_str = self.cube2str()
        for idx, ss in enumerate(slices_stage0):
            for s in ss:
                if cube_str[s] in available_colors_stage0[idx]:
                    cube_str = cube_str[:s] + "-" + cube_str[s+1:]

        cnt = 0

        for idx, ss in enumerate(slices_stage0):
            for s in ss:
                if cube_str[s] not in available_colors_stage0[idx] and cube_str[s] != "-":
                    if 0 <= s < 9:  # up
                        oriented_cube = self.center_cube("u", cube_str)
                        central_face = "u"
                    elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36:  # left
                        oriented_cube = self.center_cube("l", cube_str)
                        central_face = "l"
                    elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39:  # front
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"
                    elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42:  # right
                        oriented_cube = self.center_cube("r", cube_str)
                        central_face = "r"
                    elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45:  # post
                        oriented_cube = self.center_cube("p", cube_str)
                        central_face = "p"
                    elif 45 <= s < 54:  # bottom
                        oriented_cube = self.center_cube("b", cube_str)
                        central_face = "b"
                    else:
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"

                    new_idx = self.translate_index(s, central_face)
                    cube_map = self.map_cube(oriented_cube)
                    ss_x, ss_y = self.translate_index_map(new_idx)
                    x_c, y_c = [], []
                    for color in available_colors_stage0[idx]:
                        x_t, y_t = np.where(cube_map == color)
                        x_c.extend(x_t)
                        y_c.extend(y_t)

                    x_c = np.array([x_c])
                    y_c = np.array([y_c])
                    dist = self.euclides(ss_x, ss_y, x_c, y_c)

                    cnt += np.min(dist)
        self.fitness = cnt
        # print(cube_map)
        if cnt == 0:
            self.good_state1 = True

    def fitness_dist_2(self):
        cube_str = self.cube2str()
        for idx, ss in enumerate(slices_stage1):
            for s in ss:
                if cube_str[s] in available_colors_stage1[idx]:
                    cube_str = cube_str[:s] + "-" + cube_str[s+1:]

        cnt = 0
        for idx, ss in enumerate(slices_stage1):
            for s in ss:
                if cube_str[s] not in available_colors_stage1[idx] and cube_str[s] != "-":
                    if 0 <= s < 9:  # up
                        oriented_cube = self.center_cube("u", cube_str)
                        central_face = "u"
                    elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36:  # left
                        oriented_cube = self.center_cube("l", cube_str)
                        central_face = "l"
                    elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39:  # front
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"
                    elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42:  # right
                        oriented_cube = self.center_cube("r", cube_str)
                        central_face = "r"
                    elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45:  # post
                        oriented_cube = self.center_cube("p", cube_str)
                        central_face = "p"
                    elif 45 <= s < 54:  # bottom
                        oriented_cube = self.center_cube("b", cube_str)
                        central_face = "b"
                    else:
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"

                    new_idx = self.translate_index(s, central_face)
                    cube_map = self.map_cube(oriented_cube)
                    ss_x, ss_y = self.translate_index_map(new_idx)
                    x_c, y_c = [], []
                    for color in available_colors_stage1[idx]:
                        x_t, y_t = np.where(cube_map == color)
                        x_c.extend(x_t)
                        y_c.extend(y_t)

                    x_c = np.array([x_c])
                    y_c = np.array([y_c])
                    dist = self.euclides(ss_x, ss_y, x_c, y_c)

                    cnt += np.min(dist)
        self.fitness = cnt
        if cnt == 0:
            self.good_state2 = True

    def fitness_dist_3(self):
        cube_str = self.cube2str()
        for idx, ss in enumerate(slices_stage2):
            for s in ss:
                if cube_str[s] in available_colors_stage2[idx]:
                    cube_str = cube_str[:s] + "-" + cube_str[s+1:]

        cnt = 0
        for idx, ss in enumerate(slices_stage2):
            for s in ss:
                if cube_str[s] not in available_colors_stage2[idx] and cube_str[s] != "-":
                    if 0 <= s < 9:  # up
                        oriented_cube = self.center_cube("u", cube_str)
                        central_face = "u"
                    elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36:  # left
                        oriented_cube = self.center_cube("l", cube_str)
                        central_face = "l"
                    elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39:  # front
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"
                    elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42:  # right
                        oriented_cube = self.center_cube("r", cube_str)
                        central_face = "r"
                    elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45:  # post
                        oriented_cube = self.center_cube("p", cube_str)
                        central_face = "p"
                    elif 45 <= s < 54:  # bottom
                        oriented_cube = self.center_cube("b", cube_str)
                        central_face = "b"
                    else:
                        oriented_cube = self.center_cube("f", cube_str)
                        central_face = "f"

                    new_idx = self.translate_index(s, central_face)
                    cube_map = self.map_cube(oriented_cube)
                    ss_x, ss_y = self.translate_index_map(new_idx)
                    x_c, y_c = [], []
                    for color in available_colors_stage2[idx]:
                        x_t, y_t = np.where(cube_map == color)
                        x_c.extend(x_t)
                        y_c.extend(y_t)

                    x_c = np.array([x_c])
                    y_c = np.array([y_c])
                    dist = self.euclides(ss_x, ss_y, x_c, y_c)

                    cnt += np.min(dist)
        self.fitness = cnt
        if cnt == 0:
            self.good_state3 = True

    def fitness_dist_4(self):
        cube_str = self.cube2str()
        cnt = 0

        for idx, ss in enumerate(slices_stage3):
            for s in ss:
                if cube_str[s] not in available_colors_stage3[idx]:
                    if 0 <= s < 9:  # up
                        oriented_cube = self.center_cube("u")
                        central_face = "u"
                    elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36:  # left
                        oriented_cube = self.center_cube("l")
                        central_face = "l"
                    elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39:  # front
                        oriented_cube = self.center_cube("f")
                        central_face = "f"
                    elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42:  # right
                        oriented_cube = self.center_cube("r")
                        central_face = "r"
                    elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45:  # post
                        oriented_cube = self.center_cube("p")
                        central_face = "p"
                    elif 45 <= s < 54:  # bottom
                        oriented_cube = self.center_cube("b")
                        central_face = "b"
                    else:
                        central_face = "f"

                    new_idx = self.translate_index(s, central_face)
                    cube_map = self.map_cube(oriented_cube)
                    ss_x, ss_y = self.translate_index_map(new_idx)
                    x_c, y_c = [], []
                    for color in available_colors_stage3[idx]:
                        x_t, y_t = np.where(cube_map == color)
                        x_c.extend(x_t)
                        y_c.extend(y_t)

                    x_c = np.array([x_c])
                    y_c = np.array([y_c])
                    dist = self.euclides(ss_x, ss_y, x_c, y_c)

                    cnt += np.min(dist)
        self.fitness = cnt
        if cnt == 0:
            self.good_state4 = True

    def fitness_1(self):
        cube_str = self.cube2str()
        cnt = 0
        for idx, ss in enumerate(slices_stage0):
            for s in ss:
                if cube_str[s] not in available_colors_stage0[idx]:
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
        for idx, ss in enumerate(slices_stage1):
            for s in ss:
                if cube_str[s] not in available_colors_stage1[idx]:
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
            cond1 = cube_str[slices_stage2[0][s]
                             ] not in available_colors_stage2[0]
            cond2 = cube_str[slices_stage2[1][s]
                             ] not in available_colors_stage2[1]
            cond3 = cube_str[slices_stage2[2][s]
                             ] not in available_colors_stage2[2]
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
        cnt = sum(1 for x, y in zip(self.cube2str(), solved_cube) if x != y)

        if cnt == 0:
            self.good_state4 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * 2 * cnt
        self.fitness = J

    def fitness_pruning_3(self):
        cube_str = self.cube2str()
        x = 0
        for s in range(len(slices_stage2[0])):
            cond1 = cube_str[slices_stage2[0][s]
                             ] not in available_colors_stage2[0]
            cond2 = cube_str[slices_stage2[1][s]
                             ] not in available_colors_stage2[1]
            cond3 = cube_str[slices_stage2[2][s]
                             ] not in available_colors_stage2[2]
            if cond1 or cond2 or cond3:
                x += 1
        y = 0
        for s in range(len(slices_stage2[3])):
            if cube_str[slices_stage2[3][s]] not in available_colors_stage2[3]:
                y += 1
        for s in range(len(slices_stage2[4])):
            if cube_str[slices_stage2[4][s]] not in available_colors_stage2[4]:
                y += 1

        for key in MyRubic.stage3_pruning_corners.keys():
            corner_flag = True
            for c, p in zip(cube_str, key):
                if p == 'X':
                    continue
                if c != p:
                    corner_flag = False
                    break
            if corner_flag:
                break
        penalty = (not corner_flag) * 100  # nie pasuje do zadnej maski

        if x == 0 and y == 0 and corner_flag:
            self.good_state3 = True

        num_of_moves = len(self.moves)
        # J = 5 * 2 * cnt + num_of_moves
        J = 5 * (x + 2 * y) + penalty
        self.fitness = J

    def fitness_pruning_4(self):
        if self.cube2str() in MyRubic.stage4_pruning_table.keys():
            self.fitness = MyRubic.stage4_pruning_table[self.cube2str()]
        else:
            self.fitness = 200
            # self.fitness_4()
        if self.fitness == 0:
            self.good_state4 = True

    def cube2str(self):
        return str(self.cube).replace(" ", "").replace("\n", "")

    def make_move(self,  move):
        if (move == 'L'):
            self.cube.L()
        elif (move == 'U'):
            self.cube.U()
        elif (move == 'B'):
            self.cube.B()
        elif (move == 'F'):
            self.cube.F()
        elif (move == 'D'):
            self.cube.D()
        elif (move == 'R'):
            self.cube.R()
        elif (move == 'L2'):
            self.cube.L()
            self.cube.L()
        elif (move == 'D2'):
            self.cube.D()
            self.cube.D()
        elif (move == 'B2'):
            self.cube.B()
            self.cube.B()
        elif (move == 'R2'):
            self.cube.R()
            self.cube.R()
        elif (move == 'U2'):
            self.cube.U()
            self.cube.U()
        elif (move == 'F2'):
            self.cube.F()
            self.cube.F()

    def make_moves(self, moves, stage):
        done_moves = []
        for m in moves:
            self.make_move(m)
            done_moves.append(m)
            self.calculate_fintess(stage)
            if self.fitness == 0:
                return done_moves

        return done_moves

    def __str__(self):
        return str(self.fitness)

    def __repr__(self):
        return str(self.fitness)
