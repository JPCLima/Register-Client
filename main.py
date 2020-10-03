from tkinter import *
from tkinter import ttk

root = Tk()

BG_COLOR = '#173F5F'
FRAME_COLOR = '#E0DFD5'
BTN_FONT_BOLD = ('Helvetica', 8, 'bold')
BTN_FONT_NORMAL = ('Helvetica', 8)
BTN_FONT_NORMAL = ('Helvetica', 8)


class Functions():
    def clean_canvas(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.city_entry.delete(0, END)


class Aplication(Functions):

    def __init__(self):
        self.root = root
        self.canvas()
        self.frame_window()
        self.widgets_frame1()
        self.treen_view()
        root.mainloop()

    def canvas(self):
        self.root.title("Sign In new Clients")
        self.root.configure(background=BG_COLOR)
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=400)

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
        self.btn_clean = Button(
            self.frame_1, text=text_label[0], bd=2, font=BTN_FONT_NORMAL, command=self.clean_canvas)
        self.btn_clean.place(relx=0.2, rely=0.1, relwidth=0.1,
                             relheight=0.1)

        # Seach btn
        self.btn_clean = Button(
            self.frame_1, text=text_label[1], bd=2, font=BTN_FONT_NORMAL)
        self.btn_clean.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)

        # New btn
        self.btn_new = Button(
            self.frame_1, text=text_label[2], bd=2, font=BTN_FONT_BOLD)
        self.btn_new.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)

        # Edit btn
        self.btn_edit = Button(
            self.frame_1, text=text_label[3], bd=2,  font=BTN_FONT_NORMAL)
        self.btn_edit.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

        # Delete btn
        self.btn_delete = Button(
            self.frame_1, text=text_label[4], bd=2, font=BTN_FONT_NORMAL)
        self.btn_delete.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)

        # Label and Entry
        # ID - label and entry
        self.label_id = Label(
            self.frame_1, text=text_label[5], bg=FRAME_COLOR)
        self.label_id.place(relx=0.01, rely=0.0, relwidth=0.1)

        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx=0.05, rely=0.1,
                            relwidth=0.1)

        # Name - label and entry
        self.label_name = Label(
            self.frame_1, text=text_label[6], bg=FRAME_COLOR)
        self.label_name.place(relx=0.028, rely=0.3,
                              relwidth=0.1)

        self.name_entry = Entry(self.frame_1)
        self.name_entry.place(relx=0.05, rely=0.4,
                              relwidth=0.7)

        # Phone - label and entry
        self.label_phone = Label(
            self.frame_1, text=text_label[7], bg=FRAME_COLOR)
        self.label_phone.place(relx=0.789, rely=0.3,
                               relwidth=0.15)

        self.phone_entry = Entry(self.frame_1)
        self.phone_entry.place(relx=0.8, rely=0.4,
                               relwidth=0.15)

        # Address - label and entry
        self.label_address = Label(
            self.frame_1, text=text_label[8], bg=FRAME_COLOR)
        self.label_address.place(relx=0.038, rely=0.5,
                                 relwidth=0.1)

        self.address_entry = Entry(self.frame_1)
        self.address_entry.place(relx=0.05, rely=0.6,
                                 relwidth=0.7)

        # City - label and entry
        self.label_city = Label(
            self.frame_1, text=text_label[9], bg=FRAME_COLOR)
        self.label_city.place(relx=0.767, rely=0.5,
                              relwidth=0.1)

        self.city_entry = Entry(self.frame_1)
        self.city_entry.place(relx=0.8, rely=0.6,
                              relwidth=0.15)

    def treen_view(self):

        self.listClients = ttk.Treeview(
            self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        # Create the haeders
        self.listClients.heading('#0', text='')
        self.listClients.heading('#1', text='ID')
        self.listClients.heading('#2', text='Name')
        self.listClients.heading('#3', text='Phone')
        self.listClients.heading('#4', text='Address')
        self.listClients.heading('#5', text='City')

        # Create the With of each column
        self.listClients.column("#0", width=1)
        self.listClients.column("#1", width=50)
        self.listClients.column("#2", width=100)
        self.listClients.column("#3", width=100)
        self.listClients.column("#4", width=100)
        self.listClients.column("#4", width=100)
        self.listClients.column("#5", width=100)

        self.listClients.place(
            relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Create scroll_bar
        self.scroll_bar = Scrollbar(self.frame_2, orient='vertical')
        self.listClients.configure(yscroll=self.scroll_bar.set)
        self.scroll_bar.place(relx=0.96, rely=0.1,
                              relwidth=0.04, relheight=0.85)


Aplication()
