def peopInClub(line, diff):
    size = len(line)
    M = 0
    W = 0    
    count = 0
    for person in line:
        if(line[count]=='M'):
            if(abs((M + 1) - W) <= diff):
                M = M + 1
            else:
                if(count != size - 1 and line[count+1]=='W'):
                    W = W + 1
                    lineCop = list(line)
                    lineCop[count+1] = 'M'
                    line = ''.join(lineCop)
                else:
                    break
         
        if(line[count]=='W'):
            if(abs(M - (W + 1)) <= diff):
                W = W + 1
            else:
                if(count!=size-1 and line[count+1]=='M'):
                    M = M + 1
                    lineCop = list(line)
                    lineCop[count+1] = 'W'
                    line = ''.join(lineCop)
                else:
                    break
            
        count = count + 1    
    return M + W

def main():
    diff = input()
    diff = int(diff)
    line = input()
    print(peopInClub(line, diff))
    return 0

if __name__ == "__main__":
    main()
