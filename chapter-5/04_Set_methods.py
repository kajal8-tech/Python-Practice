S = {1,2,3,4,3,4}
S2 = {8,9,10,1}


S.add(39)  #Add one element to the set
S.update([5,6,7])  #Add multiple elements to the set.
S.remove(39)  #Remove the element from the set.
print(S.union(S2))  #Returns all the unique elements from both sets
print(S.symmetric_difference(S2))  #Returns the elements that are present in either set, but not in both sets.