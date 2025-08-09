import random

def login():
    ph_no=eval(input('enter your phone number : '))
    return ph_no
store_phno=login()
user_n=['Hacker']
password=['hack143']
yuser=input('enter your username :')
ypass=input('enter your password :')
while True:
    if yuser in user_n and ypass in password:
        ph=eval(input('enter your registered phone number :'))
        for ph in store_phno:
             otp=random.randint(1000,9999)
             print(otp)
             rotp=int(input('enter your input :'))
             if rotp==otp:
                 print('you have logined successfully')
                 break
             else:
                 print('you have failed to login invalid credentials')
        else:
            print(' phone number is not in database')
    else:
        print('invalid credintials')
            

