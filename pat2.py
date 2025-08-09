'''n=int(input( ) )
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n+1:
            print('*',end=' ')

    print()


n=int(input( ) )
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('$',end=' ')
        elif i==j:
            print('@',end=' ')
        elif i+j>n+1:
            print('&',end=' ')
        elif i+j<n+1:
            print('&',end=' ')
            
        elif i>j:
            print('#',end=' ')
        
        else:
            print('%',end=' ')
       

    print()


n=int(input('enter value : ' ) )
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<n+1:
            print('*',end=' ')
        elif i+j==n+1:
            print('@',end=' ')

    print()
'''
n=int(input('enter value : ' ) )
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


    
