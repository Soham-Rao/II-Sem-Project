#type: ignore
import customtkinter as tk
from tkinter import *

tk.set_default_color_theme("dark-blue")
tk.set_appearance_mode("dark")

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.y = 100

        self.geometry("600x600")
        self.title("Animated Widgets")
        self.text = tk.CTkTextbox(self, 400, 100)
        self.text.place(x = 100, y = self.y)
        self.up_button = tk.CTkButton(self, 40, 20, 10, text = "up", command = self.up).place(x = 100, y = 50)
        self.down_button = tk.CTkButton(self, 40, 20, 10, text = "down", command = self.down).place(x = 440, y = 50)

    def down(self):
        if self.y < 700:
            self.y += 2
            self.text.place(x = 100, y = self.y)
            self.after(2, self.down)


    def up(self):
        if self.y > 101:
            self.y -= 2
            self.text.place(x = 100, y = self.y)
            self.after(2, self.up)

app = App()
app.mainloop()
