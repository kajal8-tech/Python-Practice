Num = int(input("Enter a number: "))

for i in range (2,Num):
    if(Num%i)==0:
        print("The number is not prime.")
        break
else:
    print("Number is prime.")