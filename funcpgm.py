#wap to find a factorial of the number
'''def fact():
    n=int(input('enter value :'))
    res=1
    for i in range(1,n+1):
        res*=i
    print(res)

fact()
'''
#wap to check the given number is prime number or not
'''
  def prime():
    n=int(input('enter value :'))
    if n>=2:
        for i in range(2,n):
            if i%2==0:
                print('not a prime number')
                break
            else:
                print('prime number')
    else:
        print('not a prime number')

prime()
'''
#wap to perform add of 2 numbers without using return
'''def add(a,b):
    print(a+b)

add(10,35)
'''

#wap to check whether the given string is palindrome or not
'''
def palin(s):
    if type(s)==str:       
        if s==s[::-1]:
            print('palindrome')
        else:
            print('not a palindrome')
'''
#wap to replace the space with '-' in given string

'''def rep(s):
    out=''
    if type(s)==str:
        for i in s:
            if 'A'<=i<='Z' or 'a'<=i<='z' or 1<=i<=9:
                out=out+i
            else:
                out+='-'
        print(out)
    else:
        print('not a string')

rep('hello world')'''

#wap to check that given password is valid or not
'''
def valid(s):
    if len(s)>=8:
        for i in s:
            if 'A'<=i<='Z' and 'a'<=i<='z' and 1<=i<=9 and i in '@#!$':
                print('the given password is valid')
            else:
                print('pass is not valid')
    else:
        print('length is lesser than 8 ')
valid('Hello@123world')'''

##this is an correct way for the solution
'''def valid(s):
    lc,up,sc,dg=0,0,0,0
    if len(s)>=8:
        for i in s:
            if 'A'<=i<='Z':
                up+=1
            elif 'a'<=i<='z':
                lc+=1
            elif i>='1' and i<='9':
                dg+=1
            else:
                sc+=1
        if lc>=1 and up>=1 and dg>=1 and sc>=1:
            print('valid')
        else:
            print('not valid')

valid('Hello@1world')'''

#                







































        
