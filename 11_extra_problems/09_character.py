# Take a string.

# For every character, print:

# Character
# Position
# Whether position is even or odd
# Whether character is vowel, consonant, digit, or special character
# At the end, count how many characters fall into each category
strings=input("enter your stringss: ")
vowel=0
vowels=["a","e","i","o","u"]
consonant=0
digit=0
special_character=0

for key,value in enumerate(strings):
    if key %2==0:
        print("even")
    else:
        print("odd") 


    if  value.isalpha():
        if value.lower() in vowels:
            type="vowel"


