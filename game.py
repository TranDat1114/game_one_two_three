# Import thư viện random
import random
# Import hàm nhà làm\ * tức là import tất cả
from for_game import *

# Variables
downtext = ' '
text_won = 'Bạn Thắng Rồi!!!'
text_lose = 'Bạn Thua Rồi!!!'
text_draw = 'Bạn Hoà Rồi!!!'
win_point = 0
lose_point = 0
draw_point = 0
match = 0
running = True

# Gọi là game thì phải chơi được liên tục và while true: là cách để thực hiện việc đó
while running:
	# Variables
	number = 7
	player = 0
	draw_test = False
	won_test = True
	test_input = True
	
	# Try to input values
	# Thuật toán là nếu nhập vào khác số từ 1 đến 15 thì buộc nhập lại
	while test_input:
		# Gọi hàm làm sạch terminal
		screen_clear()
		# Hiện ra các dữ liệu trò chơi gồm: dict[menu chọn từ 1 - 15]; điểm
		showing_data(win_point, draw_point, lose_point, match)
		# Try - except tức là bắt lỗi mục đích để handle nếu có lỗi do người dùng tạo ra
		try:
			player = int(input('Nhập vào một số tương ứng: '))
		except ValueError:
			test_input = True
			
		if (player > 0) and (player < 16):
			test_input = False

	# Cách tạo 1 list
	list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	# Random trong list a
	com = random.choice(list_a)
	
	# Đơn giản là một cách print giá trị và chuỗi hơi khác bình thường một tý
	print(f'Bạn chọn {dictData[player]}')
	print(f'Máy chọn {dictData[com]}')
	
	# Thuật toán logic của trò chơi này
	# nếu player + 7 > 15: nếu player - 7 < com and player > com: thua
	# nếu player - 7 < 0 : nếu player + 7 > com and player < com: thắng
	# Có nhiều cách và mình dùng cái này vì nó đơn giãn nhất
	
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
	
	# Xuống dòng cho đẹp thôi bình thường thì là '\n'
	# Nhưng powerShell của mình cứ sau mỗi lần print là con trỏ chuột tự xuống dòng
	# Nên mình dùng '__' (__: ký hiệu cho khoảng trống : Space)
	print(downtext)
	
	# Show_point
	# Dùng để tăng điểm sau mỗi vòng chơi
	# Bạn có thể tách hàm show_data thành thánh 1 hàm mới tên là show_point và gọi nó sau đoạn if - else này 
	# Để nó cập nhật điểm ngay lập tức
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
	
	# Tương tự show_point nhưng là đếm số trận đã chơi
	match = match + 1
	
	# Test is variables for testing input
	test = True
	print('chơi tiếp hay không?: ')
	while test:
		# if users have wrong input program show input again
		play_again = str(input('Yes(y)/ No(n) \n'))
		
		#func_input() là hàm trong for_game.py
		if func_input(play_again) == True:
			test = False	
		# PLEASE STOP DOING THAT HOÀNG
		# Why u have too much commit bruh? :L
		elif func_input(play_again) == False:
			test = False
			running = False
		else:
			print('"yes"; "YES"; "Yes"; "y"; "Y" nếu đồng ý chơi lại \n')
			print('"no"; "NO"; "No"; "n"; "N" nếu muốn thoát \n')
			test = True
			
