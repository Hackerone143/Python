#print(ex_neg([10,-7,'hi',5,2.5,true,-11]))
def neg(li):
    out=[]
    for i in li:
        if type(i)==int:
            if i>0:
                out.append(i)
    return out

li=eval(input('Enter a Value :'))
print(neg(li))

