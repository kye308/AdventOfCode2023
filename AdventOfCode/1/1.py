import os

def first_digit(s): # returns string
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
    return "" # no digits in string

def last_digit(s): # returns string
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            return s[i]
    return "" # no digits in string

if __name__ == "__main__":
    # read input
    f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input")
    sum = 0

    for line in f.readlines():
        # update sum with [first digit][second digit]
        # potential validation: check if first_digit and last_digit return nonzero length strings
        sum += int(first_digit(line) + last_digit(line))
    print(sum)