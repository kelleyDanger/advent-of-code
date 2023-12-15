class Game:
	def __init__(self):
		self.shape_score = {
			"rock": 1,
			"paper": 2,
			"scissor": 3
		}

		self.move_shape = {
			"A": "rock",
			"B": "paper",
			"C": "scissor",
			"X": "rock",
			"Y": "paper",
			"Z": "scissor"
		}

		self.round_end = {
			"X": "lose",
			"Y": "draw",
			"Z": "win"
		}

		self.score = {
			"p1": 0,
			"p2": 0
		}

	def read_cheat_sheet(self, cheat_sheet_path: str):
		f = open(cheat_sheet_path, "r")
		lines = f.readlines()
		return lines

	def get_winner(self, p1_shape: str, p2_shape: str) -> int:
		winner = 0 #draw

		if p1_shape == p2_shape:
			return winner;

		if p1_shape == "rock":
			if p2_shape == "paper":
				winner = 2
			else: 
				winner = 1
		if p1_shape == "paper":
			if p2_shape == "scissor":
				winner = 2
			else: 
				winner = 1
		if p1_shape == "scissor":
			if p2_shape == "rock":
				winner = 2
			else: 
				winner = 1

		return winner

	def get_winning_shape(self, p1_shape):
		match p1_shape:
			case "rock":
				return "paper"
			case "paper":
				return "scissor"
			case "scissor":
				return "rock"

	def get_loosing_shape(self, p1_shape):
		match p1_shape:
			case "rock":
				return "scissor"
			case "paper":
				return "rock"
			case "scissor":
				return "paper"

	def get_p2_shape(self, p1_shape, p2_move: str):
		round_outcome = self.round_end.get(p2_move)

		match round_outcome:
			case "draw":
				return p1_shape
			case "lose":
				return self.get_loosing_shape(p1_shape)
			case "win":
				return self.get_winning_shape(p1_shape)

	def update_shape_points(self, p1_shape: str, p2_shape: str):
		p1_shape_score = self.shape_score.get(p1_shape)
		p2_shape_score = self.shape_score.get(p2_shape)

		self.score['p1'] += p1_shape_score
		self.score['p2'] += p2_shape_score

	def update_round_points(self, winner: int):
		# assign round points
		# if draw, each player gets 3
		# else winner gets 6 points
		match winner:
			case 0: #draw
				self.score['p1'] += 3
				self.score['p2'] += 3

			case 1:
				self.score['p1'] += 6

			case 2:
				self.score['p2'] += 6

	def calculate_round_score(self, line: str):
		p1_move, p2_move = line.split()
		p1_shape = self.move_shape.get(p1_move)
		#p2_shape = self.move_shape.get(p2_move)
		p2_shape = self.get_p2_shape(p1_shape, p2_move)
		print(f"p2 shape: {p2_shape}")

		# assign shape points
		self.update_shape_points(p1_shape, p2_shape)
		# who wins round
		winner = self.get_winner(p1_shape, p2_shape)
		self.update_round_points(winner)
		
	def calculate_game_score(self):
		return self.score


if __name__ == "__main__":
	g = Game()
	for line in g.read_cheat_sheet("d2.txt"):
		print(f"line: {line}")
		g.calculate_round_score(line)
	print(g.calculate_game_score())
