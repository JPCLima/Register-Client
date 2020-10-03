from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import sqlite3

root = tix.Tk()

BG_COLOR = '#173F5F'
FRAME_COLOR = '#E0DFD5'
BTN_FONT_BOLD = ('Helvetica', 8, 'bold')
BTN_FONT_NORMAL = ('Helvetica', 8)
BTN_FONT_NORMAL = ('Helvetica', 8)


class Functions():

    def get_variables(self):
        self.id = self.id_entry.get()
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.address = self.address_entry.get()
        self.city = self.city_entry.get()

    def clean_canvas(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.city_entry.delete(0, END)

    def connect_db(self):
        self.conn = sqlite3.connect("clients.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close()

    def create_table(self):
        self.connect_db()
        # Create table
        self.cursor.execute(""" 
                                CREATE TABLE IF NOT EXISTS clients (
                                    id INTEGER PRIMARY KEY,
                                    name_client CHAR(40) NOT NULL,
                                    phone_number INTEGER(20),
                                    address CHAR(40),
                                    city CHAR(40)
                                ); """)
        self.conn.commit()
        self.disconnect_db()

    def add_client(self):

        self.get_variables()

        # Msg box if there is not name
        if self.name_entry.get() == "":
            msg = "To insert a new client \n"
            msg += "you need to enter at least the name"
            messagebox.showinfo("Sign in new Cleint - Warning!!!", msg)
        else:
            self.connect_db()
            self.cursor.execute("""  
                                    INSERT INTO clients 
                                    (name_client, phone_number, address, city)
                                    VALUES (?,?,?,?)""", (self.name, self.phone, self.address, self.city))
            self.conn.commit()
            self.disconnect_db()
            self.select_list()

    def select_list(self):
        # Clean old list
        self.listClients.delete(*self.listClients.get_children())
        # Upadate client list
        self.connect_db()
        list_clients = self.cursor.execute("""  
                                                SELECT id, name_client, phone_number, address, city
                                                FROM clients
                                                ORDER BY name_client ASC;
                                                """)
        for client in list_clients:
            self.listClients.insert("", END, values=client)
        self.disconnect_db()

    def double_click(self, event):
        self.clean_canvas()
        self.listClients.selection()

        for i in self.listClients.selection():
            col1, col2, col3, col4, col5 = self.listClients.item(i, 'values')
            self.id_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.phone_entry.insert(END, col3)
            self.address_entry.insert(END, col4)
            self.city_entry.insert(END, col5)

    def delete_client(self):
        self.get_variables()
        self.connect_db()

        self.cursor.execute(""" 
                                DELETE FROM clients WHERE id = ? """, (self.id))
        self.conn.commit()

        self.disconnect_db()
        self.clean_canvas()
        self.select_list()

    def edit_client(self):
        self.get_variables()
        self.connect_db()

        self.cursor.execute(""" UPDATE clients
                                SET name_client = ?, phone_number=?, address=?, city=? WHERE id = ?  """,
                            (self.name, self.phone, self.address, self.city, self.id))
        self.conn.commit()

        self.disconnect_db()
        self.select_list()
        self.clean_canvas()

    def search_client(self):
        self.connect_db()
        self.listClients.delete(*self.listClients.get_children())
        self.name_entry.insert(END, '%')
        name = self.name_entry.get()

        self.cursor.execute(""" 
                                SELECT id, name_client, phone_number, address, city
                                FROM clients WHERE name_client LIKE '%s' ORDER BY name_client ASC""" % name)

        search_client_name = self.cursor.fetchall()
        for i in search_client_name:
            self.listClients.insert("", END, values=i)

        self.clean_canvas()
        self.disconnect_db()


class Validation():
    def valid_client_id(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100


class Aplication(Functions, Validation):

    def __init__(self):
        self.root = root
        self.validation_entries()
        self.canvas()
        self.frame_window()
        self.widgets_frame1()
        self.treen_view()
        self.select_list()
        root.mainloop()

    def canvas(self):
        self.root.title("Sign In new Clients")
        self.root.configure(background=BG_COLOR)
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=400)
        self.create_table()

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
        self.btn_search = Button(
            self.frame_1, text=text_label[1], bd=2, font=BTN_FONT_NORMAL, command=self.search_client)
        self.btn_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
        # Info msg
        text_msg = "Please enter in the name field the client which you would like to search."
        self.info_msg_search = tix.Balloon(self.frame_1)
        self.info_msg_search.bind_widget(self.btn_search, balloonmsg=text_msg)

        # New btn
        self.btn_new = Button(
            self.frame_1, text=text_label[2], bd=2, font=BTN_FONT_BOLD, command=self.add_client)
        self.btn_new.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)

        # Edit btn
        self.btn_edit = Button(
            self.frame_1, text=text_label[3], bd=2,  font=BTN_FONT_NORMAL, command=self.edit_client)
        self.btn_edit.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

        # Delete btn
        self.btn_delete = Button(
            self.frame_1, text=text_label[4], bd=2, font=BTN_FONT_NORMAL, command=self.delete_client)
        self.btn_delete.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)

        # Label and Entry
        # ID - label and entry
        self.label_id = Label(
            self.frame_1, text=text_label[5], bg=FRAME_COLOR)
        self.label_id.place(relx=0.01, rely=0.0, relwidth=0.1)

        self.id_entry = Entry(self.frame_1, validate="key",
                              validatecommand=self.validate_cmd)
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

        self.listClients.bind("<Double-1>", self.double_click)

    def validation_entries(self):
        self.validate_cmd = (self.root.register(
            self.valid_client_id), '%P')


Aplication()
