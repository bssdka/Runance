# Importing libraries
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__ini__()
        
        self.iniUI()
        
    def initUI(self):
        print("Hello, world!")
        

if __name__ == '__main__':
    app = App()
    app.mainloop()