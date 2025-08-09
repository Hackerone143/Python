#wap for simple calc
def calc(a,b):
    a=eval(input("Enter a 1st Value : "))
    b=eval(input("Enter a 2nd Value : "))
    return a,b

while True:
    print("Enter 1 For Addition !! ")
    print("Enter 2 For Subtraction !!")
    print("Enter 3 For Multiplication !!")
    print("Enter 4 For Division !!")
    print("Enter 5 For Exit !!")
    n=input("Enter a Option : "))
    if n=='1':
        v1,v2=calc()
 
