mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))

total_percentage = ((mark1+mark2+mark3)/300)*100

if(total_percentage>=40):
    print("Your are pass: ",total_percentage)
else:
    print("Your are fail, Try again next year: ",total_percentage)
