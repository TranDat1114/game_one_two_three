# Import thư viện OS là một thư viện có điều khiển terminal, hệ điều hành,... 
# Trong ChuongTrinh này là cls (xoá màn hình) tương tự clrscr trong pascal
import os
# Thư viện time này mình không dùng trong chương trình, 
#mình test xoá màn hình trong 5s nhưng quên xoá
from time import sleep

# Tạo thư viện
dictData = {
		1 : 'Rock',
		2 : 'Fire',
		3 : 'Scissors',
		4 : 'Snake',
		5 : 'Human',
		6 : 'Tree',
		7 : 'Wolf',
		8 : 'Sponge',
		9 : 'Paper',
		10: 'Air',
		11: 'Water',
		12: 'Dragon',
		13: 'Devil',
		14: 'Lighting',
		15: 'Gun'}

# The screen clear function
def screen_clear():
	# for mac and linux(here, os.name is 'posix')
	if os.name == 'posix':
		_ = os.system('clear')
	else:
	# for windows platfrom
		_ = os.system('cls')
   
def showing_data(win, draw, lose, match):
	global dictData
	# Data game
	result = []
	#Show data and clean it
	for i in range(1, len(dictData) + 1, 1):
		txt = str(i) + ':' + str(dictData[i]) 
		result.append(txt)
		if i == 5:
			result.append('')
		elif i == 10:
			result.append('')
		elif i == 15:
			result.append('')
	for i in range(0, len(result), 1):
		print(result[i])
	# show match
	print(f'Số Trận: {match}')
	# show point
	print(f'Thắng: {win} \ Hoà: {draw} Thua: {lose}')

# Mình dùng hàm func_input này để đỡ làm rối main program
def func_input(play_again): 
	if (play_again == 'y') or (play_again == 'Y') or (play_again == 'Yes') or (play_again == 'yes') or (play_again == 'YES'):
		return(True)
	elif (play_again == 'n') or (play_again == 'N') or (play_again == 'No') or (play_again == 'no') or (play_again == 'NO'):
		return(False)
	else:
		return('1')
