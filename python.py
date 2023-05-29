from tkinter import *

file = open("soubor2.txt", "r")
size = file.readline().split(" ")
rowCount = int(size[0])
columnCount = int(size[1])
squareSize = 480/rowCount
if rowCount < columnCount:
    squareSize = 480/columnCount

def generate():
    for _ in range(rowCount):
        line = file.readline().strip("\n").split(" ")
        for x in range(len(line)):
            if int(line[x]) == 1:
                canvas.create_line(10+(x*squareSize),10+(_*squareSize),10+(x*squareSize),10+squareSize+(_*squareSize))
            elif int(line[x]) == 2:
                canvas.create_line(10+(x*squareSize),10+(_*squareSize),10+(x*squareSize),10+squareSize+(_*squareSize), fill="red", width=4)

    for y in range(columnCount):
        line = file.readline().strip("\n").split(" ")
        for x in range(len(line)):
            if int(line[x]) == 1:
                canvas.create_line(10+(y*squareSize),10+(x*squareSize),10+squareSize+(y*squareSize),10+(x*squareSize))
            elif int(line[x]) == 2:
                canvas.create_line(10+(y*squareSize),10+(x*squareSize),10+squareSize+(y*squareSize),10+(x*squareSize), fill="red", width=4)

def place():
    canvas.delete("player")
    position = entry.get().split(" ")
    positionX = int(position[0])
    positionY = int(position[1])

    canvas.create_oval(20+(positionX*squareSize),20+(positionY*squareSize),squareSize+(positionX*squareSize),squareSize+(positionY*squareSize), tags="player")


win=Tk()
win.geometry("700x500")
frame1 = Frame(win, width=200, height=500,bg="red")
frame1.place(x=0, y=0)
btn1 = Button(frame1, text="Generovat", bg="blue", command=generate)
btn1.place(x=0,y=0)
entry = Entry(frame1)
entry.place(x=0, y=30)
submitBtn = Button(frame1, text="Postavit robota", bg="blue", command=place)
submitBtn.place(x=0,y=60)
frame2 = Frame(win, width=500, height=500)
frame2.place(x=200, y=0)
canvas=Canvas(frame2, width=500, height=500, bg="blue")
canvas.pack()







win.mainloop()