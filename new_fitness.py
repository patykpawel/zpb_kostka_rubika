
from rubik.cube import Cube
from myRubic import MyRubic
from constants_tutorial import *
import random
from utlis_genetic import *


start_state = "WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY"





def center_cube(cube: MyRubic, face):
   
    orginal = cube.cube2str()

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
        orientet_cube = p_f + l_f[0:3] + u_f[0:3] + r_f[0:3] + b_f[0:3] + l_f[3:6] + u_f[3:6] + r_f[3:6] + b_f[3:6] + l_f[6:9] + u_f[6:9] + r_f[6:9] + b_f[6:9] + f_f
    elif  face == "b":
        orientet_cube = f_f + l_f[0:3] + b_f[0:3] + r_f[0:3] + u_f[0:3] + l_f[3:6] + b_f[3:6] + r_f[3:6] + u_f[3:6] + l_f[6:9] + b_f[6:9] + r_f[6:9] + u_f[6:9] + p_f
    elif  face == "l":
        orientet_cube = u_f + p_f[0:3] + l_f[0:3] + f_f[0:3] + r_f[0:3] + p_f[3:6] + l_f[3:6] + f_f[3:6] + r_f[3:6] + p_f[6:9] + l_f[6:9] + f_f[6:9] + r_f[6:9] + b_f
    elif  face == "r":
        orientet_cube = u_f + f_f[0:3] + r_f[0:3] + p_f[0:3] + l_f[0:3] + f_f[3:6] + r_f[3:6] + p_f[3:6] + l_f[3:6] + f_f[6:9] + r_f[6:9] + p_f[6:9] + l_f[6:9] + b_f        
    elif  face == "p":
        orientet_cube = u_f + r_f[0:3] + p_f[0:3] + l_f[0:3] + f_f[0:3] + r_f[3:6] + p_f[3:6] + l_f[3:6] + f_f[3:6] + r_f[6:9] + p_f[6:9] + l_f[6:9] + f_f[6:9] + b_f
        
    
    return orientet_cube



def map_cube(centerd_cube):

    orginal = list(centerd_cube)
    
    cube_map = np.empty((9, 12), dtype=str)
    
    
    cube_map[0:3, 0:3] = "-"
    cube_map[6:9, 0:3] = "-"
    cube_map[0:3, 6:12] = "-"
    cube_map[6:9, 6:12] = "-"
    
    ## up
    cube_map[0, 3:6] = orginal[0:3] 
    cube_map[1, 3:6] = orginal[3:6]
    cube_map[2, 3:6] = orginal[6:9]
    ## left, front, right, post
    cube_map[3, 0:12] = orginal[9 : 21]
    cube_map[4, 0:12] = orginal[21 : 33]
    cube_map[5, 0:12] = orginal[33 : 45]
    
    ## bottom
    cube_map[6, 3:6] = orginal[45:48] 
    cube_map[7, 3:6] = orginal[48:51]
    cube_map[8, 3:6] = orginal[51:54]


    return cube_map


def translate_index(idx, face):
    if face == "f":
        return idx
    elif face == "u":
        if 0 <= idx < 3:
            new_idx = idx + 12
        elif 3 <= idx < 6:
            new_idx = idx + 21
        elif 6 <= idx < 9:
            new_idx = idx + 30
    elif  face == "b":
        if 45 <= idx < 48:
            new_idx = idx - 33
        elif 48 <= idx < 51:
            new_idx = idx - 24
        elif 51 <= idx < 54:
            new_idx = idx - 15
    elif  face == "l":
        if 9 <= idx < 12:
            new_idx = idx + 3
        elif 21 <= idx < 24:
            new_idx = idx + 3
        elif 33 <= idx < 36:
            new_idx = idx + 3
    elif  face == "r":
        if 15 <= idx < 18:
            new_idx = idx - 3
        elif 27 <= idx < 30:
            new_idx = idx - 3
        elif 39 <= idx < 42:
            new_idx = idx - 3
    elif  face == "p":
        if 18 <= idx < 21:
            new_idx = idx - 6
        elif 30 <= idx < 33:
            new_idx = idx - 6
        elif 42 <= idx < 45:
            new_idx = idx - 6
    
    
    return new_idx
        

def translate_index_map(idx):
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

    
def euclides(x, y, indices_x:np.array, indices_y:np.array):
    a = np.power(x - indices_x, 2)
    b = np.power(y - indices_y, 2)

    return np.sqrt(a + b)

def fitness_dist_1(cube: MyRubic):
    
    cube_str = cube.cube2str()
    cnt = 0
    for idx, ss in enumerate(slices_stage0):
        for s in ss:            
            if cube_str[s] not in available_colors_stage0[idx]:
                if 0 <= s < 9: # up
                    oriented_cube = center_cube(cube, "u")
                    central_face = "u"
                elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36: #left
                    oriented_cube = center_cube(cube, "l")
                    central_face = "l"
                elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39: #front
                    oriented_cube = center_cube(cube, "f")
                    central_face = "f"
                elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42: #right
                    oriented_cube = center_cube(cube, "r")
                    central_face = "r"
                elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45: #post
                    oriented_cube = center_cube(cube, "p")
                    central_face = "p"
                elif 45 <= s < 54: #bottom
                    oriented_cube = center_cube(cube, "b")
                    central_face = "b"
                else:
                    central_face = "f"
                
                new_idx = translate_index(s, central_face)
                cube_map = map_cube(oriented_cube)
                ss_x, ss_y = translate_index_map(new_idx)
                x_c, y_c = [], []
                for color in available_colors_stage0[idx]:
                    x_t, y_t = np.where(cube_map == color)
                    x_c.extend(x_t)
                    y_c.extend(y_t)

                x_c = np.array([x_c])
                y_c = np.array([y_c])
                dist = euclides(ss_x, ss_y, x_c, y_c)

                cnt += np.min(dist) + 1
    


