def find(n, m):
    diff = int(1e9)
    summ = int(1e9)

    for x in range(len(n)):
        for y in range(x + 1, len(n)):
            both = n[x] + n[y]
            absolute = abs(m - both)
            if (absolute < diff):
                diff = absolute
                summ = both
    return summ

def main():
    while True:
        #nArray = []
        #mArray = []
        try:
            count = 1
            while True:
                nArray = []
                mArray = []
                n = int(input())
                #print("N: ", n)
                for i in range(0, n):
                    line = int(input())
                    nArray.append(line)
                m = int(input())
                #print("M: ", m)
                for i in range(0, m):
                    line = int(input())
                    mArray.append(line)
                print("Case {}:".format(count))
                for x in mArray:
                    clSum = find(nArray, x)
                    print("Closest sum to {} is {}.".format(x, clSum))
                count += 1

        except EOFError:
            break
    
    
if __name__ == "__main__":
    main()  
