n=int(input('n :'))
while(n>1) :
    if(n==0 or n ==1 ):
        print('1')
    else :
        print(f'{n*(n-1)}')
        n+=1