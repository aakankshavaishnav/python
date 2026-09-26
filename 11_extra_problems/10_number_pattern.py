n=int(input("enter your n: "))
for i in range(1,n):
    for j in range (1,i+1):
        if j%3==0 and j%5==0:
             print("z",end=" ")
        elif j%3==0:
            print("x",end=" ")
        elif j%5==0:
            print("y",end=" ")  
        else: 
            print(j,end=" ")  
           

    print()        
