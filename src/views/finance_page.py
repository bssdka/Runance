# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        lbl = tk.CTkLabel(self, text="FINANCE PAGE")
        lbl.place(x=60, y=60)
