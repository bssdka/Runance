# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

import views.settings.config as config 

# Global variables
VERSION = config.dct['VERSION']

class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        
        self.initUI(master, width, height)
        
    def initUI(self, *args):
        
        frame = tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        # !Билд всех виджетов
        # Рамки для расположения виджетов настроек
        head_frame = tk.CTkFrame(frame, fg_color="#70687D", width=310, height=60).place(x=20, y=20)
        main_frame = tk.CTkFrame(frame, fg_color="#70687D", width=310, height=380).place(x=20, y=90)
        
        # Виджеты окна (head_frame)
        self.default_btn = tk.CTkButton(head_frame, text="Default", font=("Verdana", 15, "bold"), width=140, height=40, bg_color="#70687D", corner_radius=10, fg_color="#8E48F0", border_color='white', hover_color="#9364f2", border_width=2).place(x=30, y=30)
        self.apply_btn = tk.CTkButton(head_frame, text="Apply", font=("Verdana", 15, "bold"), width=140, height=40, bg_color="#70687D", corner_radius=10, fg_color="#8E48F0", border_color='white', hover_color="#9364f2", border_width=2).place(x=180, y=30)
        
        # Виджета окна (main_frame)
        