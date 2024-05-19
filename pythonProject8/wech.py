z=int(input("enter the size"))
a=[]
sum=0
for i in range(z):
    y =int(input())
    a.append(i)
    if(i%2==0 and i%3!=0):
        sum+=i
print(sum)