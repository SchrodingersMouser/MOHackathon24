from tkinter import *

urmom = Tk()

urmom.geometry("1000x1000")
canvas = Canvas(urmom, width=600, height=600)
canvas.pack

canvas.create_line(100,200,200,35, fill="green", width=30)

urmom.mainloop()