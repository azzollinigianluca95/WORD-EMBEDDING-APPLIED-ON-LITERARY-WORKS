from tkinter import *

frame = None

class LayoutStandard:

    def __init__(self, where):

        self.bg = Frame(where, bg="white", height=100, width=300, padx=10, pady=10) #SFONDO
        self.center = Frame(self.bg, bg="lightblue", height=300, width=300, pady=10, padx=10) #FRAME INTERNO ALLO SFONDO
    
    def unpackCenter(self):
        for widget in self.center.winfo_children():
            widget.destroy()

    