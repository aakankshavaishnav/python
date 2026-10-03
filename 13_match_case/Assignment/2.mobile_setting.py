menu=input("1.wi-fi, \n 2.bluetooth 3.\n Mobile data \n 4.airplane mode \n 5.exit")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        print("you selecterd wif-i")
    case 2:
        print("you selecterd bluetooth")
    case 3:
        print("you selected mobile data")
    case 4:
        print("airplane mode")    
    case _:
        print("exit")                