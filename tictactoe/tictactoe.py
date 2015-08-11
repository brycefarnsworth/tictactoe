PLAYER = ["X", "O"]

class Game(object):
	def __init__(self):
		self.board = [[' ', ' ', ' '],
		              [' ', ' ', ' '],
		              [' ', ' ', ' ']]
		self.player = 0
		self.choice = None
		
	def reset(self):
		self.board = [[' ', ' ', ' '],
		              [' ', ' ', ' '],
		              [' ', ' ', ' ']]
		self.player = 0
		self.choice = None
		
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
		elif self.get_winner(gamestate) == PLAYER[(player + 1) % 2]:
			return -10
		return 0
		
	def next_gamestate(self, gamestate, player, move):
		new_gamestate = []
		for i in range(3):
			new_gamestate.append(list(gamestate[i]))
		new_gamestate[move[0]][move[1]] = PLAYER[player]
		return new_gamestate
		
	def minimax(self, gamestate, minimax_player, active_player):
		"""
		if game_over:
			return score
		legal_moves = get_legal_moves
		scores = [0 for move in legal_moves]
		for i in range(len(legal_moves)):
			scores[i] = minimax(next_gamestate(legal_moves[i]))
		# We now have the list of moves and their corresponding list of scores
		# How do we tell the A.I. what move to make based on the scores?
		if minimax_player == active_player:
			self.choice = legal_moves(scores.index(max(scores)))
			return max(scores)
		else if minimax_player == active_player:
			self.choice = legal_moves(scores.index(min(scores)))
			return min(scores)
		"""
		if self.game_over(gamestate):
			return self.score(gamestate, minimax_player)
		legal_moves = self.get_legal_moves(gamestate)
		scores = [0 for move in legal_moves]
		for i in range(len(legal_moves)):
			scores[i] = self.minimax(self.next_gamestate(gamestate, active_player, legal_moves[i]), minimax_player, (active_player + 1) % 2)
		if minimax_player == active_player:
			self.choice = legal_moves[scores.index(max(scores))]
			return max(scores)
		else:
			self.choice = legal_moves[scores.index(min(scores))]
			return min(scores)
			
	def make_choice_move(self):
		self.move(self.choice[0], self.choice[1])
	
while True:
	g = Game()
	while not g.game_over(g.board):
		g.print_board()
		if g.player == 1: # 0 -> computer plays X's, 1 -> computer plays O's
			g.minimax(g.board, 1, 1)
			g.make_choice_move()
		else:
			row = int(raw_input())
			col = int(raw_input())
			g.move(row, col)
	g.print_board()
	if g.get_winner(g.board) != "D":
		print "%c Wins!" % g.get_winner(g.board)
	else:
		print "Draw!"
	g.reset()
	