import customtkinter 
import tkinter.messagebox as msgbox
import UI_login

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master=master, width=400, height=300)
        self.pack()
        
        self.entry1 = customtkinter.CTkEntry(master=self, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=self, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.entry3 = customtkinter.CTkEntry(master=self, placeholder_text="Confirm Password", show="*")
        self.entry3.pack(pady=12, padx=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("825x500")
        self.resizable(True, True)
        self.title("Sign Up")

        self.frame = MyFrame(master=self)

        self.button = button(master=self, text="Sign up")
        self.button.pack()

    

class button(customtkinter.CTkButton):
    def __init__(self, master=None, text=""):
        super().__init__(master=master, text=text, command=signup)
        self.pack(pady=12, padx=10)

def signup():
    print("Sign up successful!")
    msgbox.showinfo("Sign up", "Sign up successful!")
    # self.destroy()
    # UI_login.run()

app = App()
app.mainloop()