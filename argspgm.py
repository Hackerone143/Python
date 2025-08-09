def form(name,phno,email,alt_phno=None,alt_mail=None):
    print(" Thank You For Registering !! ")
    print('='*40)
    print("Your Name is  : ",name)
    print("Your Phone Number is : ",phno)
    print("Your Email ID is : ",email)
    print("Your Alternate Phone Number is : ",alt_phno)
    print("Your Alternate Email ID is : ",alt_mail)
while True:
    n=input('* Enter Your Name : ')
    ph=input('* Enter Your Phone Number : ')
    mail=input('* Enter Your Mail ID: ')
    a_ph=input('Enter Your Alternater Number : ')
    a_mail=input('Enter Your Alternate Email : ')
    n2=form(n,ph,mail,a_ph,a_mail)
    print(n2)
    
    print("!!! Enter 1 to continue or press any value !!! ")
    print("!!! Enter 2 to Display Your Details !!! ")
    print("!!! Enter 3 to  EXIT !!!")
    n1=input("Enter here : ")
    if n1=="1":
        continue
    elif n1=="2":
        print(n2)
        print("!!! Enter 1 to continue or press any value !!! ")
        print("!!! Enter 2 to Display Your Details !!! ")
        n1=input("Enter here : ")
        if n1=="1":
            continue
        else:
            break
    else:
        break

    
    
    
                
