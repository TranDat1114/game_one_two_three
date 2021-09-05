import random
from for_game import *

#varible
player = 0
test_input = True
won = True
downtext = ' '
text_won = 'Bạn Thắng Rồi!!!'
text_lose = 'Bạn Thua Rồi!!!'
text_draw = 'Bạn Hoà Rồi!!!'
draw = False
number = 7

#Try to input values
while test_input:
	screen_clear()
	showing_data()
	try:
		player = int(input('Nhập vào một số tương ứng: '))
	except ValueError:
		test_input = True
		
	if (player > 0) and (player < 16):
		test_input = False


list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
com = random.choice(list_a)

print(f'Bạn chọn {dictData[player]}')
print(f'Máy chọn {dictData[com]}')

# nếu player + 7 > 15: nếu player - 7 < com and player > com: thua
# nếu player - 7 < 0 : nếu player + 7 > com and player < com: thắng

if player == com:
		draw = True
elif player + 7 > 15:
	if (player - 7 < com) and (player > com):
		won = False
elif (player - 7 < 0):
	if (player + 7 > com) and (player < com):
		won = True
	else:
		won = False
else:
	if player > com:
		won = False
		
print(downtext)

if draw == True:
	print(text_draw)
elif won == True:	
	print(text_won)
else:
	print(text_lose)

print(downtext)