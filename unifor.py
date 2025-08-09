'''l=eval(input("Enter a List : "))
uni=[]
for i in l:
    if i not in uni:
        uni.append(i)

print(uni)'''

'''l=eval(input("Enter a List : "))
uni=[]
out=[]
for i in l:
    if l.count(i)==1:
        out.append(i)
        

print(uni)'''

l=[10,2.4,'hai','python']
d={}
for i in l:
    if type(i)==str:
        d[i]=i[::-1]
        

print(d)

        

        
