#wap to find the initial index of the given character from the string
s='murugann'
c='n'
def f_index(s,c):
    for i in range(0,len(s)):
        if s[i]==c:
            return i
    return 'char is not present'

print(f_index(s,c))