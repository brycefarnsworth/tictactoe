PLAYER = ["X", "O"]

class Game(object):
	def __init__(self):
		self.board = [[' ', ' ', ' '],
		              [' ', ' ', ' '],
		              [' ', ' ', ' ']]
		self.player = 0
		
	def reset(self):
		self.board = [[' ', ' ', ' '],
		              [' ', ' ', ' '],
		              [' ', ' ', ' ']]
		self.player = 0
		
	def print_board(self):
		print """
		 %c | %c | %c
		-----------
		 %c | %c | %c
		-----------
		 %c | %c | %c
		""" % (self.board[0][0], self.board[0][1], self.board[0][2],
		       self.board[1][0], self.board[1][1], self.board[1][2],
		       self.board[2][0], self.board[2][1], self.board[2][2])
			   
	def get_gamestate(self):
		gamestate_board = []
		for i in range(3):
			gamestate_board.append(list(self.board[i]))
		return gamestate_board
		
	def empty_spaces(self, gamestate):
		for i in range(3):
			for j in range(3):
				if gamestate[i][j] == " ":
					return True
		return False
	
	def get_winner(self, gamestate):
		lines = []
		for row in gamestate:
			lines.append(row)
		for i in range(3):
			lines.append([gamestate[0][i], gamestate[1][i], gamestate[2][i]])
		lines.append([gamestate[0][0], gamestate[1][1], gamestate[2][2]])
		lines.append([gamestate[2][0], gamestate[1][1], gamestate[0][2]])
		if ["X", "X", "X"] in lines:
			return "X"
		elif ["O", "O", "O"] in lines:
			return "O"
		return "D"
		
	def game_over(self, gamestate):
		if self.get_winner(gamestate) != "D":
			return True
		if self.empty_spaces(gamestate):
			return False
		return True
		
	def get_legal_moves(self, gamestate):
		legal_moves = []
		for i in range(3):
			for j in range(3):
				if gamestate[i][j] == " ":
					legal_moves.append((i, j))
		return legal_moves
		
	def move(self, row, col):
		if (row, col) in self.get_legal_moves(self.board):
			self.board[row][col] = PLAYER[self.player]
			self.player = (self.player + 1) % 2
			
	def score(self, gamestate, player):
		if self.get_winner(gamestate) == PLAYER[player]:
			return 10
		elif self.get_winner(gamestate) == PLAYER[(player + 1) % 2]
			return -10
		return 0
	
while True:
	g = Game()
	while not g.game_over(g.board):
		g.print_board()
		row = int(raw_input())
		col = int(raw_input())
		g.move(row, col)
	g.print_board()
	if g.get_winner(g.board) != "D":
		print "%c Wins!" % g.get_winner(g.board)
	else:
		print "Draw!"
	g.reset()
	