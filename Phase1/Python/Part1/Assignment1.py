## Assignment 1 


'''Q1= Write a program that asks the user for their name and age, then prints a
sentence like  "Hello Shradha, you are 21 years old!" 


code==

name = input("Enter your name:")
age= int(input("Enter the age:"))

print("Hi",name,"you are",age,"years old!")

'''

'''
Q2=Take two numbers as input from the user and print their sum, difference,product, and quotient

code ==

first_num=float(input("Enter the 1st name:"))
second_num=float(input("Enter the 2nd name:"))

sum= first_num+ second_num
diff= first_num-second_num
product=first_num*second_num
quotient= first_num/ second_num

print("Sum of two numbers is:",sum)
print("Difference of two numbers is:",diff)
print("Product of two numbers is:",product)
print("Quotient of two numbers is:",quotient)
'''
'''
Q3.Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
code == 

num1= float(input("Enter the num1:"))
num2= float(input("Enter the num2:"))
num3= float(input("Enter the num3:"))

avg=(num1+num2+num3)/3

print("Avg of three numbers is :",avg)
'''


''' Q4 The user enters a string containing a number (e.g., ). Convert it to:Q4 "45"
 an integer
 a float
 a string again
Print all three values with their types 
code ==

num_string=input("Enter the string contain num:")

num_integer= int(num_string)
num_float= float(num_string)
num_string2= str(num_string)

print(num_integer,type(num_integer))
print(num_float,type(num_float))
print(num_string2,type(num_string2))
'''
'''
Q5 output of the equation,ans=22
code ==
x = 10 + 3 * 2 ** 2
print(x)
'''

'''
Q6 Write a program to  swap values of two numbers entered by the user.

a=float(input("Enter the 1st num:"))
b=float(input("Enter the 2nd num:"))
print("Before swap:",a,",",b)

c=a
a=b
b=c

print("after swap:",a,",",b)
'''

'''
Q8 Take the radius (r) as user input and print the area.

r=float(input("Enter the radius of the circle:"))
PI=3.14
area= PI*r*r
print("Area of a circle:",area)

'''

'''
Q7 Ask the user for a temperature in Celsius (string input).Convert it to  float,
then calculate and print temperature in Fahrenheit

FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
code =



celTemp= str(input("Enter the temp in celsius :"))
temp_float=float(celTemp)
FahrenheitTemp = ( temp_float * (9/5)) + 32

print("You Enter temp in Celsius is",celTemp,"the conversion in Fahrenheit is:",FahrenheitTemp)

'''

'''
Q9  Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
compute simple interest:
SI = (P * R * T )/100

code=

str_prin=str(input("Enter the principal amount:"))
str_rate=str(input("Enter the rate:"))
str_time=str(input("Enter the time:"))

prin_float=float(str_prin)
rate_float=float(str_rate)
time_float=float(str_time)

SI = ( prin_float* rate_float * time_float )/100

print("Your Principle amount is:",prin_float,"Time is:",time_float,"Rate is:",rate_float,"Simple Intereset(SI) is:",SI)

'''

'''
Q10 Take a decimal number as input (like 45.78 ) and output it
integer part = 45
 fractional part = .78

 code=


num=float(input("Enter the decimal number:"))
num_int=int(num)
num_fractional= round(num - num_int,2)

print("Decimal NUmber is:",num,"\nInteger part:",num_int,"\nFractional part:",num_fractional)

'''