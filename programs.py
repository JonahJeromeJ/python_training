
#####1
# v=int(input("last number:"))
# print(v)
# for i in range(1,v+1):
#     print(i)
#     if i%2==0:
#      {print("even")}
#     else:

#      {print("odd")}

# print(type(v))

######2
# a = input("1st no.: ")
# b = input("2nd no.: ")

# if a.isdigit() == False or b.isdigit() == False:
##.isnumeric()
#     print("Error")
# else:
#     a = int(a)
#     b = int(b)
#     print(a + b)


# try:
#     a = int(input("1st no.: "))
#     b = int(input("2nd no.: "))
#     sum = a + b
#     print(sum)
# except ValueError:
#    print("Error")






####3
# try:
#     v = int(input("Enter a number: "))
    
#     if v > 0:
#         print("Positive")
#     elif v < 0:
#         print("Negative")
#     else:
#         print("Zero")

# except ValueError:
#     print("Invalid input! Please enter a valid integer.")





####4
# s = "26"        
# num_int = int(s)    
# print(num_int)     
# print(type(num_int)) 
# num_float= float(num_int)
# print(type(num_float)) 

# num_int1 = int(num_float) 
# print(type(num_int1))

###5

# Get user input
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operation: ")

# if op == "+":
#     result = a + b
# elif op == "-":
#     result = a - b
# elif op == "*":
#     result = a * b
# elif op == "**":
#      result=a**b
# elif op == "/":
#     if b == 0:
#         result = "Error: Division by zero"
#     else:
#         result = a / b
# else:
#     result = "Invalid operator"

# print("Result:", result)




####extra 
# # if more than 100 produve error
# try:
#     v=int(input("number:"))
#     if v>100:
 
#         raise("error")
#     else:
#         print("ok")


# except Exception as e:
#     print(e)



# 
# v2 = int(input("Enter number2: "))
# v3 = int(input("Enter number3: "))

# if v1.isnumeric==False:
#     print("v1 is a wrong input")
# elif v2.isnumeric==False:
#     print("v2 is a wrong input")
# elif v3.isnumeric==False:
#     print("v3 is a wrong input")
# else:
#     values = [v1, v2, v3]
#     max_val = max(values)
#     count_max = values.count(max_val)

#     if v1 == v2 == v3:
#         print("All three numbers are equal.")
#     elif count_max == 2:
#         print("Two numbers are equal and greatest.")
#     elif count_max == 1:
#         if max_val == v1:
#             print("v1 is greatest.")
#         elif max_val == v2:
#             print("v2 is greatest.")
#         else:
#             print("v3 is greatest.")



# word = (input("Enter string: "))
# alpha=input("enter which alphabet")
# x = word.count(alpha)

# print(x)


# i=0
# char_count={}
# name="hi how are you "
# name = name.replace(" ", "")
# for i in name:
#     if i not in char_count:
#      char_count[i]=1
#     else:
#      char_count[i]+=1

# print(char_count)

# def my_function():
#  i=0
#  char_count={}
#  name=input("enter:")
#  name = name.replace(" ", "")
#  for i in name:
#     if i not in char_count:
#      char_count[i]=1
#     else:
#      char_count[i]+=1
#  print(char_count)
# my_function()


# name="awsedf"
# n=45

# print(f"{name}+{n}")
# name=input("enter:")
# n=int(input("enter:"))
# def my_function1(name,n):
 

#   print(f"{name}+{n}")

# my_function1(name,n) 

# import datetime
# def PrinTime():
#   current_datetime = datetime.datetime.now()
# print("Current date and time:")

# PrinTime()
# Python3 code to  calculate age in years

from datetime import date
birthDate=date(2004,4,14)
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year 
    if ((today.month, today.day) < (birthDate.month, birthDate.day)):
        print(age-1)
    else:
        
        print("exact age:",age,datetime.)
calculateAge(birthDate)

