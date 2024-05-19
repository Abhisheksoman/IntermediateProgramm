for j in range(1,11):
    if j==1:
        print('*'*1)
    else:
        for i in range(2,j):
            if j%i==0:
                print('*' * j)
                break
        else:
            print('*' * (j+1) )