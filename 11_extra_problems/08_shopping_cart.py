# Take prices of 8 products.

# For every price:

# Below 500 → "Budget"
# 500–1999 → "Regular"
# 2000–4999 → "Premium"
# 5000 or more → "Luxury"
# Calculate:

# Total amount.
# Number of products in each category.
# Average product price.

total=0
budget=0
regular=0
premium=0
luxury=0
for i in range(8):
    price=int(input(f"enter your product price:{i}:"))


    if price<=500:
        print("budget") 
        # budget += use for count !!
        budget +=1
    elif 1999>price>500:
        print("regular")
        regular +=1
    elif 2000>price>4999:
        print("premium") 
        premium +=1
else:
    print("luxury")
    luxury +=1

total += price  
averageprice=total/8
print("budget",budget)
print("regular", regular)
print("premium",premium)
print("luxury",luxury)
print("averageprice",averageprice)
