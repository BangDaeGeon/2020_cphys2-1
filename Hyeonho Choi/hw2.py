def multi(dan):    
    print(dan,'단 :', [dan*i for i in range(1,10)])
    
def OorE(number):
    if(number%2 == 1):
        return 'Odd'
    if(number%2 == 0):
        return 'Even'
    else:
        return 'Input number must to be integer'

def average(A):
    sum = 0
    for i in range(len(A)):    
        sum = sum+a[i]
    return sum/len(A)
a=[]
for i in range(1,10):
    a.append(i)
average(a)
