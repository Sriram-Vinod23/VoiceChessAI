import customtkinter as ctk
import tkinter as tk
import chess

from src.board import ChessBoard
from src.pieces import PieceManager
from src.move_history import MoveHistory
from src.chess_engine import ChessEngine


class ChessGUI:

    BOARD_SIZE = 640
    SQUARE_SIZE = BOARD_SIZE // 8

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()
        self.window.title("VoiceChess AI")
        self.window.geometry("1200x800")

        self.engine = ChessEngine()
        self.board = self.engine.get_board()

        self.selected_square = None
        self.legal_moves = []

        self.create_layout()

        self.board_renderer = ChessBoard(
            self.canvas,
            self.SQUARE_SIZE
        )

        self.piece_manager = PieceManager(
            self.SQUARE_SIZE
        )

        self.move_history = MoveHistory(
            self.right
        )

        self.canvas.bind(
            "<Button-1>",
            self.on_click
        )

        self.refresh_board()

    def create_layout(self):

        # Left Side

        self.left = ctk.CTkFrame(self.window)

        self.left.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.canvas = tk.Canvas(
            self.left,
            width=self.BOARD_SIZE,
            height=self.BOARD_SIZE,
            highlightthickness=0
        )

        self.canvas.pack()

        # Right Side

        self.right = ctk.CTkFrame(
            self.window,
            width=300
        )

        self.right.pack(
            side="right",
            fill="y",
            padx=20,
            pady=20
        )

        title = ctk.CTkLabel(
            self.right,
            text="VOICE CHESS AI",
            font=("Arial",24,"bold")
        )

        title.pack(pady=20)

        self.status = ctk.CTkLabel(
            self.right,
            text="Ready",
            font=("Arial",18)
        )

        self.status.pack()

        history_title = ctk.CTkLabel(
            self.right,
            text="Move History",
            font=("Arial",18,"bold")
        )

        history_title.pack(pady=(20,10))

    def refresh_board(self):

        self.board_renderer.draw(
            selected_square=self.selected_square,
            legal_moves=self.legal_moves
        )

        self.piece_manager.draw(
            self.canvas,
            self.board
        )

        self.move_history.update(
            self.board
        )

    def on_click(self, event):

        col = event.x // self.SQUARE_SIZE
        row = event.y // self.SQUARE_SIZE

        square = chess.square(col, 7 - row)

        # ---------- First Click ----------

        if self.selected_square is None:

            piece = self.board.piece_at(square)

            if piece is not None and piece.color == self.board.turn:

                self.selected_square = square
                self.legal_moves = []

                for move in self.board.legal_moves:

                    if move.from_square == square:
                        self.legal_moves.append(move.to_square)

                self.status.configure(text="Piece Selected")
                self.refresh_board()

            return

        # ---------- Second Click ----------

        move = chess.Move(self.selected_square, square)

        if move in self.board.legal_moves:

            self.board.push(move)
            self.status.configure(text=f"Played: {move.uci()}")

        else:

            self.status.configure(text="Illegal Move")

        self.selected_square = None
        self.legal_moves = []

        self.refresh_board()

    def run(self):

        self.window.mainloop()