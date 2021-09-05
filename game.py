import random
from for_game import *

#Variables
downtext = ' '
text_won = 'Bạn Thắng Rồi!!!'
text_lose = 'Bạn Thua Rồi!!!'
text_draw = 'Bạn Hoà Rồi!!!'
win_point = 0
lose_point = 0
draw_point = 0
match = 0
running = True

#Try to input values
while running:
	#Variables
	number = 7
	player = 0
	draw_test = False
	won_test = True
	test_input = True
	
	while test_input:
		screen_clear()
		showing_data(win_point, draw_point, lose_point, match)
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
			draw_test = True
	elif player + 7 > 15:
		if (player - 7 <= com) and (player > com):
			won_test = False
	elif (player - 7 < 0):
		if (player + 7 >= com) and (player < com):
			won_test = True
		else:
			won_test = False
	else:
		if player > com:
			won_test = False
			
	print(downtext)

	if draw_test == True:
		print(text_draw)
		draw_point = draw_point + 1
	elif won_test == True:	
		print(text_won)
		win_point = win_point + 1
	else:
		print(text_lose)
		lose_point = lose_point + 1

	print(downtext)
	match = match + 1

	print('chơi tiếp hay không?: ')
	while test_input == False:
		play_again = str(input('Yes(y)/ No(n) \n'))
		if (play_again == 'n') or (play_again == 'N'):
			test_input = True
			running = False
		elif (play_again == 'y') or (play_again == 'Y'):
			Test_input = True
		else:
			test_input = False
			
