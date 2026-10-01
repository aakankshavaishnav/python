name = input("enter your sentence: ").lower()
vowel = "aeiou"

freq = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
vowels = 0
consonants = 0

for ch in name:
    if ch.isalpha():
        if ch in vowel:
            vowels += 1
            freq[ch] += 1
        else:
            consonants += 1

if vowels > consonants:
    print("Vowels Win")
elif consonants > vowels:
    print("Consonants Win")
else:
    print("Draw")

for v in freq:
    print(v, ":", freq[v])