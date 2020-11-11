T = int(input())
outputs = []
while(T > 0):
    
    smallestNumber = -1
    smallestQuotient = -1
    
    inStr = input()
    N = int(inStr.split(" ")[0])
    K = int(inStr.split(" ")[1])

    inStr = input()
    PList = list(map(int,inStr.split(" ")))
    
    for i in range(0,N):
        tempSmallQuotient = 0
        if(PList[i] <= K):
            if(K % PList[i] == 0):
                tempSmallQuotient = K // PList[i]
                if(smallestQuotient == -1 or smallestQuotient > tempSmallQuotient):
                    smallestQuotient = tempSmallQuotient
                    smallestNumber = PList[i]
        
    outputs.append(smallestNumber)
    T -= 1
print(*outputs, sep="\n")
