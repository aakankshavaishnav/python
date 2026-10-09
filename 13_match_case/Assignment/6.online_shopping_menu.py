menu= int("1.electronic \n 2.clothing  \n 3. Books \n 4.grocery \n 5.exit")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        print("opening electronics")
    case 2:
        print("opening clothing")        
    case 3:
        print("books")
    case 4:
        print("grocery")
    case _:
        print("exit")            