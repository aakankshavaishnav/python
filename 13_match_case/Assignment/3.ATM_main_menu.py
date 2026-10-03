menu=input("1.check balanc \n 2.withdraw \n 3.deposit money \n 4.change pin \n 5.exit")
choice=int(input("enter your choice:: "))
match choice :
    case 1:
        print("check balance selected")
    case 2:
        print("withdraw money selected") 
    case 3:
        print("deposit money selected") 
    case 4:
        print("change pin")
    case 5:
        print("exit")
    case _:
        print("invalid")                  