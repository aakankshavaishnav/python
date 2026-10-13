def greet ():
    print("hello")

greet()    

# ======================================
# Define a function named greet that prints Hello, Python!. Call it once.

# ques-2===================
def show_name ():
    print("coco")

show_name()


# ============================
# Define a function named show_name that prints your name. Call it three times.

# ques-3
def print_line ():
    print("----------------------------------")

print_line()
# 
# Define a function named print_line that prints 20 hyphens. Call it before and after a heading.

# ques-4
def show_rule():
    print("rules")

#    Define a function named show_square that prints a 4-by-4 square of * characters using four print("****") statements. Call it once.
# ques=5
def show_sqaure():
    for i in range(4):
        print("*",end=" ")

show_sqaure()  

# ques- 6 a function named show_menu that prints three menu options. Call it twice.
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
show_menu()

# ques- 7  Define two functions, morning_message and evening_message. Call them in the reverse order of their definitions.
def morning_massage():
    print("good morning")

def evening_massage():
    print("good evening")
evening_massage()
morning_massage()     

# question=8   Define a function named show_student_card that prints a heading, a student name, and a roll number. Call it once.
def show_student_card():
    print("heading")
    print("asha")
    print("1232")
show_student_card()    

# ques=9   Define a function named print_numbers that prints the numbers 1 through 5 using five print statements. Call it twice.
def print_number():
    for i in range(1,5):
        print(i)
        i +=1

print_number()      

# ques=10 Define a function named show_pattern that prints:
def print_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)

print_pattern(5)

# ques=10 Create three functions: show_header, show_body, and show_footer. Call them in the correct order to print a simple report.
def show_header():
    print("=" * 30)
    print("       MONTHLY REPORT")
    print("=" * 30)

def show_body():
    print("Sales      : 1200")
    print("Expenses   : 800")
    print("Profit     : 400")

def show_footer():
    print("=" * 30)
    print("      End of Report")
    print("=" * 30)

show_header()
show_body()
show_footer()

# Create a function named show_separator that prints ====================. Use it between sections of a report.
def show_reports():
    print("==================")


# Debugging and 


# 1. step_one, step_two, step_three called in order 3, 1, 2
def step_one():
    print("Step One")

def step_two():
    print("Step Two")

def step_three():
    print("Step Three")

step_three()
step_one()
step_two()


# 2. show_table_heading before two student rows
def show_table_heading():
    print("Roll No | Name     | Marks")
    print("-" * 28)

show_table_heading()
print("1       | Aarav    | 85")
print("2       | Diya     | 92")


# 3. Five stars on one line, called four times
def print_stars():
    print("* * * * *")

for _ in range(4):
    print_stars()


# 4. show_welcome at the start of a program
def show_welcome():
    print("Welcome to the Python Programming Course!")
    print("Course: Introduction to Python")

show_welcome()
print("Let's start learning.")


# 5. show_help before the calculator menu
def show_help():
    print("Instructions:")
    print("1. Choose an operation from the menu.")
    print("2. Enter two numbers when asked.")
    print("3. The result will be displayed.")

show_help()
print("Menu: 1.Add  2.Subtract  3.Multiply  4.Divide")


# 6. Receipt opening and closing lines
def receipt_start():
    print("======= SHOP RECEIPT =======")

def receipt_end():
    print("====== Thank You! ======")

receipt_start()
print("Notebook   : 50")
print("Pen        : 10")
print("Total      : 60")
receipt_end()


# 7. print_box called twice
def print_box():
    print("+--------+")
    print("| Python |")
    print("+--------+")

print_box()
print_box()


# 8. Title, menu, closing message flow
def show_title():
    print("=== STUDENT MANAGER ===")

def show_menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

def show_closing():
    print("Goodbye! Have a nice day.")

show_title()
show_menu()
show_closing()