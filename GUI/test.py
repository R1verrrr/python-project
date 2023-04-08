import customtkinter as ctk
import tkinter
from tkinter import messagebox

import TYPE_CHECKING

if TYPE_CHECKING:
    import signup

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

appWidth = 925
appHeight = 600

class App(ctk.CTk):
    def __init__(self, master=None):
        super().__init__()
        #set title and size of the window
        self.title("Human Resources Information System Management")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(True, True)

        #create a frame
        self.frame = ctk.CTkFrame(master=self, width=320, height=360, corner_radius=20, border_width=2)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #create a label
        self.label = ctk.CTkLabel(master=self.frame, text="Sign In", font=('Century Gothic', 30))
        self.label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        self.label1 = ctk.CTkLabel(master=self.frame, text="Forgot password?", font=('Century Gothic', 12))
        self.label1.place(x=155, y=195)

        self.label2 = ctk.CTkLabel(master=self.frame, text="Don't have an account?", font=('Century Gothic', 12))
        self.label2.place(x=50, y=300)

        #create entries
        self.entry1 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Username', font=('Century Gothic', 14))
        self.entry1.place(x=50, y=110)

        self.entry2 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*", font=('Century Gothic', 14))
        self.entry2.place(x=50, y=165)

        #create sign in button
        self.button1 = ctk.CTkButton(master=self.frame, width=220, text="Login", command=lambda: print('test'), corner_radius=6, font=('Century Gothic', 14))
        self.button1.place(x=50, y=230)

        #create sign up button
        self.button2 = ctk.CTkButton(master=self.frame, width=100, text="Sign Up", command=lambda: print('test'), corner_radius=6, font=('Century Gothic', 14))
        self.button2.place(x=200, y=300)


    def signup(self):
        self.destroy()

        
        


    def run(self):
        self.mainloop()


app = App()
app.run()

