
#print A letter in pattern program
'''n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==1 and i>1) or (j==n and i>1) or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''
#print B letter in pattern program
'''n=int(input('enter a value : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (i==1 and j<n) or (i==n and j<n) or (i==n//2+1 and j<n) or (j==n and 1<i<n and i!=n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print( )
'''

#print O letter in pattern program
'''n=int(input('enter a value : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (i==n and 1<j<n) or (j==1  and 1<i<n) or (j==n  and 1<i<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''

    
#print C letter in pattern program
'''n=int(input('enter a value : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==1 and 1<i<n) or (i==n and 1<j<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''



#print G alphabet letter in pattern method
n=int(input('enter a value : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==1 and 1<i<n) or (i==n and 1<j<n) or (j==n and 1<i<n) or (i==n//2+1 and j!=n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )












