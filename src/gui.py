import customtkinter as ctk


class ChessGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()
        self.window.title("Voice Chess AI")
        self.window.geometry("1200x800")

        self.create_layout()

    def create_layout(self):

        # Left Side (Chess Board)
        self.board_frame = ctk.CTkFrame(
            self.window,
            width=700,
            height=700
        )

        self.board_frame.pack(side="left", padx=20, pady=20)

        # Right Side
        self.side_panel = ctk.CTkFrame(
            self.window,
            width=350,
            height=700
        )

        self.side_panel.pack(side="right", fill="y", padx=20, pady=20)

        title = ctk.CTkLabel(
            self.side_panel,
            text="VOICE CHESS AI",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        self.voice_status = ctk.CTkLabel(
            self.side_panel,
            text="🎤 Waiting...",
            font=("Arial",18)
        )

        self.voice_status.pack(pady=20)

        self.ai_status = ctk.CTkLabel(
            self.side_panel,
            text="🤖 AI Ready",
            font=("Arial",18)
        )

        self.ai_status.pack(pady=20)

    def run(self):

        self.window.mainloop()