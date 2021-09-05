import os
from time import sleep
# The screen clear function

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

def screen_clear():
	# for mac and linux(here, os.name is 'posix')
	if os.name == 'posix':
		_ = os.system('clear')
	else:
      # for windows platfrom
		_ = os.system('cls')
   
def showing_data(win, draw, lose):
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
	
	print(f'Thắng: {win} \ Hoà: {draw} Thua: {lose}')

