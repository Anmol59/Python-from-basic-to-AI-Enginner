# word1="Anmol"
# word2="Tiwari"

# print(word2[2])

# for ch in word2:
#     print(ch)

#strings are immutable in python 



##########  SLICING ##############################


# word1="Anmol Sidhu"
# print(word1[0:6])


##########  STRING FORMATTING (dynamic formatting) ##############################
#1.format()

a=5
b=10

sum = a+b 
#normal formatting
print("sum is {}".format(sum))
print("language is {}".format("python"))


#index based formatting
print("sum is {1} & {0} is {2}".format(a,b,sum))

#value based formatting 
print ("value of vars {a} and {b}".format(a=10,b=6))

#2.f-strings
a=5
b=10

print(f"avg is {a} & {b} is {(a+b)/2}")

