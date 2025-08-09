'''def sam(n=0,out=0):
    while n!=0:
        ld=n%10
        out+=ld
        n=n//10
    print(out)
sam(7865)'''

#wap for factorial of the number using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(int(input("enter a Value : "))))

#wap to find sum of value using recursion

def sum(n):
    if n==0 or n==1:
        return 1
    return n+sum(n-1)
print(sum(int(input("enter a Value : "))))



