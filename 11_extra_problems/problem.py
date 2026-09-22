# # number=int(input("Enter your number: "))
# # if number>=0:
# #    print("Positive")
# # elif number<=0:
# #    print("nagative")
# # elif number==0:
# #    print("zero")
# # else:print("invalid")
   
# #Q=2
# # number=int(input("enter your number: "))
# # if number%2==0 and number>0:
# #    print("positive even")
# # elif number%2==0 and number<0:
# #     print("nagative even")
# # elif number%2 != 0 and number <0:
# #    print("positive odd")
# # elif number%2 ==0 and number<0:
# #    print("nagative odd")
# # # else:print("invalid")
      
# #Q=3
# # a=int(input("enter your first value: "))
# # b=int(input("enter your second value: "))
# # if a>b :
# #    print("a is larger")
# # elif a<b :
# #    print("b is larger")
# # elif a==b :
# #    print("both are equal")
# # else:("error")

# # #Q=4
# # a=int(input("enter num1: "))
# # b=int(input("enetr num2: "))
# # c=int(input("enter num3: "))
# # if a<b and a<c :
# #    print("a is smaller")
# # elif b<a and b<c :
# #    print("b is smaller") 
# # elif c<a and c<b :
# #    print("c is smalller") 

# #Q=5
# # a=int(input("enetr your num: "))
# # b=int(input("enter your num2:  "))
# # c=int(input("enter your num3:  ")) 
# # if a>b and a>c :
# #    print("a is largest ")
# # elif b>a and a>c :
# #    print("b is largest")
# # elif c>b and c>a :
# #    print("c is largest")    

# #Q=6
# # number=int(input("enter your num: "))
# # if number%5==0 and number%11==0:
# #    print("divisible")
# # elif number%5==0:
# #    print("only 5")
# # elif number%11==0 :
# #    print("only 11")
# # elif number%5 != 0 and number%11 !=0 :
# #    print("neither 11 nor 5")   

# # #Q=7 
# # number=int(input("enetr your number: "))
# # if number%3==0 and number%7==0 :
# #    print("divisible")
# # elif number%3== 0 :
# #    print("divisible")
# # #Q=8
# # marks=int(input("enter your marks: "))
# # if marks<0:
# #    print("invalid") 
# # elif marks>100:
# #    print("invalid marks")
# # elif marks>=40:
# #    print("pass")
# # elif marks<40 :
# #    print("fail")  


# #Q=9
# # marks=int(input("enter your number: "))
# # if marks>90 and marks<=100:
# #    print("A")
# # elif marks>80 and  marks<=89:
# #    print("B")
# # elif marks>70 and marks<=79 :
# #    print("C")
# # elif marks>60 and marks<=69:
# #    print("D")
# # elif marks>40 and marks<=49:
# #    print("E")
# # elif marks<40:
# #    print("fail")         
# #Q=11
# # leap=int(input("enter a leap year: "))
# # if leap%4==0 :
# #     print("it's a leap year ")
# # elif leap%4 !=0 :
# #     print("it's not a leap year")    

# # char=input("enter your character:  ")
# # if char.isupper():
# #     print(f"is alphabet is upper")
# # elif char.islower():
# #     print(f"lowercase")
# # elif char.isdigit():
# #     pirnt(f"digit")
# # else:print("special char")

# #q 13
# # character=input("enter your character: ")
# # if character>="a" and character<="z" or character>="A" and character<="Z":
# #     if character=="a" or character=="e" or character=="i" or character=="o" or character=="u" or character=="A" or character=="E" or character=="I" or character=="O" or character=="U":
# #         print("Vowel")
# #     else:
# #         print("Consonant")
# # else:
# #     print("Invalid input")

# #q 14
# # cost_price=float(input("enter your cost price: "))
# # selling_price=float(input("enter your selling price:"))
# # if selling_price>cost_price:
# #     profit=selling_price-cost_price
# #     print("Profit =",profit)
# # elif selling_price<cost_price:
# #     loss=cost_price-selling_price
# #     print("Loss =",loss)
# # else:
# #     print("No profit and no loss")

# #Q=15
# # cost_price=float(input("enter your cost price: "))
# # selling_price=float(input("enter your selling price:"))
# # if selling_price>cost_price:
# #     profit=selling_price-cost_price
# #     print("Profit =",profit)
# #     percentage_of_profit=profit / cost_price * 100
# # elif selling_price<cost_price:
# #     loss=cost_price-selling_price
# #     print("Loss =",loss)
# #     percentage_of_profit=loss / cost_price * 100

# # else:
# #     print("No profit and no loss")
# #  
# #q 17
# a=float(input())
# b=float(input())
# operator=input()
# if operator=="+":
#     print(a+b)
# elif operator=="-":
#     print(a-b)
# elif operator=="*":
#     print(a*b)
# elif operator=="/":
#     if b==0:
#         print("Cannot divide by zero")
#     else:
#         print(a/b)
# else:
#     print("Invalid operator")

# #q 18
# temperature=float(input())
# if temperature<0:
#     print("Freezing")
# elif temperature<=15:
#     print("Very Cold")
# elif temperature<=25:
#     print("Cold")
# elif temperature<=35:
#     print("Normal")
# else:
#     print("Hot")

# #q 19
# number=int(input())
# if number<0:
#     print("Negative")
# elif number<=10:
#     print("0-10")
# elif number<=50:
#     print("11-50")
# elif number<=100:
#     print("51-100")
# else:
#     print("Above 100")

# #q 20
# a=int(input())
# b=int(input())
# c=int(input())
# if a+b>c and a+c>b and b+c>a:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# #q 21
# a=int(input())
# b=int(input())
# c=int(input())
# if a+b<=c or a+c<=b or b+c<=a:
#     print("Invalid triangle")
# elif a==b and b==c:
#     print("Equilateral")
# elif a==b or b==c or a==c:
#     print("Isosceles")
# else:
#     print("Scalene")

# #q 22
# balance=float(input())
# withdrawal=float(input())
# if withdrawal<=0:
#     print("Invalid withdrawal amount")
# elif withdrawal%100!=0:
#     print("Withdrawal amount must be divisible by 100")
# elif withdrawal>balance:
#     print("Insufficient balance")
# elif balance-withdrawal<500:
#     print("At least 500 must remain")
# else:
#     remaining=balance-withdrawal
#     print("Withdrawal successful")
#     print("Remaining balance:",remaining)

# #q 23
# username=input()
# password=input()
# if username!="admin":
#     print("User not found")
# elif password!="python123":
#     print("Wrong password")
# else:
#     print("Login successful")

# #q 24
# amount=float(input())
# if amount<500:
#     discount_percent=0
# elif amount<1000:
#     discount_percent=5
# elif amount<2000:
#     discount_percent=10
# elif amount<5000:
#     discount_percent=15
# else:
#     discount_percent=20
# discount_amount=amount*discount_percent/100
# final_amount=amount-discount_amount
# print("Original amount:",amount)
# print("Discount percentage:",discount_percent)
# print("Discount amount:",discount_amount)
# print("Final amount:",final_amount)

# # 
# text = "Hello Python"
# print(text.find("o", 5))
