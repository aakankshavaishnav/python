age=int(input("enter your age: ").split()[0])
print(age)
if age>=18:
    print("true")
number=int(input("enetr your number: "))
if number>=0 :
    print("positive") 

#Q=4
Result=int(input("eneter your marks"))
if Result>=40 :
    print("you are pass")
    
Q=5
user=int(input("enetr your number: "))
if user==0 :
    print("zero")

#Q=6
number=int(input("enetr youur number: "))
if number % 2 ==0 :
    print("number is even")
else:
    print("numbert is odd")
#Q=7
age=int(input("enter your age"))
if age>= 18 :
    print("Adult")
else:
    print("Minor")

#Q=8
number=int(input("enetr your number  :"))
if number %2 ==0 :
    print("Even")
else:
    print("Odd")

#Q=9
marks=int(input("enter your martks- "))
if marks>=40 :
    print("your are pass")
else:
    print("Fail")

#Q=10
num1= int(input("enter your first number: "))
num2= int(input("enetr your number: "))
if num1> num2 :
    print("num1 is greater")
else:
    print("num2 is greater")

Q=16
age=int(input("enter your age"))
if age>=18 :
    if age<=60 :
         print("your are above 18")
    else:print("belowe 18")
else: print("your are below 18")

a=map(int ,input("enter your first num: "))
b=map(int ,input("enter your second num: "))
# c=int(input("enter your third number: "))
operator =input("+,-,*,% , //")
if operator=="+" :
    print(f"addition is :("a+b"))

elif operator=="-" :
    print("a-b")    

elif operator=="%" :
    print("a%b") 

elif operator=="//" :
    print("a//b")  

else: print("invalid operator")   
nested list


Age=int(input("enter your Age"))
if Age>=18 :
    print(your )



age=int(input("enetr your age: ")) 
if age>=18 :
    print("your are above 18") 
    if age <=60 :
        print("you are atmost 60")
    else:
        print("but you ar eolder than 18") 
else:print("error")

Q=17
marks=int(input("enter your marks: "))
if marks>=40 :
    print("you are passed")
    if marks>=75 :
        print("good")
    elif marks<=45 :
        print("failed")

        
else:print("invalid")
#Q=19

Age=int(input("enter your value: "))
if Age>=18 :
    print("you are adult")
    if Age>= 60 :
        print("you are senior")
    else:print("your not super senior")
else:print("you are under 18")

#Q=20
age= int(input("enter your age: "))
marks=int(input("enter your marks: "))
if age>=18 and marks>=40 :
    print("Eligible")
else: print("not eligible")


#Q=22
number=int(input("enter your number"))
if number<10 or number>100 :
    print("special")
else:print("not special")


#CLASS CALCULATION

operation=int(input("enter the operation you want to perform: 1.addition 2.substraction 3.multiplication 4.division"))

if operation ==1 or operation==2 or operation==3 or operation==4:
    first_number=int(input("enter your number: "))
    second_numbe=int(input("enter your number: "))
    