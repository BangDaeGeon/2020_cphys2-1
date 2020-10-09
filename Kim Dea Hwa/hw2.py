def GUGUDAN(a):
    x=[1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        x[i]=a*x[i]
    return x

def oddeven(a):
    
    if a%2==0:
        b='짝수,even'
    elif a%2==1 :
        b=('홀수,odd')
    else:
        b=('정수가 아님')
    return print(a,'은',b)

list = []
End=0
while End<1:
    a=input("숫자를 입력해 평균을 구하고 싶은 값들을 입력하고 'Enter'를 눌러주세요. 끝나면 'end' 혹은 '끝'을 입력해주세요");
    if a=='end' or a=='끝':
        End=+1
    else:
        list.append(float(a))
list,len(list)
def Mean(k): # 최대한 넓은 의미로 해석해서 감점은 하지 않겠으나 리스트를 입력받는 함수를 작성하는 것이 과제였음.
    Sum=0
    for i in range (0,len(list)):
        Sum=Sum+list[i]
    return Sum/k
Mean(len(list))
