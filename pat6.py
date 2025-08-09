n=int(input('enter a digit : '))
sv=int(input('enter a starting value : '))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(chr(sv),end=' ')
            sv+=1
        else:
            print(' ',end=' ')
    print( )
