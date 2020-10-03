from tkinter import *

root = Tk()

BG_COLOR = '#173F5F'
FRAME_COLOR = '#E0DFD5'


class Aplication():

    def __init__(self):
        self.root = root
        self.canvas()
        self.frame_window()
        self.widgets_frame1()
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
        self.frame_1 = Frame(self.root, bd=4, bg=FRAME_COLOR)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # Frame 2
        self.frame_2 = Frame(self.root, bd=4, bg='white')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):

        text_label = ['Clean', 'Seach', 'New', 'Edit',
                      'Delete', 'ID', 'Name', 'Phone number', 'Address', 'City']

        # Clean btn
        self.btn_clean = Button(self.frame_1, text=text_label[0], bd=2)
        self.btn_clean.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)

        # Seach btn
        self.btn_clean = Button(self.frame_1, text=text_label[1], bd=2)
        self.btn_clean.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)

        # New btn
        self.btn_clean = Button(self.frame_1, text=text_label[2], bd=2)
        self.btn_clean.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)

        # Edit btn
        self.btn_clean = Button(self.frame_1, text=text_label[3], bd=2)
        self.btn_clean.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

        # Delete btn
        self.btn_clean = Button(self.frame_1, text=text_label[4], bd=2)
        self.btn_clean.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)

        # ID - label and entry
        self.label_name = Label(self.frame_1, text=text_label[5])
        self.label_name.place(relx=0.05, rely=0.0, relwidth=0.1)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.05, rely=0.1,
                              relwidth=0.1)

        # Name - label and entry
        self.label_name = Label(self.frame_1, text=text_label[6])
        self.label_name.place(relx=0.05, rely=0.3,
                              relwidth=0.1)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.05, rely=0.4,
                              relwidth=0.7)

        # Phone - label and entry
        self.label_name = Label(self.frame_1, text=text_label[7])
        self.label_name.place(relx=0.8, rely=0.3,
                              relwidth=0.15)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.8, rely=0.4,
                              relwidth=0.15)

        # Address - label and entry
        self.label_name = Label(self.frame_1, text=text_label[8])
        self.label_name.place(relx=0.05, rely=0.5,
                              relwidth=0.1)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.05, rely=0.6,
                              relwidth=0.7)

        # City - label and entry
        self.label_name = Label(self.frame_1, text=text_label[9])
        self.label_name.place(relx=0.8, rely=0.5,
                              relwidth=0.1)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.8, rely=0.6,
                              relwidth=0.15)


Aplication()
