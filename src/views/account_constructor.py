# -*- coding: utf-8 -*-

import customtkinter as tk
# bg-color #3F3A46

import views.settings.config as config
import views.account_functions.signup_page as signupLoad
import views.account_functions.accountIsTrue as accountIsTrue

class Content(tk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        self.initUI(master, width, height)

    def initUI(self, master, width, height):

        tk.CTkFrame(self, fg_color="#3F3A46", width=330, height=470).place(x=0, y=0)
        
        if config.dct['user_activated'] is True:
            pass
        elif config.dct['user_activated'] is False:
            contentx = signupLoad.ContentAccount(self, 330, 470)
            contentx.place(x=10, y=10)
        else:
            print('Syntax error (src/views/settings/config.py {line 8})')