'''n=int(input('enter a value : '))
k=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            k=i+j-1
            print(k,end=' ')
        else:
            print(' ',end=' ')
    print()'''

    

n=int(input('enter a value : '))
n1=int(input('enter a starting value : '))
k=n1-1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            k+=1
            print(k**2,end=' ')
        else:
            print(' ',end=' ')
    print()
            
