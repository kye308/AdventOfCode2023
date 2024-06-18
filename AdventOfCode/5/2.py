import os 

def getMinLocation(seeds, range_list):
    minLocation = 1000000000000
    for s in seeds:
        curNum = int(s)
        for map_i in range(len(range_list)):
            # for each map/range list, iterate over all tuples to see if the curNum is mapped by that tuple
            for range_i in range(len(range_list[map_i])):
                dest, src, length = range_list[map_i][range_i]
                if curNum >= int(src) and curNum < int(src) + int(length):
                    curNum -= (int(src) - int(dest))
                    break
        if curNum < minLocation:
            minLocation = curNum
    return minLocation

if __name__ == "__main__":
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input"))
    # f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_small"))

    groups = f.read().split('\n\n')

    range_list = [] # list of list of (int, int, int)
    for i in range(len(groups) - 1):
        range_list.append([])

    # could create function getSeeds
    seeds = []
    seed_ranges = groups[0].split(":")[1].strip().split(" ")
    for i in range(len(seed_ranges) // 2):
        seedNum, values = int(seed_ranges[2*i]), int(seed_ranges[2*i+1])
        for j in range(seedNum, seedNum+values, 1):
            seeds.append(j)

    for map_i in range(len(range_list)):
        lines = groups[map_i + 1].split('\n')
        # omit first line
        # add (dest src i) to a list for each map
        for line_i in range(1, len(lines), 1):
            range_list[map_i].append(lines[line_i].split(" "))
    
    # print (range_list)
    print(getMinLocation(seeds, range_list))