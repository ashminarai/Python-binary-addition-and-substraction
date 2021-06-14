#Here, we define the function decimalToBinary(a)#
def decimalToBinary(a):
    val = a
    total= ""
    while val>0:
        r= val%2
        total=str(r)+total
        val = int(val/2) 
    return total
#Here, we define the function binaryToDecimal(a)#
def binaryToDecimal(a):
    val = a
    total = 0
    i=0
    while(val>0):
        r = val%10
        total +=r*(2**i)
        i=i+1
        val = int(val/10)
    return total
#Here, we define the function StringToDecimal(a)#
def stringToDecimal(a):
    num1 = 0
    num2 = 0
    for i in range(len(a)-1,-1,-1):
        b = int(a[i])
        num1 = num1 + (b*(2**num2))
        num2 = num2 + 1

    return num1

