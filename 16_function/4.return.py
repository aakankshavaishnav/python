# def is_even(number):
#     return number % 2 == 0

# if is_even(8):
#     print("Even")
# else:
#     print("Odd")
# # +++++++++++++++++++++++
# a=10
# b=20
# c=30
# d=50
# e=2
# f=6
# def add (a,b):
#     c=a+b
#     return c

# def sub(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def floor_division():
#     return a//b

# def div():
#     return a/b

# print(div(floor_division(multiply(sub(add(a,b),c),d),e),f))

# def calculate(a,b):
#     return a+b,a/b
# total ,difference =calculate(10,4)
# print("total",total)
# print("difference",difference)


def order(item, quantity=1, price=100):
    print(item, quantity, price)

order("Notebook" )
order("Notebook", 3)
order("Notebook", price=50)
order("Notebook", 3, 50)