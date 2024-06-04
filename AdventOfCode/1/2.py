import os
import re

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

def get_digits(s): # return a string of digits for a given input line
    digit_str = ""
    pos = 0
    while pos < len(s):
        for k in digits: # add digit to digit_str if a digit word is found at the current position
            if s.find(k, pos) == pos: 
                digit_str += str(digits[k])
                break
        if s[pos].isdigit():
            digit_str += s[pos]
        pos += 1
    return digit_str

def convert_letter_to_num(string):
    # for each index in eightwothree
    for i in range(len(string)):
        # for each index, start slicing the window +1 until len(string)
        j = i
        # slicing window until len(string)
        while j <= len(string):
            # if the window matches, replace the window with the number from dict, and
            # recursivly call on that newly changed string
            if string[i:j] in digits.keys():
                string = string.replace(string[i:j-1], str(digits[string[i:j]]))
                convert_letter_to_num(string)
            # no match: keep on +1 the window slicing
            else:
                j += 1
        
    # If no changes are made in this iteration, return the result
    return string

if __name__ == "__main__":
    # read input
    f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input")
    sum = 0

    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    test_cases = [
        "twone",
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "fourseven8fkmtqzdbfourseven"
    ]

    for c in test_cases:
        print(get_digits(c))
    
    print("END TEST CASES") # missing test case was repeated digits for a line
    for line in f.readlines():
        s = get_digits(line)
        
        # update sum with [first digit][second digit]
        # potential validation: check if first_digit and last_digit return nonzero length strings
        digit_str = get_digits(line)
        my_ans = int(first_digit(s) + last_digit(s))
        # my_ans = int(digit_str[0] + digit_str[-1])
        sum += my_ans

    print(sum)