p = input("Enter payment method: ")
match p:
    case "upi": print("UPI Payment Selected")
    case "card": print("Card Payment Selected")
    case "cash": print("Cash Payment Selected")
    case "wallet": print("Wallet Payment Selected")
    case _: print("Invalid Payment Method")