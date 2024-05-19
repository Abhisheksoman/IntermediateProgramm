def calculate_pi(n):
    pi=0
    denom=1
    for i in range(n):
        if i%2==0:
            pi+=4/denom
            denom+=2
        else:
            pi-=4/denom
            denom+=2
    return pi
e=int(input("enter the value"))
print(calculate_pi(e))
