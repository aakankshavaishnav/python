existing_balance=30000
def check_balance(existing_balance=3000):
    print("balance=",existing_balance)
def credit_balance(credit):
    total_balance=credit+existing_balance
    print(total_balance)
def withdrawl_balance(widhraw):
    total_balance=existing_balance-widhraw
    print(total_balance)

check_balance()
credit_balance(500)
withdrawl_balance(500)

# =============++++++++++++++++++++++++++
def check_balance(existing_balance=3000):
    print("balance=",existing_balance)
def credit_balance(credit,existing_balance=3000):
    total_balance=credit+existing_balance
    print(total_balance)
def withdrawl_balance(widhraw,existing_balance=3000):
    total_balance=existing_balance-widhraw
    print(total_balance)

check_balance()
credit_balance(500)
withdrawl_balance(500)
credit_balance(500,1500)
withdrawl_balance(500,1500)

# =================
existing_balance = 30000

while True:
    print("\n1. Check Balance")
    print("2. Credit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance =", existing_balance)

    elif choice == 2:
        credit = int(input("Enter amount to credit: "))
        existing_balance = existing_balance + credit
        print("Total Balance =", existing_balance)

    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))

        if withdraw <= existing_balance:
            existing_balance = existing_balance - withdraw
            print("Total Balance =", existing_balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")