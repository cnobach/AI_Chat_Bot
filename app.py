from tkinter import *
from chat import get_response, bot_name

# Color definition
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

# Fonts 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication :
    
    def __init__(self) -> None:
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()