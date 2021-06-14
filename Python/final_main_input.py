#Here, we import the value form main_test#
from main_test import *


inputFun()

flag = False
while not flag:
    cont = int(input("\npress 0 if you want to stop. press 1 to continue "))
            
    if cont == 0:
        print("\t\t|*-----------------------------------------------------*|")
        print("\t\t|                                                       |")
        print("\t\t|                        FEEDBACK                       |")
        print("\t\t|              Thankyou!Have a wonderful day:)          |")
        print("\t\t|                                                       |")
        print("\t\t|*-----------------------------------------------------*|")
        flag = True
        
    elif cont == 1:
        inputFun()
    else:
        print("\t\t|*----------------------------------*|")
        print("\t\t|                                    |")
        print("\t\t|             ERROR 404              |")
        print("\t\t|        Input correct value         |")
        print("\t\t|                                    |")
        print("\t\t|*----------------------------------*|")
        flag = False
