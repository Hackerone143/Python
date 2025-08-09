#unlock mobile using pin
import time
pin=4050
count=5
while True:
    if count>0:
        upin=int(input('enter a pin : '))
        if upin==pin:
            print('unclocked')
            break
        else:
            print('wrong pin')
    else:
        print('wait for 5 seconds')
        time.sleep(5)
        count=5


#Guess the number
'''n=44      

while True:
    value=int(input('enter a value :'))
    if value==n:
        print('You are guessed the number')
        break
    elif value>n:
        print('greater number')
    elif value<n:
        print('less than n')
'''


#login on phonepay
'''import random
n=random.randint(1000,9999)
user='hack@'
passw='@123'
while True:
    usern=input('enter a username :')
    passwo=input('enter password :')
    if usern==user and passwo==passw:
        print(n)
        otp=int(input('enter a otp :'))
        if otp==n:
            print('verified successfully')
            break
        elif otp!=n:
            print('verification failed')
    else:
         print('incorrect credential')'''


