def minProd(n, v1, v2):
    prod = 0
    for x in range(n):
        summ = v1[x]*v2[x]
        prod+=summ
    
    return prod
   
testCases = int(input())
for i in range(testCases):
    n = int(input())
    
    v1 = sorted([int(x) for x in input().split()], reverse=False)
    v2 = sorted([int(y) for y in input().split()], reverse=True)

    print("Case #" + str(i+1) + ": " + str(minProd(n, v1, v2)))
