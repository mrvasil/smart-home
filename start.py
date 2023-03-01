import tkinter
import customtkinter
import webbrowser
import random
import requests
import time

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  
app.title("Smart home")
app.geometry("400x240")

def button_function2():
    global rand_string
    r = requests.get("http://192.168.1.181:8912/token", params={'secret': rand_string})
    f = open("secrets.txt", 'a').write(r.text)
    app.destroy()

def button_function():
    global rand_string
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_string = ''.join(random.choice(letters) for i in range(22))
    webbrowser.open_new(r"http://192.168.1.181:8912/?secret="+rand_string)   
    time.sleep(2)
    button = customtkinter.CTkButton(master=app, text="Я авторизовался", command=button_function2)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app.mainloop()

button = customtkinter.CTkButton(master=app, text="Авторизация", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def start():
    app.mainloop()

#start()