'''n=int(input('enter a value : '))
for i in range(65,65+n):
    for j in range(65,65+n):
        if i>=j:
            print(chr(i),end=' ')
        else:
            print(' ',end=' ')
    print( )
'''

n=int(input('enter a value : '))
sv=int(input('enter a value : '))

for i in range(65,65+n):
    k=i-1
    for j in range(65,65+n):
        if i>=j:
        
            print(chr(k),end=' ')
            k=i-1
        else:
            print(' ',end=' ')
    print( )
        
