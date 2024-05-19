x=int(input('enter the range'))
i=1

while i<=x:
    if(i%2==0):
        print('*' * i )
    else:
        print('*' * i*2)
    i=i+1