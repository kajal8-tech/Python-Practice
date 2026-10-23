Mark = int(input("Enter the mark of a student: "))

if(Mark>100):
    print("Invalid mark")
elif(Mark>=90):
    print("Gread is EX")
elif(Mark>=80):
    print("Gread is A")
elif(Mark>=70):
    print("Gread is B")
elif(Mark>=60):
    print("Gread is C")
elif(Mark>=50):
    print("Gread is D")
else:
    print("You are fail")