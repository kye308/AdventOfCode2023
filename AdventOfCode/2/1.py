import os

def game_possible(draws_str, cube_d):
    color_idxs = [1, 3, 5]
    # split on ";" to get each draw, split each draw on space to get the number of each type of cube
    # for each draw check that the number of cubes (idx preceeding the idx of the color) is less equal the number from the cube_d dict
    draws = draws_str.split(";")
    for draw in draws:
        draw_lst = draw.strip().split(" ")
        assert len(draw_lst) % 2 == 0 # assert length is even

        i = 0
        while i < len(draw_lst) / 2: # assumes draw_lst is in the form [X color_1 {maybe Y color_2 Z color_3} ]
            if int(draw_lst[color_idxs[i] - 1]) > cube_d[draw_lst[color_idxs[i]]]:
                return False
            i += 1
    return True

if __name__ == "__main__":
    # read input
    # f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input_small_1")
    f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input")
    sum = 0

    cube_dict = {
        "red": 12,
        "green": 13,
        "blue": 14,
        "red,": 12,
        "green,": 13,
        "blue,": 14
    }

    for line in f.readlines():
        id_end_idx = line.find(":")
        game_id = line[len("Game "):id_end_idx]
        draws = line[id_end_idx+1:]

        # if the game represented by line is possible, add its ID to the sum
        # extension: create a Game class?
        if game_possible(draws.strip(), cube_dict):
            sum += int(game_id)
    print("Sum:", sum)