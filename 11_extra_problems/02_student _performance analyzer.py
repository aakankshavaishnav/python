fail = 0
pass_count = 0
good = 0
excellent = 0

for i in range(10):

    marks = int(input("Enter your marks: "))

    if marks < 35:
        print("Fail")
        fail += 1

    elif marks < 50:
        print("Pass")
        pass_count += 1

    elif marks < 75:
        print("Good")
        good += 1

    else:
        print("Excellent")
        excellent += 1

print("Fail students:", fail)
print("Pass students:", pass_count)
print("Good students:", good)
print("Excellent students:", excellent)