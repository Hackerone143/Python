'''n=int(input('n: '))
i=2
count=0
while i<n:
    if n%i==0:
        print(f"{n} is not a prime")
        break
    i=i+1
else:
    print(f'{n} is a prime')
    

'''
#wap to find whether the given is prime or not using while
#first try with while loop then try with recursive function
'''
n=int(input('n: '))
i=2
while n<1 and i>n:
    if n%i==0:
        print(f"{n} is not a prime")
        break
    i=i+1
else:
    print(f'{n} is a prime')
    '''
    
def is_prime(n,i=2):
    if i<1 or n%i==0:
        return False
    if i>=n:
        return True
    return is_prime(n,i+1)

while True:
    out=int(input('enter a value : '))
    print(is_prime(out))
    print('enter 1 to continue 🤓')
    print('enter 2 to break 😒')
    pro=int(input('enter a value : '))
    if pro==1:
        print('😁 khbbeep Going 😁')
        continue
    else:
        print('😼 Thank You 😼')
        break
