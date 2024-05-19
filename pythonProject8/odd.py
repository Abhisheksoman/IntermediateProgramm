list=[]
x=int(input("enter your size"))
for y in range(x):
    y=int(input())
    list.append(y)
print(list)
z=0
while z<x:
    if list[z]%2!=0:
        list[z]="@"
    z+=1
list.reverse()
print(list)