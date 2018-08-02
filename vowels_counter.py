"""Vowels"""
STRING = input("Enter a string")
VOWELS = 0
CONSONANTS = 0
for n in STRING:
    if n in 'aeiou':
        VOWELS += 1
    else:
        CONSONANTS += 1

print("Number of Vowels:")
print(str(VOWELS))