def fitness_dist_2(cube: MyRubic):
    cube_str = cube.cube2str()
    cnt = 0
    for idx, ss in enumerate(slices_stage1):
        for s in ss:            
            if cube_str[s] not in available_colors_stage1[idx]:
                if 0 <= s < 9: # up
                    oriented_cube = center_cube(cube, "u")
                    central_face = "u"
                elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36: #left
                    oriented_cube = center_cube(cube, "l")
                    central_face = "l"
                elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39: #front
                    oriented_cube = center_cube(cube, "f")
                    central_face = "f"
                elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42: #right
                    oriented_cube = center_cube(cube, "r")
                    central_face = "r"
                elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45: #post
                    oriented_cube = center_cube(cube, "p")
                    central_face = "p"
                elif 45 <= s < 54: #bottom
                    oriented_cube = center_cube(cube, "b")
                    central_face = "b"
                else:
                    central_face = "f"
                
                new_idx = translate_index(s, central_face)
                cube_map = map_cube(oriented_cube)
                ss_x, ss_y = translate_index_map(new_idx)
                x_c, y_c = [], []
                for color in available_colors_stage1[idx]:
                    x_t, y_t = np.where(cube_map == color)
                    x_c.extend(x_t)
                    y_c.extend(y_t)

                x_c = np.array([x_c])
                y_c = np.array([y_c])
                dist = euclides(ss_x, ss_y, x_c, y_c)

                cnt += np.min(dist) + 1
    

   

def fitness_dist_3(cube: MyRubic):
    cube_str = cube.cube2str()
    cnt = 0
    for idx, ss in enumerate(slices_stage2):
        for s in ss:            
            if cube_str[s] not in available_colors_stage2[idx]:
                if 0 <= s < 9: # up
                    oriented_cube = center_cube(cube, "u")
                    central_face = "u"
                elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36: #left
                    oriented_cube = center_cube(cube, "l")
                    central_face = "l"
                elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39: #front
                    oriented_cube = center_cube(cube, "f")
                    central_face = "f"
                elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42: #right
                    oriented_cube = center_cube(cube, "r")
                    central_face = "r"
                elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45: #post
                    oriented_cube = center_cube(cube, "p")
                    central_face = "p"
                elif 45 <= s < 54: #bottom
                    oriented_cube = center_cube(cube, "b")
                    central_face = "b"
                else:
                    central_face = "f"
                
                
                new_idx = translate_index(s, central_face)
                cube_map = map_cube(oriented_cube)
                ss_x, ss_y = translate_index_map(new_idx)
                x_c, y_c = [], []
                for color in available_colors_stage2[idx]:
                    x_t, y_t = np.where(cube_map == color)
                    x_c.extend(x_t)
                    y_c.extend(y_t)

                x_c = np.array([x_c])
                y_c = np.array([y_c])
                dist = euclides(ss_x, ss_y, x_c, y_c)

                cnt += np.min(dist) + 1
    

def fitness_dist_4(cube: MyRubic):
    cube_str = cube.cube2str()
    cnt = 0
    for idx, ss in enumerate(slices_stage3):
        for s in ss:            
            if cube_str[s] not in available_colors_stage3[idx]:
                if 0 <= s < 9: # up
                    oriented_cube = center_cube(cube, "u")
                    central_face = "u"
                elif 9 <= s < 12 or 21 <= s < 24 or 33 <= s < 36: #left
                    oriented_cube = center_cube(cube, "l")
                    central_face = "l"
                elif 12 <= s < 15 or 24 <= s < 27 or 36 <= s < 39: #front
                    oriented_cube = center_cube(cube, "f")
                    central_face = "f"
                elif 15 <= s < 18 or 27 <= s < 30 or 39 <= s < 42: #right
                    oriented_cube = center_cube(cube, "r")
                    central_face = "r"
                elif 18 <= s < 21 or 30 <= s < 33 or 42 <= s < 45: #post
                    oriented_cube = center_cube(cube, "p")
                    central_face = "p"
                elif 45 <= s < 54: #bottom
                    oriented_cube = center_cube(cube, "b")
                    central_face = "b"
                else:
                    central_face = "f"
                
                
                new_idx = translate_index(s, central_face)
                cube_map = map_cube(oriented_cube)
                ss_x, ss_y = translate_index_map(new_idx)
                x_c, y_c = [], []
                for color in available_colors_stage3[idx]:
                    x_t, y_t = np.where(cube_map == color)
                    x_c.extend(x_t)
                    y_c.extend(y_t)

                x_c = np.array([x_c])
                y_c = np.array([y_c])
                dist = euclides(ss_x, ss_y, x_c, y_c)

                cnt += np.min(dist) + 1 
    



m = MyRubic(Cube(state_stage0))
xd = map_cube(m.cube2str())
m.fitness_1()
print(m.fitness)
fitness_dist_1(m)
fitness_dist_2(m)
fitness_dist_3(m)
fitness_dist_4(m)





# print(m.cube)
# print()
# xd = Cube(print_orient_cube(m , "l"))
# # print(xd)



# m = MyRubic(Cube(start_state))
# # print(m.cube)
# # print()
# xd = Cube(print_orient_cube(m , "l"))
# # print(xd)






