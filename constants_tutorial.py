# wartości z tutoriala
# link https://observablehq.com/@onionhoney/how-to-model-a-rubiks-cube


# tutorial g_0 obrazek
state_stage0 = 'YRGGWRBYOGOWRBWBWRWGRROWOGYORYRBBGWBOBYOYBYWWYOGGYGOBR'


# tutorial g_2 obrazek
state_stage2 = "YYWYWYWWWOBGRGOGRRBGGRORGGBOROGBBORGRORBBOBOBYYYWYWYWW"


# tutorial ulozona kostka g_solved
solved_cube = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'

slices_stage0 = [[1, 3, 5, 7, 46, 48, 50, 52], [24, 26, 30, 32]]
# [0, 2, 6, 8, 45, 47, 51, 53] - ['O', 'R']
# [1, 3, 5, 7, 46, 48, 50, 52] - ['O', 'R']
# [24, 26, 30, 32] - ['W', 'B']

slices_stage1 = [[0, 2, 6, 8, 45, 47, 51, 53], [
    1, 3, 5, 7, 46, 48, 50, 52], [24, 26, 30, 32]]

slices_stage2 = [[0, 2, 6, 8, 45, 47, 51, 53], [9, 11, 33, 35, 15, 17, 39, 41], [
    12, 14, 36, 38, 18, 20, 42, 44], [10, 34, 16, 40], [13, 37, 19, 43]]
# slices_stage2 = [[0, 2, 6, 8, 45, 47, 51, 53], [12, 13, 14, 24, 26, 36, 37, 38, 18, 19,
# 20, 30, 32, 42, 43, 44], [9, 10, 11, 21, 23, 33, 34, 35, 15, 16, 17, 27, 29, 39, 40, 41]]
slices_stage3 = [[0, 1, 2, 3, 5, 6, 7, 8], [9, 10, 11, 21, 23, 33, 34, 35], [12, 13, 14, 24, 26, 36, 37, 38], [45, 46, 47, 48, 50, 51, 52, 53], [15, 16, 17, 27, 29, 39, 40, 41], [18, 19, 20, 30, 32, 42, 43, 44]]

available_colors_stage0 = [['W', 'Y'], ['G', 'B']]
# available_colors_stage1 = [['O'], ['R'], ['W', 'B']]
available_colors_stage1 = [['W', 'Y'], ['W', 'Y'], ['G', 'B']]
available_colors_stage2 = [["W", "Y"], [
    "O", "R"], ["G", "B"], ["O", "R"], ["G", "B"]]
# available_colors_stage2 = [['O', 'R'], ['W', 'B'], ['Y', 'G']]
available_colors_stage3 = [["w"], ["O"], ["G"], ["Y"], ["R"], ["B"]]


max_moves_stage0 = 7
max_moves_stage1 = 12
max_moves_stage2 = 15
max_moves_stage3 = 17

# stage0_moves = ["F", "R", "U", "B", "L", "D"]
stage0_moves = ["U", "D", "F", "B", "L", "R"]
stage1_moves = ["U", "D", "F2", "B2", "L", "R"]

stage2_moves = ["U", "D", "R2", "L2", "F2", "B2"]
stage3_moves = ["F2", "R2", "U2", "B2", "L2", "D2"]

all_moves = list(set(stage0_moves + stage1_moves +
                 stage2_moves + stage3_moves))


no_population = 100
no_parents = 10
