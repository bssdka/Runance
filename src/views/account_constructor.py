# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

import views.account_pages.sign_page as sign

def Content(master, width, height):
    
    tk.CTkFrame(master, fg_color="#3F3A46", width=330, height=470).place(x=10, y=10)
        
    contentx = sign.Content(master, 330, 470)