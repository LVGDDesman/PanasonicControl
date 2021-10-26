from tkinter import *
import utils.table
from window_test import Window

class Registration_window(Window):
    
    def __init__(self, width, height):
        Window.__init__(self, "Registrating to Camera", width, height)

    def initialize_login(self):
        root = Window.create_window(self)
        Window.create_status_bar(self, root)

        main_frame = Frame(root, width = self.width, height = self.height)
        
        login_text = "Login to Camera" 
        login_label = Label(main_frame, text = login_text, justify=LEFT)
        login_label.pack()
        
        information_label = Label(main_frame)
        information = [("IP-adress", "XX.XX.XX.XX"),("Client-Name", "XXXXX")]

        utils.table.create_table(information_label, information)
        information_label.pack()

        login_label1 = Label(main_frame, text = "Make sure to connect to the camera network first!", fg= "red")
        login_label1.pack()
        
        main_frame.place(in_=root, anchor="c", relx=.5, rely=.5)
        
        root.mainloop()
        return root

a = Registration_window(1920, 1080)
a.initialize_login()
