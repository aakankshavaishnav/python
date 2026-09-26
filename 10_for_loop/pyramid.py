# n=5
# for i in range(1,n+1):
#         for j in range(i):
#             print(" " ,end="")
#         for k in range(n):
#               print("*",end="")
#         print()  
#         #secondddddd 
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print() 
#     #thirdsssssss    
# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("=", end="")

# for i in range(5):
#     for j in range(i):
#          print(" ",end=" ")
#     for k in range():
#          print("*" , en)
#n = int(input("Enter your number: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if  j ==1 or i ==n or j == n :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# n = int(input("Enter your number: "))

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == n-1 or i==n%3 and j==n%3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    