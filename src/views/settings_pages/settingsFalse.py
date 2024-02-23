# -*- coding: utf-8 -*-

import customtkinter as tk

import views.settings.config as config

# Global variables
VERSION = config.dct['VERSION']

class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        
        
        self.initUI(master, width, height)
        
    def initUI(self, *args):
        
        frame = tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        