x=int(input("enter the size"))
a=[]
for i in range(x):
    i =int(input())
    a.append(i)
z=0
while z<x:
    if (a[z] % 2 == 0):
      a[z]="@"
    elif(a[z]%7==0):
        a[z]="%"
    z+=1
print(a)