d = int(input("Enter day number: "))
match d:
    case 1 | 2 | 3 | 4 | 5: print("Weekday")
    case 6 | 7: print("Weekend")
    case _: print("Invalid Day")