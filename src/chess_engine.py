import chess

class ChessEngine:

    def __init__(self):
        self.board = chess.Board()

    def display_board(self):
        print("\nCurrent Board:\n")
        print(self.board)

    def make_move(self, move):

        try:

            chess_move = chess.Move.from_uci(move)

            if chess_move in self.board.legal_moves:

                self.board.push(chess_move)
                return True

            return False

        except:

            return None
        