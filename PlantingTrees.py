def plantingTrees(index):    
    minimum = index[0]
    minDays = 0
    
    for x in index:
        if x > minimum:
            minimum = index[index.index(x)]
        minimum -=1
        minDays+=1
    minDays+=(minimum + 2)
    print(minDays)
    return minDays


n = [int(x) for x in input()]

seedlings = sorted([int(y) for y in input().split()], reverse = True)
minDays = plantingTrees(seedlings)
