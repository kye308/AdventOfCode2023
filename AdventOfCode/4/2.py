import os

def calculateScratchcards(wantNums, myNums):
    assert(len(wantNums) == len(myNums)) # assert num cards to match equals the number of cards I have

    numCards = [1] * len(myNums)

    # for each card
    # put wantNums in a set, iterate through myNums to count matches
    # increment the number of cards based on the number of matches
    # cards cannot be copied past the end of the table
    for i in range(len(wantNums)):
        toMatch = set()
        matches = 0
        for num in wantNums[i]:
            if len(num) > 0:
                toMatch.add(num)
        for num in myNums[i]:
            if num in toMatch:
                matches += 1
        
        if matches > 0:
            for j in range(1, matches + 1):
                numCards[i + j] += numCards[i]

    return sum(numCards)


if __name__ == "__main__":
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input"))
    # f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_small"))

    lines = f.read().split('\n')

    # split on colon to separate out card num, then on | to separate wantNums from myNums
    nums = [l.split(":")[1] for l in lines] # list of winning numbers | my numbers

    wantNums = [n.strip().split("|")[0].strip().split(" ") for n in nums] # list of winning numbers
    myNums = [n.strip().split("|")[1].strip().split(" ") for n in nums] # list of my numbers

    print(wantNums, myNums)
    print (calculateScratchcards(wantNums, myNums))