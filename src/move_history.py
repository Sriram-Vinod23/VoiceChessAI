import tkinter as tk


class MoveHistory:

    def __init__(self, parent):

        self.widget = tk.Text(
            parent,
            width=25,
            height=22,
            font=("Consolas", 12),
            state="disabled"
        )

        self.widget.pack(padx=10, pady=10)

    def update(self, board):

        self.widget.configure(state="normal")

        self.widget.delete("1.0", tk.END)

        moves = list(board.move_stack)

        for i in range(0, len(moves), 2):

            move_number = i // 2 + 1

            white = moves[i].uci()

            black = ""

            if i + 1 < len(moves):
                black = moves[i + 1].uci()

            self.widget.insert(
                tk.END,
                f"{move_number}. {white:<8} {black}\n"
            )

        self.widget.configure(state="disabled")