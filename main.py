from tkinter import *

root = Tk()

BG_COLOR = '#173F5F'


class Aplication():

    def __init__(self):
        self.root = root
        self.canvas()
        self.frame_window()
        self.create_btn()
        root.mainloop()

    def canvas(self):
        self.root.title("Sign In new Clients")
        self.root.configure(background=BG_COLOR)
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frame_window(self):
        # Frame 1
        self.frame_1 = Frame(self.root, bd=4, bg='white')
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # Frame 2
        self.frame_2 = Frame(self.root, bd=4, bg='white')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def create_btn(self):
        # Clean btn
        self.btn_clean = Button(self.frame_1, text='Clean')
        self.btn_clean.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)


Aplication()
