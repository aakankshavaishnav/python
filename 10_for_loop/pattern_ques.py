# for i in range(10,0,-1):
#     print(i)
# str=input("enter your string").strip().lower()
# str2=""
# length=len(str)
# for element in range(length -1,-1,-1):
#     print(str[element])
#     str2=str2+str[element]
# if str==str2:
#     print("same") 
# else:print("not same")   

# name="rashi"
# for character in name:
#     print(character)


# name="python"
# length=len(name)
# for elements in range (0,length):
# #     print(name[elements])

# for i in range(3):
#     for j in range(7):
#         print(i,j)

# for row in range(3):
#     for column in range(4):
#         print("*", end="")
#     print()

# for row in range (1,5):
#     for column in range(4):
#         print(1 , end="")
#     print()    



  

for row in range(1,6):
    for column in range(1,row+1):
        print("3",end="")
    print()   

for row in range(6,1):
    for column in range(1,row+1):
        print("7",end="")
    print()           
 
for row in range(1,6):
    for column in range(1,6):
        print(column,end="")

    print()



for row in range(5):
    for column in range (6):
        print("*",end="")
for row in range(5):
    for column in range(6):
        print("*" ,end="")
for i in range (5):
    for i in range(5):
        print("*" , end="")
    print("")    

for i in range(5):
    for i in range(5 - i):
        print("*",end="")
n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(j+ 1, end="")
    print("")

for i in range (1,6):
    for j in range(i):
        print(j+1,end="")
    print("")    

for row in range(5):
    for column in range(1):
        print("*", end="")
n = 5
for i in range(1, n + 1):
    print(" "*(n - i)+"#"*i)


    n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# for i in range(1,6):
#     for j in range(1,5-1) :
#         print(" ", end="")
#     for k in range (1, i+1):
#         print("*",end="") 
#     print()       
# n = int(input("Enter your number: "))
# # for i in range(1, n + 1):
#     for j in range(i):
#         print(*+ 1, end="")
#     print("")
# reverse star
    n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
n=int(input("enter the number:"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("*", end="")
    print()

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1)) 

n = 5

for row in range(1, n + 1):
    for column in range(1, n - row + 1):
        print(" ", end="")
        
    for column in range(1, 2 * row):
        print("*", end="")
        
    print()