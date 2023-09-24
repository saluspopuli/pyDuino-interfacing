from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

class GUI:

    root = Tk()
    label = ttk.Label(text="OwO")
    def __init__(self, name):
        style = ThemedStyle(self.root)
        style.set_theme("yaru")

        self.root.title(name)
        self.root.geometry("600x600")

        self.label.place(x = 500,y =300)

    def move_label(self, x, y):
        new_x = int(x)/2
        new_y = int(y)/2
        self.label.place(x=new_x, y=new_y)
        self.root.update()

    def start_gui(self):
        self.root.mainloop()

