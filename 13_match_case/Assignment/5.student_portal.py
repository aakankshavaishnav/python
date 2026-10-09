menu=input("1.view profile \n 2.view courses\n 3.view marks \n 4.view attendence \n 5.logout")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        print("view profile")
    case 2:
        print("view courses")    
    case 3:
        print("view marks")
    case 4:
        print("view attendence")
    case _:
        print("logout")            