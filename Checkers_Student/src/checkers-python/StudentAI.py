from random import randint
from BoardClasses import Move
from BoardClasses import Board
# The following part should be completed by students.
# Students can modify anything except the class name and exisiting functions and varibles.

class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_move(self, move):
        #opponent made a move
        if len(move) != 0:
            #add opponent's move in own board
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1

        #moves: [[Move([(self.row,self.col),(pos_x,pos_y)])]]
        #move = self.minimax(self.board,self.color,4)
        move = self.alpha_beta_search(self.board, self.color, 6)

        self.board.make_move(move, self.color)
        return move


    def checker_num_heuristic(self, board, color):
        if color == 1:
            return board.black_count - board.white_count
        else:
            return board.white_count - board.black_count


    def minimax(self,board,color,depth):
        opposite = self.opposite_color(color)
        moves = board.get_all_possible_moves(color)
        best_move = moves[0][0]
        best_score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min(board, opposite,depth-1)
                board.undo()
                if score > best_score:
                    best_move = moves[i][j]
                    best_score = score
        return best_move

    def min(self,board,color,depth):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board,color)
        moves = board.get_all_possible_moves(color)
        best_score = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.max(board,opposite,depth-1)
                board.undo()
                if score < best_score:
                    best_score = score
        return best_score

    def max(self,board,color,depth):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board, color)
        moves = board.get_all_possible_moves(color)
        best_score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min(board, opposite,depth-1)
                board.undo()
                if score > best_score:
                    best_score = score
        return best_score


    def opposite_color(self,color):
        return self.opponent[color]


    def alpha_beta_search(self,board,color,depth):
        opposite = self.opposite_color(color)
        moves = board.get_all_possible_moves(color)
        best_move = moves[0][0]
        alpha = float('-inf')
        beta = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min_value(board, opposite,depth-1,alpha,beta)
                board.undo()
                if score > alpha:
                    best_move = moves[i][j]
                    alpha = score
        return best_move

    def min_value(self,board,color,depth,al,be):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board,color)
        moves = board.get_all_possible_moves(color)
        score = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = min(score, self.max_value(board,opposite,depth-1,al,be))
                board.undo()
                if score <= al:
                    return score
                be = min(be, score)
        return be

    def max_value(self,board,color,depth,al,be):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board, color)
        moves = board.get_all_possible_moves(color)
        score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = max(score, self.min_value(board, opposite,depth-1,al,be))
                board.undo()
                if score >= be:
                    return score
                al = max(al,score)
        return score








