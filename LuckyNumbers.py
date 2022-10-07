def luckyNum(digits, allNums):
    length = 10
    #check in whole range
    for x in range(2, digits+1):
        listForSupply = []
        count = 0
        #check in "lucky" subsets
        for y in allNums:
        #check that first n digits form num divisible by n
            for z in range(length):
                newDigit = y*length
                newDigit += z
                #check if evenly divisible
                if newDigit % x == 0:
                    #append to list containing lucky numbers
                    listForSupply.append(newDigit)
                    count += 1
        allNums = listForSupply
    print(count)

def main():
    n = int(input())
    count = 0
    allNums = [1,2,3,4,5,6,7,8,9]
    return(luckyNum(n, allNums))

if __name__ == "__main__":
    main()
