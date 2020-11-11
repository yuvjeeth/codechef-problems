N = int(input())
inStr = input()
army = list(map(int,inStr.split(" ")))

soldiersEven = 0
soldiersOdd = 0

for i in range(0,N):
    if(army[i] % 2 == 0):
        soldiersEven += 1
    else:
        soldiersOdd += 1

if(soldiersEven > soldiersOdd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
