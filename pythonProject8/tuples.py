a=(121, 123, 145, 124, 1244, 1556, 990, 999, 101, 111, 121)
b=list(a)
largest = float('-inf')
secound_largest=float('-inf')
for i in b:
    if(i>largest):
        secound_largest=largest
        largest=i
    elif(i>secound_largest):
        secound_largest=i
print("secound largest is:",secound_largest)