CityGroup = []
front = 0
rear = 0

outputs = []
T = int(input())
while(T > 0):
    inStr = input()
    inStr = list(map(int, inStr.split(" ")))
    N = inStr[0]
    K = inStr[1]
    X = inStr[2]
    Y = inStr[3]

    T -= 1
    
