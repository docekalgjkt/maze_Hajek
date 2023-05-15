from tkinter import *

file = open("soubor.txt", "r")
size = file.readline().split(" ")
rowCount = int(size[0])
columnCount = int(size[1])

win=Tk()
win.geometry("700x350")
canvas=Canvas(win, width=700, height=350)
canvas.pack()

for _ in range(rowCount):
    for id, item in enumerate(file.readline().split(" ")):
        num = id+1
        if item:
            canvas.create_line(20,20,20,80)






win.mainloop()