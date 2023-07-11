class Solution:
	def is_valid_sudoku(self, board):
		# Check rows
		for i in range(9):
			seen = set()
			for j in range(9):
				if board[i][j] != '.':
					if board[i][j] in seen:
						print(f"Invalid value {board[i][j]} in row {i + 1}")
						return False
					seen.add(board[i][j])

		# Check columns
		for j in range(9):
			seen = set()
			for i in range(9):
				if board[i][j] != '.':
					if board[i][j] in seen:
						print(f"Invalid value {board[i][j]} in column {j + 1}")
						return False
					seen.add(board[i][j])

		# Check 3x3 sub-boxes
		for k in range(3):
			for l in range(3):
				seen = set()
				for i in range(3 * k, 3 * k + 3):
					for j in range(3 * l, 3 * l + 3):
						if board[i][j] != '.':
							if board[i][j] in seen:
								print(f"Invalid value {board[i][j]} in sub-box ({k + 1}, {l + 1})")
								return False
							seen.add(board[i][j])

		print("Valid Sudoku board!")
		return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

testcase1 = Solution()
print(testcase1.is_valid_sudoku(board))

testcase2 = Solution()
print(testcase2.is_valid_sudoku(board2))
