inStr = input()
inStr = list(map(float,inStr.split(" ")))
withdrawAmt = inStr[0]
initialBalance = inStr[1]

if(withdrawAmt % 5 == 0):
    if(initialBalance > (withdrawAmt + 0.50)):
        out = initialBalance - withdrawAmt - 0.50
        print('{0:.2f}'.format(out))
else:
    print('{0:.2f}'.format(initialBalance))

