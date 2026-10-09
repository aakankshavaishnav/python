r = input("Enter role: ")
match r:
    case "admin": 
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest": 
        print("Limited Access")
    case _: 
        print("Invalid Role")