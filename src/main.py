# -*- coding: utf-8 -*-

# Importing requirements
import customtkinter as tk
import ctypes
import time
import sys
import os


# Importing additional files
import views.home_page as viewHome
import views.finance_page as viewFinance
import views.account_page as viewAccount
import views.settings_page as viewSettings

import settings

# Global variables
VERSION = "Runance w1.00.2A"

class MainApp(tk.CTk):
    def __init__(self):
        super().__init__()
        
        try:
            # $Set Windows titlebar icon$
            if sys.platform.startswith('win'):
                self.directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                self.after(200, lambda: self.iconbitmap(os.path.join(self.directory, "assets", "icon", "logo.ico")))

                # $Set the taskbar icon$
                myappid = 'bssdkaDev.Runance' # arbitrary string
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass 
        
        self.initUI()
        
    def initUI(self):
        self.title(VERSION)
        self.geometry("350x550+150+150")
        self.resizable(False, False)
        
        # <---------Down Menu------------>
        down_frame = tk.CTkFrame(self, fg_color="#3F3A46", width=350, height=60).place(x=0, y=490)
        
        self.home_btn = tk.CTkButton(down_frame, width=75, height=40, text="Home", bg_color="#3F3A46", fg_color="#8E48F0", hover_color="#6C489E", 
                                    command=lambda:viewHome.Content(self, width=330, height=470).place(x=10, y=10))
        self.home_btn.place(x=10, y=500)
        
        self.finance_btn = tk.CTkButton(down_frame, width=75, height=40, text="Finance", bg_color="#3F3A46", fg_color="#8E48F0", hover_color="#6C489E",
                                    command=lambda:viewFinance.Content(self, width=330, height=470).place(x=10, y=10))
        self.finance_btn.place(x=95, y=500)

        self.account_btn = tk.CTkButton(down_frame, width=75, height=40, text="Account", bg_color="#3F3A46", fg_color="#8E48F0", hover_color="#6C489E",
                                    command=lambda:viewAccount.Content(self, width=330, height=470).place(x=10, y=10))
        self.account_btn.place(x=180, y=500)
        
        self.settings_btn = tk.CTkButton(down_frame, width=75, height=40, text="Settings", bg_color="#3F3A46", fg_color="#8E48F0", hover_color="#6C489E",
                                    command=lambda:viewSettings.Content(self, width=330, height=470).place(x=10, y=10))
        self.settings_btn.place(x=265, y=500) 

        # # Инициализируем главную страницу
        content = viewHome.Content(self, width=330, height=470)
        content.place(x=10, y=10)

        # Привязываем кнопки к анимации
        self.home_btn.bind('<Enter>', lambda x: (self.animateOn(self.home_btn), self.home_btn.place(x=7.5, y=497.5)))
        self.home_btn.bind('<Leave>', lambda x: (self.animateOff(self.home_btn), self.home_btn.place(x=10, y=500)))
        self.finance_btn.bind('<Enter>', lambda x: (self.animateOn(self.finance_btn), self.finance_btn.place(x=92.5, y=497.5)))
        self.finance_btn.bind('<Leave>', lambda x: (self.animateOff(self.finance_btn), self.finance_btn.place(x=95, y=500)))
        self.account_btn.bind('<Enter>', lambda x: (self.animateOn(self.account_btn), self.account_btn.place(x=177.5, y=497.5)))
        self.account_btn.bind('<Leave>', lambda x: (self.animateOff(self.account_btn), self.account_btn.place(x=180, y=500)))
        self.settings_btn.bind('<Enter>', lambda x: (self.animateOn(self.settings_btn), self.settings_btn.place(x=262.5, y=497.5)))
        self.settings_btn.bind('<Leave>', lambda x: (self.animateOff(self.settings_btn), self.settings_btn.place(x=265, y=500)))

        # # Импорт colorama для отладки
        import colorama as cm
        cm.init()
        print(cm.Fore.GREEN, "Checkpoint passed. The programme has been successfully started", cm.Fore.WHITE)


    def animateOn(self, widget, *args):
        widget.configure(width=80, height=45)
        
    def animateOff(self, widget, *args):
        widget.configure(width=75, height=40)


if __name__ == '__main__':
        app = MainApp()
        app.mainloop()
