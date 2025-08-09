#using function for find leap year
'''
def is_leap(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year=int(input('enter a year: '))
print(is_leap(year))'''

#to find the second max value
'''def run_up(run):
    cop=run
    max_v=cop.remove(max(cop))
    return max(cop)
run=eval(input('enter a list : '))
print(run_up(run))

#run=eval(input('enter a list'))
#max_v=max(run)
#print(max_v)'''

#swapcase method using function
def swap(case):
    c=case.swapcase()
    return c

case=input()
print(swap(case))
    






































