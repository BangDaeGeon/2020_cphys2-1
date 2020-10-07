def times_tables(a):
    n=[1,2,3,4,5,6,7,8,9]
    return [x*a for x in n]
    
def checkeven(a):
    if a%2 == 0:
        answer='even'
    else :
        answer='odd'
    return answer

import numpy as np
a=np.array([22,37,48,20,99,97])
b=np.mean(a)
print (b)
# 함수를 작성하는 것이 과제(-1)