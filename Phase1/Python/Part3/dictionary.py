#### key(unique):value pairs
### dictionary are mutable in nature 

info_student={
    "name":"Anmol",
    "subject" : ["maths","physics","dsa"],
    "CGPA" : 8.7
                 
}


print(info_student)

info_student["CGPA"]=9.0

print(info_student)
print(info_student["CGPA"])


### methods in dictionary 
#d.keys() -->return all keys
#d.values()-->return all values
#d.items() -->return(key,val)pairs
#d.get(val) -->return val access to key
#d.update(new_item) -->adds new item  to dict

print(info_student.keys())
print(info_student.values())
print(info_student.items())
print(info_student.get("CGPA"))


info_student.update ({
    "back":1
})
print(info_student)