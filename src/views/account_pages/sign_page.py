# -*- coding: utf-8 -*-

import customtkinter as tk
from PIL import Image


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
        
        # !Билд виджетов и описание их функций
        tk.CTkLabel(frame, bg_color="#3F3A46", text="", image=self.profile_photo, corner_radius=100).place(x=100, y=25)
        self.loginEntry = tk.CTkEntry(frame, width=265, height=40, placeholder_text="Your login", bg_color="#3F3A46").place(x=45, y=160)
        self.passwordEntry = tk.CTkEntry(frame, width=265, height=40, placeholder_text="Your password", bg_color="#3F3A46").place(x=45, y=210)
        self.forgotBtn = tk.CTkButton(frame, width=125, height=40, bg_color="#3F3A46", text="Forgot password?", fg_color="#8E48F0", hover_color="#9364f2").place(x=112.5, y=260)
        self.logInBtn = tk.CTkButton(frame, width=125, height=40, text="Let's start!", fg_color="#8E48F0", hover_color="#9364f2", bg_color="#3F3A46").place(x=112.5, y=410)
