from tkinter import *
import utils.table

class Window():
    application_name = "Panasonic WLAN Control"
    version = "0.0.1"
    current_window_name = ""
    width = 0 
    height = 0
    min_width = 0
    min_height = 0

    def __init__(self, current_window_name, width, height,
            min_width = 400, min_height = 300):
        self.current_window_name = current_window_name
        self.width = width
        self.height = height
        self.min_width = min_width
        self.min_height = min_height

    def create_window(self):
        root = Tk()
        root.title(self.application_name + " " + self.version)
        root.geometry(str(self.width) + "x" + str(self.height))
        root.minsize(self.min_width, self.min_height)
        return root

    def create_status_bar(self, root):
        status_bar = Frame(root, bd=1, relief=SUNKEN)
        
        camera_model = Label(status_bar, text="G81 DMC")
        camera_model.pack(side=LEFT, pady=10)
        
        
        execution_mode = Label(status_bar, text="EXECUTING")
        execution_mode.place(relx=.5, rely=.5, anchor="center")

        status = Label(status_bar, text="disconnected")
        status.pack(side=RIGHT, pady=10)

        status_bar.pack(side=TOP, fill=X)
        
        return
