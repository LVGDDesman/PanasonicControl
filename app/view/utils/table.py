from tkinter import *

def create_table(root, data, colour = "white"):
    rows = len(data)
    columns = len(data[0])

    for i in range(rows):
        for j in range(columns):
            cell = Entry(root, width = 20, fg = colour)
            cell.grid(row=i, column=j)
            cell.insert(END, data[i][j])
    return
