from tkinter import *

file = open("soubor.txt", "r")
size = file.readline().split(" ")
rowCount = int(size[0])
columnCount = int(size[1])
print(rowCount)
def generate():
    print("hovno")


win=Tk()
win.geometry("700x500")
frame1 = Frame(win, width=200, height=500,bg="red")
frame1.place(x=0, y=0)
btn1 = Button(frame1, text="Generovat", bg="blue", command=generate)
btn1.place(x=0,y=0)
frame2 = Frame(win, width=500, height=500)
frame2.place(x=200, y=0)
canvas=Canvas(frame2, width=500, height=500, bg="blue")
canvas.pack()







win.mainloop()