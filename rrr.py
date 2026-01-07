import random
r = random.randint(1, 100)

while True:
	ans = input('請輸入數字:')
	ans = int(ans)
	if ans > 100 or ans < 1:
		print('只能輸入1~100喔')
	elif ans == r:
		print('終於猜對了!')
		break
	elif ans > r:
		print('再小一點')
	else:
		print('再大一點')
