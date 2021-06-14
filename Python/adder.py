#Here we import andGate, xorGate and orGate from gates#
from gates import andGate,xorGate,orGate
def binary(num1,num2):
    
    number1 = str(num1)
    number2 = str(num2)

    if (len(number1) < 8):
        number1 = (8 - len(number1))*"0" + number1
        
    if (len(number2) < 8):
        number2 = (8 - len(number2))*"0" + number2
        
    total_sum = ''
    length = len(number1)
    carry = 0
    for i in range(length-1,-1,-1):
        andOpr = andGate(int(number1[i]),int(number2[i]))
        xorOpr = xorGate(int(number1[i]),int(number2[i]))
        sumX = xorGate(xorOpr,carry)
        andOpr2= andGate(xorOpr,carry)
        carry= orGate(andOpr,andOpr2)
        total_sum= str(sumX) + total_sum
    if(len(total_sum) != 8):
        total_sum = str(carry) + total_sum
        
    print("sum of binary is:     ",total_sum)
#Here, we define the function fill(number)#
def fill(number):
    if (len(number) < 8):
        number = (8 - len(number))*"0" + number
    return number
