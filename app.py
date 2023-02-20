import customtkinter
import tkinter
import os
from PIL import Image
import authorization
import webbrowser



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart home")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(35, 35))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings_light.png")), size=(20, 20))

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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        def button_callback():
            print("Button click")

        def slider_callback(value):
            progressbar_1.set(value)
            print(value)
            
        frame_1 = customtkinter.CTkFrame(master=self.home_frame)
        frame_1.grid(row=0, column=0, padx=20, pady=10)
        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
        label_1.pack(pady=10, padx=10)
        progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_1.pack(pady=10, padx=10)
        button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
        button_1.pack(pady=10, padx=10)
        slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
        slider_1.pack(pady=10, padx=10)
        slider_1.set(0.5)

        frame_2 = customtkinter.CTkFrame(master=self.home_frame)
        frame_2.grid(row=0, column=1, padx=20, pady=10)
        label_2 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT)
        label_2.pack(pady=10, padx=10)
        progressbar_2 = customtkinter.CTkProgressBar(master=frame_2)
        progressbar_2.pack(pady=10, padx=10)
        button_2 = customtkinter.CTkButton(master=frame_2, command=button_callback)
        button_2.pack(pady=10, padx=10)
        slider_2 = customtkinter.CTkSlider(master=frame_2, command=slider_callback, from_=0, to=1)
        slider_2.pack(pady=10, padx=10)
        slider_2.set(0.5)

        

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.large_test_image)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="", image=self.image_icon_image)
        self.second_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.second_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.second_frame_button_3 = customtkinter.CTkButton(self.second_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.second_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.second_frame_button_4 = customtkinter.CTkButton(self.second_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.second_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
 
        switch_var = customtkinter.StringVar(value="on")
        def switch_event():
            print(switch_var.get())
        self.third_frame_switch_1 = customtkinter.CTkSwitch(self.third_frame, text="CTkSwitch", command=switch_event,
                                           variable=switch_var, onvalue="on", offvalue="off")
        self.third_frame_switch_1.pack(pady=10, padx=10)


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

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


from ya_info import info1
global info
info = info1()
app = App()
app.mainloop()