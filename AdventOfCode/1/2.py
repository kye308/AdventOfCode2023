import os

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
    print("END TEST CASES\n") # missing test case was repeated digits for a line

    for line in f.readlines():
        s = get_digits(line)
        
        # update sum with [first digit][second digit]
        # potential validation: check if first_digit and last_digit return nonzero length strings
        val = int(s[0] + s[-1])
        sum += val

    print(sum)