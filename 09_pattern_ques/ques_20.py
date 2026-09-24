# #ques11
# n=int(input("enetr your value: "))
# for i in range(2,n,2):
#     print(i)\
    #ques=12
# n=int(input("enter your no.: "))
# for i in range (1,n,2) :
#     print(i) 
#ques=13
# n=int(input())
# for i in range(1,n+1):
#     print(i*3)
#ques=14
# n = int(input("enter your value: "))
# for i in range(1, n + 1):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
#ques=15
# n=int(input("enter: "))
# count=0
# for i in range(1,n+1,1):
#     if i %2 ==0:
#         count+=1
#         print(count)
#ques=16
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)

#quess=17
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers =", total)

#ques=18
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers =", total)
#ques=19
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#ques=20
n = int(input("Enter n: "))

product = 1

for i in range(1, n + 1):
    product = product * i

print("Product =", product)
