player = 0
board = [[' ', ' ', ' '],
		 [' ', ' ', ' '],
		 [' ', ' ', ' ']]
winner = None

def reset():
	global player
	global board
	global winner
	player = 0
	board = [[' ', ' ', ' '],
			 [' ', ' ', ' '],
			 [' ', ' ', ' ']]
	winner = None

def print_board():
	print """
		   %c | %c | %c
		  -----------
		   %c | %c | %c
		  -----------
		   %c | %c | %c
		  """ % (board[0][0], board[0][1], board[0][2],
				 board[1][0], board[1][1], board[1][2],
				 board[2][0], board[2][1], board[2][2])

def move(row, col):
	global player
	if player == 1:
		try:
			board[row][col] = 'O'
			player = (player + 1) % 2
		except Exception as error:
			print "Error: %r" % error
	else:
		try:
			board[row][col] = 'X'
			player = (player + 1) % 2
		except Exception as error:
			print "Error: %r" % error
	
			
def game_over(state):
	global winner
	lines = []
	for row in state:
		lines.append(row)
	for i in range(3):
		lines.append([state[0][i], state[1][i], state[2][i]])
	lines.append([state[0][0], state[1][1], state[2][2]])
	lines.append([state[2][0], state[1][1], state[0][2]])
	if ["X", "X", "X"] in lines:
		winner = "X"
		return True
	elif ["O", "O", "O"] in lines:
		winner = "O"
		return True
	for row in state:
		for space in row:
			if space == " ":
				return False
	return True
	
def score(state, player_number):
	if game_over(state):
		if winner == "X" and player_number == 0:
			return 10
		elif winner == "X" and player_number == 1:
			return -10
		elif winner == "O" and player_number == 0:
			return -10
		elif winner == "O" and player_number == 1:
			return 10
	return 0
	
while True:
	while not game_over():
		print_board()
		row = int(raw_input())
		col = int(raw_input())
		move(row, col)
	print_board()
	if winner:
		print "%c Wins!" % winner
	else:
		print "Draw!"
	reset()
	