from PIL import Image, ImageTk
import chess
import os


class PieceManager:

    def __init__(self, square_size):

        self.square_size = square_size
        self.images = {}

        self.load_images()

    def load_images(self):

        folder = os.path.join("assets", "pieces")

        names = [
            "wp", "wr", "wn", "wb", "wq", "wk",
            "bp", "br", "bn", "bb", "bq", "bk"
        ]

        for name in names:

            path = os.path.join(folder, f"{name}.png")

            image = Image.open(path)

            image = image.resize(
                (
                    self.square_size - 10,
                    self.square_size - 10
                )
            )

            self.images[name] = ImageTk.PhotoImage(image)

    def draw(self, canvas, board):

        for square in chess.SQUARES:

            piece = board.piece_at(square)

            if piece is None:
                continue

            symbol = piece.symbol()

            if symbol.isupper():
                key = "w" + symbol.lower()
            else:
                key = "b" + symbol

            file = chess.square_file(square)
            rank = chess.square_rank(square)

            x = file * self.square_size + self.square_size // 2
            y = (7 - rank) * self.square_size + self.square_size // 2

            canvas.create_image(
                x,
                y,
                image=self.images[key]
            )