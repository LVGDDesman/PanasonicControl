from tkinter import *

# Move to model...
width = 1200
height = 1080

min_width = 400
min_height = 300

application_name = "Panasonic Control"
current_window_name = "Login"

# Topdbar settings
top_width = width
top_height = 20

# Sidebar settings
left_width = 50
left_min_width = 20
left_height = height

# Login settings
login_width = 200
login_height = 100
login_text = "Login to Camera" 


def initialize_login():
    root = Tk()
    root.geometry(str(width) + "x" + str(height))
    root.minsize(min_width, min_height)
    
    main_frame = Frame(root, width = login_width, height = login_height, bg = "grey")
    
    login_label = Label(main_frame, text = login_text, bg= "grey")
    login_label.pack()
    
    main_frame.place(in_=root, anchor="c", relx=.5, rely=.5)
    
    root.title(application_name)
    root.mainloop()
    return root

def initialize_mainview():
    root = Tk()
    root.geometry(str(width) + "x" + str(height))
    root.minsize(min_width, min_height)
    
    main_frame = Frame(root)
    main_frame.pack()
     
    left_frame = Frame(root, width = left_width, height = left_height)
    left_frame.pack(side=LEFT)
     
    top_frame = Frame(root,  bg="grey", width = top_width, height = top_height)
    top_frame.pack(side=TOP)
     
    label = Label(main_frame, text = current_window_name)
    label.pack()
     
    root.title(application_name)
    root.mainloop()
    return root

initialize_login()
