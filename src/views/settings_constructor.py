# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

import views.settings_pages.settingsFalse as set1
import views.settings_pages.settingsTrue as set2
import views.settings.config as config 

def Content(master, width, height):
    
    tk.CTkFrame(master, fg_color="#3F3A46", width=330, height=470).place(x=10, y=10)
    
    if config.dct['accountisregistered'] is True:
        contentx = set2.Content(master, 330, 470)
    
    elif config.dct['accountisregistered'] is False:
        contentx = set1.Content(master, 330, 470)
        
    else:
        pass # error