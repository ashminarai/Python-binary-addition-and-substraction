#Here, we import the value from conversion#
from conversion import *
#Here, we import binary and fill for adder#
from adder import binary,fill
#Here, we define the function check(number_first)
def check(number_first):
    value = False
    number=str(number_first)
    for i in range(len(number)):
        if number[i] == "0" or number[i] == "1":
            value = True
        else:
            print("\t\t|*------------------------------------------*|")
            print("\t\t|                                            |")
            print("\t\t|                 ERROR 404                  |")
            print("\t\t|     Binary number holds only 1 and 0       |")
            print("\t\t|                                            |")
            print("\t\t|*------------------------------------------*|")
            value = False
            break
    return value
#Here, we define the function checkByteNum(number_first)
def checkByteNum(number_first):
    value = False
    if number_first <= 11111111:
            value = True
    else:
        print("\t\t|*--------------------------------------------------*|")
        print("\t\t|                                                    |")
        print("\t\t|                      ERROR 404                     |")
        print("\t\t|     Value should be less than or equal to 255      |")
        print("\t\t|                                                    |")
        print("\t\t|*--------------------------------------------------*|")
        value = False
    return value
#Here, we define the function checkDec(number_first)
def checkDec(number_first):
    value = False
    if number_first < 255:
            value = True
    else:
        print("\t\t|*--------------------------------------------------*|")
        print("\t\t|                                                    |")
        print("\t\t|                      ERROR 404                     |")
        print("\t\t|     Value should be less than or equal to 255      |")
        print("\t\t|                                                    |")
        print("\t\t|*--------------------------------------------------*|")
        value = False
    return value
#Here, we define the function checkNeg(number_first)
def checkNeg(number_first):
    value = False
    if number_first < 0:
        print("\t\t|*----------------------------------------------*|")
        print("\t\t|                                                |")
        print("\t\t|                    ERROR 404                   |")
        print("\t\t|        Negative values are not allowed         |")
        print("\t\t|                                                |")
        print("\t\t|*----------------------------------------------*|")
        value = False
    else:
        value = True
    return value
#Here, we define the function inputFun#        
def inputFun():
    var= input("\nEnter 'd' or 'decimal' for decimal and 'b' or 'binary' for binary numbers ")
    isInputFun = False
    while not isInputFun:
        value = var.lower()
        if value == 'd' or value == 'decimal':
            try:
                number_first= int(input("\nEnter your 1st number: "))
                notNeg = checkNeg(number_first)
                if not notNeg:
                    continue
                demoCheck = checkDec(number_first)
                if not demoCheck:
                    continue
                number_second= int(input("Enter your 2nd number: "))
                notNeg = checkNeg(number_second)
                if not notNeg:
                    continue
                demoCheck = checkDec(number_second)
                if not demoCheck:
                    continue
                
            except:
                print("\t\t|*--------------------------*|")
                print("\t\t|                            |")
                print("\t\t|         ERROR 404          |")
                print("\t\t|    Enter numberic value    |")
                print("\t\t|                            |")
                print("\t\t|*--------------------------*|")
                continue
            if(number_first<0 or number_second<0):
                print("\t\t|*--------------------------------*|")
                print("\t\t|                                  |")
                print("\t\t|            ERROR 404             |")
                print("\t\t|    Negative value not allowed    |")
                print("\t\t|                                  |")
                print("\t\t|*--------------------------------*|") 
                continue
            if(number_first+number_second)>255:
                print("\t\t|*----------------------------------------------------------------*|")
                print("\t\t|                                                                  |")
                print("\t\t|                        ERROR 404                                 |")
                print("\t\t|     Enter the value whose sum is less than or equal to 255       |")
                print("\t\t|                                                                  |")
                print("\t\t|*----------------------------------------------------------------*|")
                continue
            
            number_binary1 = decimalToBinary(number_first)
            number_binary2 = decimalToBinary(number_second)
            number_binary1=fill(number_binary1)
            number_binary2=fill(number_binary2)

            print("\n        **FOR DECIMAL NUMBER**        ")
 
            print ("\n1st decimal number is ",number_first)
            print("2nd decimal number is ",number_second)
            print("\t\t    --------")
            print("Sum of decimal is:    ",number_first+number_second)
            
            print("\n        **FOR BINARY NUMBER**        ")
            
            print("\n1st binary number is  ",number_binary1)
            print("2nd binary number is  ",number_binary2)
            print("\t\t    ------------")
            binary(number_binary1,number_binary2)
            isInputFun = True
            
        elif value == 'b' or value == 'binary':
            while True:
                try:
                    print("\nEnter binary number. Only 1 and 0 is accepted ")

                    number1 = input("\nEnter your 1st number: ")
                    number_first = int(number1)
                    demoCheck= checkByteNum(number_first)
                    if not demoCheck:
                        continue

                    demoCheck = check(number_first)
                    if not demoCheck:
                        continue

                    number2 = input("Enter your 2nd number: ")
                    number_second = int(number2)

                    demoCheck = check(number_second)
                    if not demoCheck:
                        continue

                    demoCheck= checkByteNum(number_second)
                    if not demoCheck:
                        continue

                except:
                    print("\t\t|*----------------------------------*|")
                    print("\t\t|                                    |")
                    print("\t\t|             ERROR 404              |")
                    print("\t\t|        Enter Numeric Value         |")
                    print("\t\t|                                    |")
                    print("\t\t|*----------------------------------*|")
        
                    continue

                dec1 = stringToDecimal(number1)
                dec2 = stringToDecimal(number2)
    
                if dec1 + dec2 > 255:
                    print("\t\t|*----------------------------------------------------------------*|")
                    print("\t\t|                                                                  |")
                    print("\t\t|                          ERROR 404                               |")
                    print("\t\t|   Enter the value whose byte sum is less than or equal to 255    |")
                    print("\t\t|                                                                  |")
                    print("\t\t|*----------------------------------------------------------------*|")
                    continue
                else:
                    break
            decimal1=binaryToDecimal(number_first)
            decimal2=binaryToDecimal(number_second)
            number_binary1=fill(number1)
            number_binary2=fill(number2)

            print("\n        **FOR BINARY NUMBER**        ")
            
            print("\n1st binary number is  ",number_binary1)
            print("2nd binary number is  ",number_binary2)
            print("\t\t    ------------")
            binary(number_binary1,number_binary2)           
            
            print("\n        **FOR DECIMAL NUMBER**        ")
 
            print ("\n1st decimal number is ",number_first)
            print("2nd decimal number is ",number_second)
            print("\t\t    --------")
            print("Sum of decimal is:    ",number_first+number_second)
            isInputFun = True
        
        else:
            print("\t\t|*------------------------------------*|")
            print("\t\t|                                      |")
            print("\t\t|               ERROR 404              |")
            print("\t\t|       Please input correct value     |")
            print("\t\t|                                      |")
            print("\t\t|*------------------------------------*|")
            isInputFun = False
        

        

