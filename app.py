import customtkinter
import requests 
import tkinter as tk
import os
from PIL import Image
import authorization
import webbrowser
import sys
import functools
import json

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Command", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart home")
        self.geometry("670x550")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(35, 35))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "play_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings_light.png")), size=(20, 20))
        self.add_station_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "station_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "station_light.png")), size=(50, 50))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Умный дом", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Дом",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Сценарии",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Настройки",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, text="Обновить", command=self.update_button)
        self.frame_4_button.grid(row=5, column=0, padx=20, pady=20, sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ScrollableLabelButtonFrame(self, corner_radius=0, fg_color="transparent")
        global all1
        def all1():
            global i_for_switch        
            y, x, i_for_switch = 0, 0, 0
            frame_sp, label_sp, switch_sp, for_switch_sp, label2_sp, image_sp = [], [], [], [], [], []
            switch_var_sp = []

            def switch_event(a):
                url = 'https://api.iot.yandex.net/v1.0/devices/actions'
                s = requests.Session()
                token = info[4]
                headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
                data1 = '''{"devices": [{"id": "'''+a[0]+'''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": '''+switch_var_sp[a[1]].get()+'''}}]}]}'''
                r=requests.post(url,headers=headers,data=data1)

            for i in range(len(info[0])): 
                frame_sp.append(customtkinter.CTkFrame(master=self.home_frame))
                label_sp.append(customtkinter.CTkLabel(master=frame_sp[-1], justify=customtkinter.LEFT, text=info[1][i]))
                label_sp[i].pack(pady=6, padx=10)
                if (info[0][i] == 'devices.types.light') or (info[0][i] == 'devices.types.socket'): 
                    switch_var_sp.append(customtkinter.StringVar(value=str(info[5][i_for_switch]).lower()))
                    for_switch_sp.append(functools.partial(switch_event, [info[2][i], i_for_switch]))
                    switch_sp.append(customtkinter.CTkSwitch(master=frame_sp[-1], text="ON/OFF", command=for_switch_sp[-1], variable=switch_var_sp[-1], onvalue="true", offvalue="false"))
                    switch_sp[i_for_switch].pack(pady=6, padx=10)
                    i_for_switch += 1
                    if info[6][i] == 'offline':
                        label2_sp.append(customtkinter.CTkLabel(master=frame_sp[-1], justify=customtkinter.LEFT, text="offline"))
                        label2_sp[-1].pack(pady=6, padx=10)

                if 'devices.types.smart_speaker' in info[0][i]:
                    image_sp.append(customtkinter.CTkLabel(frame_sp[-1], text="", image=self.add_station_image)) 
                    image_sp[-1].pack(padx=0, pady=10)

                if i%3==0: 
                    y += 1
                    x = 0
                x+=1
                frame_sp[i].grid(row=y, column=x, padx=20, pady=10, sticky="nsew")

        all1()

        




        

        # create second frame
        # self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame = ScrollableLabelButtonFrame(self, corner_radius=0, fg_color="transparent")
        global all2
        def all2():
            frame_sp, label_sp, button_sp, for_button_sp = [], [], [], []
            x, y = 0, 0
            def button_function(a):
                url = 'https://api.iot.yandex.net/v1.0/scenarios/'+a+'/actions'
                s = requests.Session()
                headers={'Authorization': 'Bearer '+info[4]}
                r=requests.post(url,headers=headers)

            for i in range(len(info[3][0])):
                if i%2==0: 
                    y += 1
                    x = 0
                x+=1
                for_button_sp.append(functools.partial(button_function, info[3][0][i]))
                frame_sp.append(customtkinter.CTkFrame(master=self.second_frame))
                label_sp.append(customtkinter.CTkLabel(master=frame_sp[-1], justify=customtkinter.LEFT, text=info[3][1][i]))
                frame_sp[i].grid(row=y, column=x, padx=20, pady=10, sticky="nsew")
                label_sp[i].pack(pady=0, padx=0)
                button_sp.append(customtkinter.CTkButton(master=frame_sp[-1], text="", image=self.image_icon_image, command=for_button_sp[-1]))
                button_sp[-1].pack(pady=20, padx=10)
        all2()

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        switch_var = customtkinter.StringVar(value="on")
        def leave():
            open('secrets.txt', 'w').close()
            f = open("secrets.txt", 'a').write('\n')
            app.destroy()
        self.third_frame_button_1 = customtkinter.CTkButton(self.third_frame, text="Выйти из аккаунта", command=leave)
        self.third_frame_button_1.pack(pady=10, padx=10)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def update_button(self):
        global info
        info = info1()
        all1()
        all2()

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


from ya_info import info1
global info
info = info1()
if info!=0:    
    app = App()
    app.iconbitmap("C:/Users/alexe/Downloads/logo.ico")
    app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='C:/Users/alexe/Desktop/YandexID/test_images/logo.png'))
    app.iconphoto(True, tk.PhotoImage(file='C:/Users/alexe/Desktop/YandexID/test_images/logo.png'))
    app.mainloop()