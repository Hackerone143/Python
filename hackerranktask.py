import email.utils

yname=input('Enter your name :')
valid=input('Enter a mail id :')
data=''
for i in valid:
    if i==index[0] and 'A'<=i<='Z' or 'a'<=i<='z':
        out=+i
print email.utils.parseaddr(f"('{yname}','{out}')")
        
        
