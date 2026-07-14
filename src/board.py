import chess


class ChessBoard:

    LIGHT = "#F0D9B5"
    DARK = "#B58863"

    def __init__(self, canvas, square_size):

        self.canvas = canvas
        self.square_size = square_size

    def draw(self, selected_square=None, legal_moves=None):

        self.canvas.delete("all")

        # Draw board
        for row in range(8):

            for col in range(8):

                x1 = col * self.square_size
                y1 = row * self.square_size

                x2 = x1 + self.square_size
                y2 = y1 + self.square_size

                color = (
                    self.LIGHT
                    if (row + col) % 2 == 0
                    else self.DARK
                )

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline=color
                )

        # Highlight selected square
        if selected_square is not None:

            file = chess.square_file(selected_square)
            rank = chess.square_rank(selected_square)

            x1 = file * self.square_size
            y1 = (7 - rank) * self.square_size

            x2 = x1 + self.square_size
            y2 = y1 + self.square_size

            self.canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                outline="lime",
                width=4
            )

        # Draw legal move circles
        if legal_moves:

            for square in legal_moves:

                file = chess.square_file(square)
                rank = chess.square_rank(square)

                x = file * self.square_size + self.square_size // 2
                y = (7 - rank) * self.square_size + self.square_size // 2

                r = 10

                self.canvas.create_oval(
                    x - r,
                    y - r,
                    x + r,
                    y + r,
                    fill="yellow",
                    outline=""
                )