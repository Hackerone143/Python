def add(v1,v2):
    return v1+v2
def sub(v1,v2):
    return v1-v2
def mul(v1,v2):
    return v1*v2
def true_div(v1,v2):
    return v1/v2
def floor_div(v1,v2):
    return v1//v2
def mod(v1,v2):
    return v1%v2

def get():
    v1=int(input('enter the 1st value :'))
    v2=int(input('Enter the 2nd value :'))
    return v1,v2
while True:
    print('Welcome to Calculator')
    print('1.ADD')
    print('2.SUB')
    print('3.MUL')
    print('4.TRUE DIV')
    print('5.FLOOR DIV')
    print('6.MODULUS')
    print('7.EXIT')
    op=int(input('Enter '))