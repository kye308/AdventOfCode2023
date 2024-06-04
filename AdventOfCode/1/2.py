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