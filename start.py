import tkinter
import customtkinter
import authorization
import webbrowser

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  
app.title("Smart home")
app.geometry("400x240")

def button_function():
    app.destroy()
    webbrowser.open_new(r"http://127.0.0.1:8912")
    authorization.authorization()

button = customtkinter.CTkButton(master=app, text="Авторизация", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def start():
    app.mainloop()