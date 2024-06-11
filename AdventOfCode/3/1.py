# only need to keep track of "current" row being calculated, the previous row and the next row
# for each number check all adjacent squares for symbols

import os

def isSymbol(row, index): # returns bool
    if index >= 0 and index < len(row): 
        assert len(row[index]) == 1
        return row[index].isdigit() is False and row[index] != "."
    return False

def shouldIncludePartNumber(prevRow, currRow, nextRow, start, end):
    if isSymbol(currRow, start - 1) or isSymbol(currRow, end + 1):
        return True
    for i in range(start - 1, end + 2):
        if isSymbol(prevRow, i) or isSymbol(nextRow, i):
            return True
    return False

def sumPartNumbers(s): # returns int
    # s is schematic (list of str)
    partSum = 0

    # validate: check that s has length at least 2, check that each row has the same length
    # could only check row length if we used indices for the rows

    # store the current row, and the row above and below
    # you could also just store the row numbers
    prevRow = "." * len(s[0])
    currRow = s[0]
    nextRow = s[1]

     # index of start and end of current number
    iNumStart = -1
    iNumEnd = -1

    # for each row
    for i in range(len(s)):
        rowI = 0
       
        # iterate through current row for numeric characters
        while rowI < len(currRow):
            if currRow[rowI].isdigit():
                # if numeric, set iNumStart, then continue until the char at index i is not numeric to determine iNumEnd
                if iNumStart == -1:
                    iNumStart = rowI
                    rowI += 1
                    continue
                # already have iNumStart, continue tracking the current number
                else:
                    rowI += 1
                    continue
            else:
                # if we were tracking a number, set the end index
                if iNumStart > -1:
                    iNumEnd = rowI - 1
                    # check for symbols given iNumStart, iNumEnd
                    # if symbol found, update result
                    if shouldIncludePartNumber(prevRow, currRow, nextRow, iNumStart, iNumEnd):
                        partSum += int(currRow[iNumStart:iNumEnd+1])
                
                    # reset iNumStart, iNumEnd
                    iNumStart = -1
                    iNumEnd = -1
                    rowI += 1
                else:
                    rowI += 1

        # add number at end of row if we are tracking one
        if iNumStart > -1:
            if shouldIncludePartNumber(prevRow, currRow, nextRow, iNumStart, len(currRow) - 1):
                partSum += int(currRow[iNumStart:])
            # reset iNumStart, iNumEnd
            iNumStart = -1
            iNumEnd = -1

        # update rows for next iteration

        nextRow = s[i+2] if i < len(s) - 2 else "." * len(s[0])
        currRow = s[i+1] if i < len(s) - 1 else "." * len(s[0])
        prevRow = s[i]

    return partSum

if __name__ == "__main__":
    grid = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    grid2 = [
        "100*12",
        "......"
    ]

    f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input")
    gridBig = f.read().split('\n')

    print (sumPartNumbers(grid))
    print (sumPartNumbers(grid2))
    print (sumPartNumbers(gridBig))
