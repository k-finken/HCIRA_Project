from tkinter import *
app = Tk()
app.title("Project 1 Canvas")
app.geometry("400x400")

x_pos = []
y_pos = []

def clear(event):
    canvas.delete('all')
    # Clear path list
    x_pos.clear()
    y_pos.clear()
    # print(x_pos)

def get_x_and_y(event):
    global curx, cury
    curx, cury = event.x, event.y

def draw(event):
    global curx, cury
    canvas.create_line((curx, cury, event.x, event.y), fill='red', width=2)
    curx, cury = event.x, event.y
    # Store location of path
    x_pos.append(curx)
    y_pos.append(cury)
    # print(x_pos)

canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<Tab>", clear)

app.mainloop()