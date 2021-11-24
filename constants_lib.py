
#ulozona kostka lib
solved_cube = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"


slices_stage0 = [1, 3, 5, 7, 24, 26, 30, 32, 46, 48, 50, 52]
# [0, 2, 6, 8, 45, 47, 51, 53] - ['O', 'R']
# [1, 3, 5, 7, 46, 48, 50, 52] - ['O', 'R']
# [24, 26, 30, 32] - ['W', 'B']

slices_stage1 = [[0, 2, 6, 8, 45, 47, 51, 53], [
    1, 3, 5, 7, 46, 48, 50, 52], [24, 26, 30, 32]]

slices_stage2 = [[0, 2, 6, 8, 45, 47, 51, 53], [12, 13, 14, 24, 26, 36, 37, 38, 18, 19,
                                                20, 30, 32, 42, 43, 44], [9, 10, 11, 21, 23, 33, 34, 35, 15, 16, 17, 27, 29, 39, 40, 41]]
slices_stage3 = [1, 3, 5, 7, 24, 26, 30, 32, 46, 48, 50, 52]


available_colors_stage0 = ['O', 'W', 'R', 'B']
available_colors_stage1 = [['O', 'R'], ['O', 'R'], ['W', 'B']]
available_colors_stage2 = [['O', 'R'], ['W', 'B'], ['Y', 'G']]
available_colors_stage3 = ['O', 'W', 'R', 'B']


max_moves_stage0 = 7
max_moves_stage1 = 13
max_moves_stage2 = 15
max_moves_stage3 = 17

stage0_moves = ["U", "D", "F", "B", "L", "R"]
# stage0_moves = ["F", "R", "U", "B", "L", "D"]
stage1_moves = ["U", "D", "F2", "B2", "L", "R"]
# stage1_moves = ["F", "U", "B", "D", "R2", "L2"]
stage2_moves = ["U", "D", "R2", "L2", "F2", "B2"]
stage3_moves = ["F2", "R2", "U2", "B2", "L2", "D2"]


no_population = 100
no_parents = 8
