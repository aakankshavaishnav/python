# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break

#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         break
# else:
#     print("Done")    

# question-1-===============
# while True:
#     num=int(input("enter your num: "))    
#     if num>0:
#         continue
#     if num ==0:
#         break 

# // question -2=======
numbers = [12, 5, -4, 18, 0, 25, 30]
for number in numbers:
    if number<0:
        continue
    if number >0:
        print("posetive")
    if number==0:
        break
    print(number)