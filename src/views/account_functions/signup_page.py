# -*- coding: utf-8 -*-

import customtkinter as tk
from PIL import Image

from ..settings.config import dct

class ContentAccount(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        
        # !Инициализация фотографии профиля
        self.profile_photo = tk.CTkImage(light_image=Image.open(dct['profile_image']), size=(120, 120))
        
        self.initUI(master, width, height)
        
    def initUI(self, master, width, height):
        
        tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        # ! Билд виджетов
        tk.CTkLabel(self, text="", image=self.profile_photo, corner_radius=100).place(x=85, y=25)
        self.loginEntry = tk.CTkEntry(self, width=265, height=40, placeholder_text="Your login").place(x=25, y=160)
        self.passwordEntry = tk.CTkEntry(self, width=265, height=40, placeholder_text="Your password").place(x=25, y=210)
        self.forgotBtn = tk.CTkButton(self, width=125, height=40, text="Forgot password?", fg_color="#8E48F0", hover_color="#9364f2").place(x=25, y=260)
        self.signinBtn = tk.CTkButton(self, width=125, height=40, text="Sign In", fg_color="#8E48F0", hover_color="#9364f2").place(x=165, y=260)
        self.errorsText = tk.CTkTextbox(self, width=125, height=35, fg_color="#8E48F0").place(x=95, y=370)
        self.logInBtn = tk.CTkButton(self, width=125, height=40, text="Let's start!", fg_color="#8E48F0", hover_color="#9364f2").place(x=95, y=410)
        
        # !Применяем одинаковые конфиги ко всем виджетам
        for widget in self.winfo_children():
                widget.configure(bg_color="#3F3A46") 
                
        
        
