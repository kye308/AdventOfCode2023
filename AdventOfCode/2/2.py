import os

def get_power(draws_str):
    color_idxs = [1, 3, 5]
    power = 1
    min_cubes = {}
    # split on ";" to get each draw, split each draw on space to get the number of each type of cube
    # for each draw update the value in min_cubes if the number drawn is higher
    draws = draws_str.split(";")
    for draw in draws:
        draw_lst = draw.strip().split(" ")
        assert len(draw_lst) % 2 == 0 # assert length is even

        i = 0
        while i < len(draw_lst) / 2: # assumes draw_lst is in the form [X color_1 {maybe Y color_2 Z color_3} ]
            num_color = int(draw_lst[color_idxs[i] - 1])
            color = draw_lst[color_idxs[i]]
            color = color[0:-1] if color[-1] == "," else color # remove trailing comma

            if color not in min_cubes or num_color > min_cubes[color]:
                min_cubes[color] = num_color

            i += 1

    for color in min_cubes:
        power *= min_cubes[color]
    
    return power

if __name__ == "__main__":
    # read input
    # f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input_small_1")
    f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input")
    sum = 0

    for line in f.readlines():
        id_end_idx = line.find(":")
        game_id = line[len("Game "):id_end_idx]
        draws = line[id_end_idx+1:]

        sum += get_power(draws.strip())

    print("Sum:", sum)