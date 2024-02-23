# -*- coding: utf-8 -*-

import customtkinter as tk
from PIL import Image
import webbrowser
import time
import os
# bg-color #3F3A46


class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        
        # !Initialising images
        self.directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.searchImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "search.png")))
        self.marketplacesImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "marketplace.png")), size=(30, 30))
        self.supermarketsImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "supermarkets.png")), size=(30, 30))
        self.entertainmentsImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "entertainments.png")), size=(30, 30))
        self.miscellaneousImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "miscellaneous.png")), size=(30, 30))
        self.githubImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "github.png")), size=(30, 30))
        
        # ! Selection of random images for labels
        self.notfoundImg = tk.CTkImage(light_image=Image.open(os.path.join(self.directory, "assets", "images", "current_news", "not_found.png")), size=(100, 100))
        
        self.initUI(master, width, height)
    
        
    def initUI(self, master, width, height):
        
        tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        # !Выстраиваем все виджеты и описываем логику их работы
        tk.CTkLabel(self, text='Welcome to Runance', font=("Verdana", 20, "bold")).place(x=15, y=15)
        self.searchEntry = tk.CTkEntry(self, placeholder_text="Search", corner_radius=10, width=230, height=40).place(x=25, y=50)
        self.searchBtn = tk.CTkButton(self, text="", image=self.searchImg, width=40, height=40, corner_radius=8, fg_color="#8E48F0", hover_color="#9364f2", command=self.runSearch, border_color='white', border_width=2).place(x=260, y=50)
        
        tk.CTkLabel(self, text="Your spending categories", font=("Verdana", 15, "bold")).place(x=15, y=100)
        self.marketplaces_btn = tk.CTkButton(self, text="", width=50, height=50, corner_radius=10, border_color='white', fg_color="#8E48F0", hover_color="#9364f2", image=self.marketplacesImg, border_width=2).place(x=10, y=130)
        self.supermarkets_btn = tk.CTkButton(self, text="", width=50, height=50, corner_radius=10, border_color='white', fg_color="#8E48F0", hover_color="#9364f2", image=self.supermarketsImg, border_width=2).place(x=75, y=130)
        self.entertainments_btn = tk.CTkButton(self, text="", width=50, height=50, corner_radius=10, border_color='white', fg_color="#8E48F0", hover_color="#9364f2", image=self.entertainmentsImg, border_width=2).place(x=140, y=130)
        self.miscellaneous_btn = tk.CTkButton(self, text="", width=50, height=50, corner_radius=10, border_color='white', fg_color="#8E48F0", hover_color="#9364f2", image=self.miscellaneousImg, border_width=2).place(x=205, y=130)
        self.githubLink_btn = tk.CTkButton(self, text="", width=50, height=50, corner_radius=10, border_color='white', fg_color="#8E48F0", hover_color="#9364f2", image=self.githubImg, border_width=2, command=lambda: webbrowser.open("https://github.com/bssdka")).place(x=270, y=130)
        
        tk.CTkLabel(self, text="Interesting...", font=("Verdana", 15, "bold")).place(x=15, y=200)
        news1 = tk.CTkButton(self, width=150, height=150, text="", image=self.notfoundImg, corner_radius=20, border_color="white", border_width=2).place(x=10, y=240)
        news2 = tk.CTkButton(self, width=150, height=150, text="", image=self.notfoundImg, corner_radius=20, border_color="white", border_width=2).place(x=170, y=240)
        
        # !Применяем одинаковые конфиги ко всем виджетам
        for widget in self.winfo_children():
            widget.configure(bg_color="#3F3A46")
            
            
    def runSearch(self):
        print("successfully")
                