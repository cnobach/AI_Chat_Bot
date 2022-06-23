from logging import PlaceHolder
from tkinter import *
from turtle import bgcolor
from urllib import response
from time import sleep
from chat import get_response, bot_name

# Color definition
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

# Fonts 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Chat Application class to enable the window / content
class ChatApplication :
    
    # Constructor that sets up tkinter and calls the setup function
    def __init__(self) -> None:
        self.window = Tk()
        self._setup_main_window()
        
    # Method to run & pull up the main window
    def run(self):
        self.window.mainloop()
    
    # Method to set the main windows properties
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # Head Label creation - tkinter label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        # Divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # Text Widget - Stored in a class becasue it will be needed later
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # Scroll bar for the text widget 
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # Bottom label creation
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=.825)
        
        # Message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Send Button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=.77, rely=.008, relheight=.06, relwidth=.22)
        
    # When the user presses enter 
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    # Insert user message to the chat box
    def _insert_message(self, msg, sender):
        if not msg:
            return
        else:
            self.msg_entry.delete(0, END)
            userMessage = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, userMessage)
            self.text_widget.configure(state=DISABLED)
            
            self._insert_response(msg)

    def _insert_response(self, msg):
        if not msg:
            return
        else:
            response = f"{bot_name}: {get_response(msg)}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, response)
            self.text_widget.configure(state=DISABLED)
            self.text_widget.see(END)
            
# Calls the chat application to run when the app is initiated
if __name__ == "__main__":
    app = ChatApplication()
    app.run()