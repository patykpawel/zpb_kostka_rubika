from myRubic import MyRubic
from rubik.cube import Cube

#przykład 
#https://alg.cubing.net/?alg=D-_B_U_D2_F_%2F%2F_phase_1%0AD-_R-_D-_L-_U2_D-_L_%2F%2F_phase_2%0AU_F2_B2_L2_F2_U_L2_D_%2F%2F_phase_3%0AL2_R2_F2_L2_U2_L2_U2_B2_D2_B2_R2_%2F%2F_phase_4&setup=L2_U_R-_B_U-_D-_L-_U-_L-_U2_L2_D2_R2_D-_L-_U_B2_U_D_L_F2_U-_L2_R2_F-_D_B2_D-_R2_D-

#rozwiazanie
# L2 U R' B U' D' L' U' L' U2 L2 D2 R2 D' L' U B2 U D L F2 U' L2 R2 F' D B2 D' R2 D'



start_state = "WOGWWORYWGOYBRRBGYRYOGOWBGBYRBOBWOBYBGRGROBRYOYWRYGGWW"

p = MyRubic(Cube(start_state))
print("g_0")
print(p.cube)
print("g_1")
moves1 = ["D","D","D", "B","U", "D", "D", "F"]
p.make_moves(moves1, 0)
p.fitness_1()
print(p.cube)
print(p.fitness)
print("g_2")
moves2 = ["D", "D", "D", "R", "R", "R", "D", "D", "D", "L", "L", "L", "U", "U", "D", "D", "D", "L"]
p.make_moves(moves2, 1)
p.fitness_2()
print(p.cube)
print(p.fitness)