# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

import views.settings_pages.settingsFalse as setP
import views.settings.config as config 

def Content(master, width, height):
    
    tk.CTkFrame(master, fg_color="#3F3A46", width=330, height=470).place(x=10, y=10)
    
    if config.dct['accountisregistered'] is True:
        pass
    
    elif config.dct['accountisregistered'] is False:
        contentx = setP.Content(master, 330, 470)
        
    else:
        pass # error