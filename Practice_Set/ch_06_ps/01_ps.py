Num1 = int(input("Enter the 1st number: "))
Num2 = int(input("Enter the 2nd number: "))
Num3 = int(input("Enter the 3rd number: "))
Num4 = int(input("Enter the 4th number: "))

if(Num1>Num2 and Num1>Num3 and Num1>Num4):
    print("Number 1 is greatest")
elif(Num2>Num1 and Num2>Num3 and Num1>Num4):
    print("Number 2 is greatest")
elif(Num3>Num1 and Num3>Num2 and Num3>Num4):
    print("Number 3 is greatest")
else:
    print("Number 4 is greatest")

