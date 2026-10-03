menu=input("1.Pizza \n 2.burger \n 3.pasta \n 4.sandwich")
choice =int(input("enter your choice: "))
match choice:
    case 1:
        print("you selected pizza")
    case 2:
        print("you selected burger")
    case 3:
        print("you selected pasta")
    case 4:
        print("you selected sandwich")
    case _:
        print("invalid")    

