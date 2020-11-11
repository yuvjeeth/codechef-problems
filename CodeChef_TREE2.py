T = int(input())
while(T > 0):
    N = int(input())
    lengthStr = input()

    lengths = []
    itercount = 0

    lengths = list(map(int,lengthStr.split(" ")))
    H = max(lengths)
    while(H != 1):
        itercount += 1
        H = max(lengths)
        #print(lengths)
        for i in range(0,N):
            if(lengths[i] == H):
                lengths[i] = lengths[i] - (lengths[i] - min(lengths))
                
    #if(lengths.count(1) == N):
    #    for i in range(0,N):
    #        lengths[i] = 0
        #print(lengths)
   #     itercount += 1

    print(itercount)
    T -= 1
        
