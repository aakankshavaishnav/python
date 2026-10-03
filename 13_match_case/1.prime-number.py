
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