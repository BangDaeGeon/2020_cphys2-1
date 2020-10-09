def tot_GuGu():    ##전체 구구단 출력
	for a in range(2, 10):
		print(f'=={a} 단==', end = '\t')
	print()
	print()
	for i in range(1, 10):
		for j in range(2,10):
			print(j,"*", i,"=",i*j,end = '\t')
		print()
		print()

def n_GuGu(n):			##n단 출력
	print(f'=={n}단==')
	for i in range(1, 10):
		print(f'{n} * {i} = {n*i}')
		print()

print("전체 출력 : 1 \nn단 출력 : n")


while True:
	go = int(input('입력 : '))
	if go<1:
		print('1 이상 정수를 입력하세요')
	elif go == 1:
		tot_GuGu()
	else:
		n_GuGu(go)