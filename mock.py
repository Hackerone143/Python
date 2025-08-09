#wap to find a prime number using for and while and recursion function

'''n=int(input('Enter a Value : '))
i=2
while n<1 and i>n:
    if n%i==0:
        print(f'{n} is not Prime')
        break
    i+=1
else:
    print(f'{n} is a Prime')'''

#using recursion function
'''def is_prime(n,i=2):
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
        print('😁 keep Going 😁')
        continue
    else:
        print('😼 Thank You 😼')
        break'''

#using for loop
#n=int(input('Enter a value : '))


#wap to find strong number using for and while loop and recursion function


#wap to convert lowercase to uppercase and uppercase to lowercase
'''s=input('enter a word : ')
out=''
for i in s:
    if 'A'<=i<='Z':
        out+=i.lower()
    elif 'a'<=i<='z':
        out+=i.upper()
    else:
        out+=i
print(out)'''
#wap to extract numbers from the string and list
'''s=eval(input('Enter a value : '))
out=[]
for i in s:
    if type(i) in [int,float,complex]:
        out.append(i)
print(out)'''

#wap to find given number is even or odd
'''n=int(input('enter a value :'))
if n%2==0:
    print('even')
else:
    print('odd')'''

#wap to print primary diagonal triangle


#wap to find secondary diagonal triangle


#wap to find lower diagonal and upper diagonal


#wap to find given string is palindrome or not
'''def palin(s):
    if s[::-1]==s:
        print('palindrome')
    else:
        print('not a palindrome')
print(palin('malayalam'))'''

#wap to find factorial of the given digit
'''def fact():
    n=int(input('enter value :'))
    out=1
    for i in range(1,n+1):
        out*=i
    print(out)
print(fact())'''
#wap to find armstrong number using for and while loop and recursive function


#wap for calculator using function

'''def add():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1+v2
def sub():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1-v2
def mul():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1*v2
def div():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1/v2
def floor():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1//v2
def mod():
    v1=int(input('enter a 1st value :'))
    v2=int(input('enter a 2nd value :'))
    return v1%v2


while True:
    print('enter 1 to add ')
    print('enter 2 to sub ')
    print('enter 3 to multiply ')
    print('enter 4 to divide ')
    print('enter 5 to get modulus ')
    print('enter 6 for floor division ')
    print('enter 7 to exit ')
    n=int(input('entere a value :'))
    if n==1:
        print(add())

    elif n==2:
        print(sub())
    elif n==3:
        print(mul())
    elif n==4:
        print(div())
    elif n==5:
        print(floor())
    elif n==6:
        print(mod())
    else:
        print('Thank you')
        break'''

#wap to check length of the integer
'''n=int(input('enter a value : '))

con=str(n)
print(len(con))'''
jju
