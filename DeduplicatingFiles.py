def collision(files):
    coll = 0
    unique = 0
    for _, elem in files.items():
        if elem[0] > 1:
            for x, y in elem[1].items():
                coll = coll + (elem[0] - y) * y
            unique = unique + len(elem[1])
        else:
            unique = unique + 1
    
    
    return(unique, coll)

def XorAscii(file):
    
    hashing = 0
    for x in file:
        hashing ^= ord(x)
    return hashing



def main():
    output = []
    while True:
        sub = []
        numFiles = int(input())
        if numFiles < 1 or numFiles > 500:
            break
        hashes = []
        files = {}
        for i in range(0, numFiles):
            file = input()
            hashing = XorAscii(file)
            if len(file) > 50 or len(file) < 1:
                break
            if hashing not in files:
                files[hashing] = [0, {}]
            files[hashing][0] = files[hashing][0] + 1
            if file not in files[hashing][1]:
                files[hashing][1][file] = 1
            else:
                files[hashing][1][file] = files[hashing][1][file] + 1
                       
        
        unique, coll = collision(files)
        coll = coll//2
        sub.append(unique)
        sub.append(coll)
        output.append(sub)
                
    for x in output:
        print(x[0], x[1])
        

if __name__ == "__main__":
    main()
