#here i have created a basic class and object

'''class sam:
    a=10
    b=20
obj1=sam()
obj2=sam()
print(obj1.a)
print(obj2.a)'''

#to modify the value using class name

class sam:
    a=10
    b=20
obj1=sam()
obj2=sam()

sam.a=100
obj1.b=200
print(obj1.a)#if we use class name to modify the value it will  modify all of them
print(obj2.a)
print(obj1.b)#but here if I mentioned obj1.a to modify value it will only modify the specified data
print(obj2.b)