# total=0
# flag=True
# for i in range(5):
#     marks=int(input("enetr your marks: "))
#     total+=marks
#     if marks<35:
#         flag= False 

# percentage=total/5
# if flag:
#     if percentage>=90:
#         grade="A+"
#     elif percentage>=80:
#         grade="A"
#     elif percentage>=70:
#         grade="B"
#     elif percentage>=60:
#         grade="C"
#     elif percentage>=50 :
#         grade="D" 
#     else:
#         grade="f"               
# else:
#     print("fail")

# print(total,percentage,grade)
# if flag==True:
#     print("pass")
# else:
#     print("fail")


#secondquestionsss
total=0
member=True
for i in range(5):
    price=int(input("enter your  price value: "))
    total+=price

if price>=5000:
    discount=0.2
elif price>=2000:
    discount=0.1
elif price>=1000:
    discount=0.05
else:
    discount=0
final=price-price*discount


if member==True:
   final=final-final*0.05
   print("memeber discount applied")

else:
  print("Total:", total)
print("Discount:", discount * 100, "%")
print("Final bill:", final)


 
   

