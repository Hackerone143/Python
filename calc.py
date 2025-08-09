n=int(input('''Enter 1 For Add
               Enter 2 For Sub :
               Enter 3 For Multi: 
               Enter 4 For Div: 
               Enter 5 For Stop:'''))
def calc():
    if n==1:
        v1=eval(input("Enter a First : "))
        v2=eval(input("Enter a Second :"))
        out=v1+v2
        print(f'The add of {v1} and {v2} is ', out) 
    elif n==2:
        v1=eval(input("Enter a First : "))
        v2=eval(input("Enter a Second :"))
        out=v1-v2
        print(f'The subtract of {v1} and {v2} is ', out)
    elif n==3:
        v1=eval(input("Enter a First : "))
        v2=eval(input("Enter a Second :"))
        out=v1*v2
        print(f'The product of {v1} and {v2} is ', out)
    elif n==4:
        v1=eval(input("Enter a First : "))
        v2=eval(input("Enter a Second :"))
        out=v1/v2
        print(f'The Division of {v1} and {v2} is ', out)
    else:
        pass
