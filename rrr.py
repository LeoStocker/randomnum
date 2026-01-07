import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 # count = count + 1
	ans = input('請輸入數字:')
	ans = int(ans)
	if ans > end or ans < start:
		print('只能輸入', start, '~', end, '的範圍喔!')
	elif ans == r:
		print('終於猜對了!')
		print('沒錯答案就是', r,'!')
		print('這是你猜的第', count,'次')
		break
	elif ans > r:
		print('再小一點')
	else:
		print('再大一點')
	print('這是你猜的第', count,'次')
