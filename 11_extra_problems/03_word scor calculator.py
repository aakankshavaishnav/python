sentence = input("Enter a sentence: ")
highest_score = 0
highest_word = ""
for word in sentence.split():
    score = 0
    for ch in word:
        if ch.lower() in "aeiou":
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch.isdigit():
            score += 3
        else:
            score += 4
    print(word, "=", score)
    if score > highest_score:
        highest_score = score
        highest_word = word
print("Highest scoring word:", highest_word)
print("Highest score:", highest_score)