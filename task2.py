'''l=['cat','bat','tab','god','dog']
out={}
for i in l:
    s=''.join(sorted(i))
    if s not in out:
       out[s]=[i]
    else:
        out[s]+=[i]
print(out)
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------function  without args but with return---------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''def task():
    a=int(input('a: '))
    b=int(input('b: '))
    return a+b
print(task())
'''

#wap to check whether the given string is palindrome or not
'''def pali():
    s=input('enter a word : ')
    return s[::-1]==s
if pali()==True:
    print('palindrome')
else :
    print('not a palindrome')'''

#wap to extract all the unique values(remove duplicates) in the given list

'''def uni():
    l=[20,30,10,30,10,20,40]
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
            
    return out
print(uni())'''

#wap to find frequency of the characters in a given list

def rep():
    s=eval(input('Enter a String list :'))
    out={}
    for i in s:
        for j in i:
            if j not in out:
                
                out[j]=1
            else:
                out[j]+=1
    return out
print(rep())






































