from tkinter import *
app = Tk()
app.title("Project 1 Canvas")
app.geometry("400x400")

def get_x_and_y(event):
    global curx, cury
    curx, cury = event.x, event.y

def draw(event):
    global curx, cury
    canvas.create_line((curx, cury, event.x, event.y), fill='red', width=2)
    curx, cury = event.x, event.y

canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)

app.mainloop()