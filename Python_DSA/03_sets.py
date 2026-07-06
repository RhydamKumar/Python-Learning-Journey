set1= {3,45,2,34}
set2= { 12,53,5,45,58}

print(set1,type(set1))


#set methods

set1.add(32)
set1.remove(34)
set1.discard(2332) # same as remove but dont throw error if not present in set

print (set1)





# set operations 

c= set1.union(set2)
print (c)

d= set1.intersection(set2)
print(d)
