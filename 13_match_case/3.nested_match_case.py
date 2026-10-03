# Nested Match Case Example

account = "student"
choice = 4

match account:

    case "student":

        match choice:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Choice")

    case "teacher":

        match choice:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("Invalid Choice")

    case _:
        print("Invalid Account Type")
# ---------------------------
# another match case example

user="customer"
choice=1
match user:
    case "customer":
        match choice:
            case 1:
                print("product")
            case 2:
                print("view info")
            case 3:
                print("view refund") 
            case _:
                print("invalid")  

    case "manager":
        match choice:
            case 1:
                print("account info")
            case 2:
                print("student info") 
            case 3:
                print("salary")
            case _:
                print("invaluid")    
    case _:
#         print("invalid")                      
       
command = "start"
# -----------------------------------
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown Command")

command = "restart"
# -------------------------
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown Command")

# --------------------------

choice = 2

match choice:
    case 1:
        print("First")
        print("Option")
    case 2:
        print("Second")
        print("Option")
    case _:
        print("Invalid")