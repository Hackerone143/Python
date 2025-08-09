#for primary diagonal

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('$',end=' ')
        else:
            print('*',end=' ')
    print()


# for lower triangle

for i in range(1,6):
    for j in range(1,6):
        if i>=j:#we can also write it down like i>j but it will give only 4rows
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#for upper triangle

for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('@',end='')
        elif i>j:
            print('&',end='')
        else:
            print(' ',end='')
    print()'''
    
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('0',end=' ')
        elif i<j:
            print('-',end=' ')
        else:
            print(' ',end=' ')
    print()








