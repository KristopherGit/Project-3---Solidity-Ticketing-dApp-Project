# Concert Seat Selection Program GUI

from tkinter import *
root = Tk()

canvas = Canvas(root)
canvas.pack()

polygon = canvas.create_polygon(10, 10, 50, 20, 30, 50, fill="blue")
canvas.create_text(30, 30, text="Click me!", font=("Arial", 14), fill="white")


def on_polygon_click(event):
    print("Button clicked!")


canvas.tag_bind(polygon, "<Button-1>", on_polygon_click)

root.mainloop()
