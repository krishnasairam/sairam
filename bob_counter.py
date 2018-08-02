"""BOB"""
STRING = input("Enter a string")
C = 0
for n in STRING:
    if STRING(n) == 'b' and STRING(n+1) == 'o' and STRING(n+2) == 'b':
        C += 1

print(C)    
        
