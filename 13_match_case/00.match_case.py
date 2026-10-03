num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
match (num1, num2):
    case (1,0):
        print("berry")
    case (2,0):
        print("cherry")
    case (0,1):
        print("apple")
    case (0,2):
        print("banana")
while True:
    num1 = int(input("Enter the first number (0 to stop): "))
    if num1 == 0:
        num2 = int(input("Enter the second number (0 to stop): "))
        if num2 == 0:
            print("Stopped.")
            break
    else:
        num2 = int(input("Enter the second number: "))

    match (num1, num2):
        case (1, 0):
            print("berry")
        case (2, 0):
            print("cherry")
        case (0, 1):
            print("apple")
        case (0, 2):
            print("banana")
        case _:
            print("Invalid choice")

# ------------------------

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
flag=True
while flag:
    print("1. addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("addition is: ",num1+num2)
        case 2:
            print("substraction is: ",num1-num2)
        case 3:
            print("multiplication is: ",num1*num2)
        case 4:
            print("division is: ",num1/num2)
        case 0:
            flag=False
        case _:
            print("Invalid choice")

# -----------------            # 

num=int(input("Enter the number: "))    
flag=True
while flag:
    print("1.even")        
    print("2.odd")
    print("3.prime")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            if num%2==0:
                print("even")
            else:
                print("not even")
        case 2:
            if num%2!=0:
                print("odd")
            else:
                print("not odd")
        case 3:
            for i in range(2,num):
                if num%i==0:
                    print("not prime")
                    break
            else:
                print("prime")
        case 0:
            flag=False
        case _:
            print("Invalid choice")
    

            
