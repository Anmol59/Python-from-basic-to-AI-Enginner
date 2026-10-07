# list is a mutable  sequences  of values 

marks=[89,56,78,45,12,96,]

print(marks[2])
print(len(marks))

marks[2]= 100
print(type(marks))


#slicing in list
print(marks[:5])


#methods in list 

marks.append(100)
print(marks)
marks.insert(5,90)
print(marks)

marks.reverse()
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)


marks.count(4)
print(marks)



###### LOOPS IN LISTS ##########
idx=0
x=12
for mark in marks:
    if mark == x:
        print(idx)
        break
    idx += 1
