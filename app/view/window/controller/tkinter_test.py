from tkinter import *
import view.utils.table
from view.window.controller import Window
from view.window.controller.MainWindow import MainWindow

class Registration_window(Window):
    
    def __init__(self, width, height):
        super().__init__("Camera Login", width, height)

    def initialize_login(self):
        root = MainWindow().create_window()
        MainWindow().create_status_bar(root)

        main_frame = Frame(root, width = self._width, height = self._height)
        
        login_text = "Login to Camera" 
        login_label = Label(main_frame, text = login_text, justify=LEFT)
        login_label.pack()
        
        information_label = Label(main_frame)
        information = [("IP-adress", "XX.XX.XX.XX"),("Client-Name", "XXXXX")]

        view.utils.table.create_table(information_label, information)
        information_label.pack()

        login_label1 = Label(main_frame, text = "Make sure to connect to the camera network first!", fg= "red")
        login_label1.pack()
        
        main_frame.place(in_=root, anchor="c", relx=.5, rely=.5)
        
        root.mainloop()
        return root


