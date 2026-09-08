# Result=30
# if Result>=33 :
#     print("You are pass")
# else:   
#     print("You are fail")
# #     print("result")
# age=int(input("enter your age: ").split()[0])
# gender=input("enter your gender: ")
# gender=gender.lower()
# print(age,gender)
# if age>=18:
#     if gender=="female":
#         print("you are wonderful")

#     if gender=="female":
#         print("you are beautiful")    
#     else:
#         print("you are a waste")


# print(age)
# number=int(input("enter your number: ").split()[0])
# print(number)
# if number >=10:
#     print("number is greater than 10")
# else :print("number is less than 10")

# username="codinggita@gmail.com"
# password="232343"
# print(input("enter your username and password"))
# if username=="codinggita@gmail.com":
#     print("login succesfully")
# # else:print("login error")


# username = "codinggita@gmail.com"
# password = "232343"

# user = input("Enter your username: ")
# passw = input("Enter your password: ")

# if user == username and passw == password:
#     print("Login successfully")
# else:
#     print("Login error")

# ballon="red" 
# red="baloon"

# user=(input("enter your color"))
# hint=(input("enter your hint"))

# if user=="red" and hint=="baloon":
#     print("succesfully know")
# else:print("not error")
 #class work
number= int(input("enter your number: "))

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("enter the operation you want to perform: "))
if c==1:
    print(f"Addition of {a} and {b} is {a+b}")
elif c==2:
    print(f"Subtraction of {a} and {b} is {a-b}")
elif c==3:
    print(f"Multiplication of {a} and {b} is {a*b}")
elif c==4:
    print(f"Division of {a} and {b} is {a/b}")
elif c==5:
    print(f"floor division of {a} and {b} is {a//b}")


    #####
    a, b = map(int, input("Enter two numbers: ").split())

operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":
    print(a / b)

else:
    print("Invalid operation")