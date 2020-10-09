def evod():
	while True:
		x =input("홀짝홀짝\n\n")
		if x.isdigit() == False:
			print("정수내놔")
		elif int(x)%2==1:
			print("\n=>odd")
		elif int(x)%2==0:
			print("\n=>even")

		print('\n','='*7,'\n')
		

evod()

def aver_list():
	print('리스트 평균 구해드림', '\n', '수 입력 ==> 마지막에 Rmx')
	a = []
	b = int(input())
	while True:
		a.append(int(b))
		print(a)
		b=input()
		if b == "Rmx":
			break
	average = sum(a) / len(a)
	print(average)
	
aver_list()
# sum 함수를 사용하지 말라는 조건을 어김(-1)
# Zoom을 통해 전달했던대로 다른 코드에선 위 사항을 어기지 않았으나 그 코드엔 다른 문제가 있었기에 1점만 감점함.