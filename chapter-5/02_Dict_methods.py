a = {
    "Kajal":99,
    "Arpita":79,
    "Iti":87
}

print(a.items()) # print all the key value pairs in a tuple form
print(a.keys()) #prints only the keys
print(a.values()) #Prints only the values
a.update({"Kajal":90}) #update the key value
print(a)

print(a.get("Kajal")) #Return none if not exist
print(a["Kajal"]) # Return error if not exist