'''n=int(input('Enter a value : '))
sv=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            sv+=1
            print(sv**2,end=' ')
        else:
            print(' ',end=' ')
    print( )'''



n=int(input('enter a value : '))
n1=int(input('enter a start_value : '))
for i in range(1,n+1):
    k=n1+i-1
    for j in range(1,n+1):
        if i>=j and i%2==0:
            
            print(k**2,end=' ')
            k+=1
        elif i>=j and i%2==1:
            
            print(k,end=' ')
            k+=1
        else:

            print(' ',end=' ')
    print( )
