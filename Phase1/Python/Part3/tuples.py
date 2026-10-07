#tuples are immutable sequences of values 

tup = (1,2,3,100.45,3,33,2,2)

print(tup)
print(type(tup))
print(len(tup))
print(tup[2:4])

for i in tup:
    print(i)

#methods in tuple 
print(tup.index(2))  
print(tup.count(2))