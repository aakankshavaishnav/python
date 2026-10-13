*def add(a,b):
    add=a+b
    print(add)

def sub(a,b):
    sub=a-b
    print(sub)

def multiplication(a,b):
    multiply=a*b
    print(multiply)
def floor_division(a,b):
    floor_div=a//b
    print(floor_div)

add(3,5)
sub(5,2)
multiplication(2,3)
floor_division(8,2)

def even_or_odd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")

even_or_odd(7)



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function call
print(is_prime(7))   # True
print(is_prime(10))  # False