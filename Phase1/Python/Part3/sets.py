## sets is a collection of unique elements 
## sets are mutable but the elements are immutable
s ={1,3,3}
s2={3,4,5}

s.add(4)

empty_set= set()

print(len(s))
print(type(s))
print((s))
print((empty_set))


##methods in set
# s.add(3) #--->adds a val
# s.removal(3)  #--->removes a val 
# s.clear  #--->empties the set
# s.pop()   #--->removes a random val
print(s.union(s2))  #--->eeturns a new union
print(s.intersection(s2))  #--->returns new intersection