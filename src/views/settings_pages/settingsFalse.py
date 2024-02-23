# -*- coding: utf-8 -*-

import customtkinter as tk
from PIL import Image
# bg-color #3F3A46

import views.settings.config as config

# Global variables
VERSION = config.dct['VERSION']

class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        
        # !Инициализация фотографии профиля
        self.profile_photo = tk.CTkImage(light_image=Image.open(config.dct['profile_image']), size=(120, 120))
        
        self.initUI(master, width, height)
        
    def initUI(self, *args):
        
        frame = tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        # !Билд виджетов
        tk.CTkLabel(frame, bg_color="#3F3A46", text="", image=self.profile_photo, corner_radius=100).place(x=100, y=25)
        tk.CTkLabel(frame, text="You`re not logged In", font=("Verdana", 23, "bold"), bg_color="#3F3A46").place(x=40, y=170)
        