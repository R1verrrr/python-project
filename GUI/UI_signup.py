import customtkinter 
import tkinter.messagebox as msgbox
import UI_login


def run():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    window = customtkinter.CTk()
    window.geometry("825x500+300+200")
    window.configure(bg="black")
    window.resizable(False, False)
    window.title("Sign Up")

    def signup():
        print("Sign up successful!")
        msgbox.showinfo("Sign up", "Sign up successful!")
        window.destroy()
        UI_login.run()

    
    frame = customtkinter.CTkFrame(master=window, width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Confirm Password", show="*")
    entry3.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, fg_color=("green"), text="Sign up", command=signup)
    button.pack(pady=12, padx=10)



    window.mainloop()

if __name__ == "__main__":
    run()