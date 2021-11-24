from rubik.cube import Cube

from constants import *

class MyRubic():


    def __init__(self, cube: Cube):
        self.cube = cube
        self.moves = []
        self.good_state1 = False
        self.good_state2 = False
        self.fitness = None
    
    def __lt__(self, other):
         return self.fitness < other.fitness

    def fitness_1(self):
        cube_str = self.cube2str()
        cnt = 0
        for i in slices_stage0:
            if cube_str[i] not in available_colors_stage0:
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
        pass
    

    def fitness_4(self):
        pass
    

    
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
            if stage == 0:
                self.fitness_1()
            elif stage == 1:
                self.fitness_2()

            if self.fitness == 0:
                return done_moves
        
        return done_moves


    def __str__(self):
        return str(self.fitness)

    def __repr__(self):
        return str(self.fitness)