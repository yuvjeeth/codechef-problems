T = int(input())
outputs = []
while(T > 0):
    
    P1 = 0
    P2 = 0
    
    N = int(input())
    inStr = input()
    ArrN = list(map(int,inStr.split(" ")))
    ArrN.sort(reverse=True)
    for i in range(0,N):
        if(i == 0):
            P1 += ArrN[i]
        elif(i % 2 == 1 and i != 1):
            P1 += ArrN[i]
        elif(i % 2 == 0 or i == 1):
            P2 += ArrN[i]
    if(P1 > P2):
        outputs.append("first")
    elif(P2 > P1):
        outputs.append("second")
    else:
        outputs.append("draw")
    T -= 1
print(*outputs, sep="\n")
        

