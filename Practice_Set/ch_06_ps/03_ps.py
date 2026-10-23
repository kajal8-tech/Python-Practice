p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter message: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Message is spam")
else:
    print("Message is not spam")