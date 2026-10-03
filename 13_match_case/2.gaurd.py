# using gaurd in match case
mark=67
match mark:
    case x if x>=90:
        print("Grade A")
    case x if x>=80:    
        print("Grade B")  
    case x if x>=70:
        print("Grade C")    
    case x if x>=60:
        print ("D")
    case _:
        print("invalid")

# -----------------------------------------
# using match case in dayss    #    
day = 8
match day:
    case 1|2|3|4|5:
        print("weekdays")
    case 6|7:            
        print("weekend")
    case _:
        print("invalid day")