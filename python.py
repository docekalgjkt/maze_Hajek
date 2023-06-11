from tkinter import *
import time

file = open("maze.txt", "r")
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
            index = 0
            if int(line[x]) == 1:
                canvas.create_line(10+(x*squareSize),10+(_*squareSize),10+(x*squareSize),10+squareSize+(_*squareSize))
                index =+ 1
            elif int(line[x]) == 2:
                canvas.create_line(10+(x*squareSize),10+(_*squareSize),10+(x*squareSize),10+squareSize+(_*squareSize), fill="red", width=4, tags="finish")

    for y in range(columnCount):
        line = file.readline().strip("\n").split(" ")
        for x in range(len(line)):
            if int(line[x]) == 1:
                canvas.create_line(10+(y*squareSize),10+(x*squareSize),10+squareSize+(y*squareSize),10+(x*squareSize))
            elif int(line[x]) == 2:
                canvas.create_line(10+(y*squareSize),10+(x*squareSize),10+squareSize+(y*squareSize),10+(x*squareSize), fill="red", width=4, tags="finish")

def place():
    canvas.delete("player")
    position = entry.get().split(" ")
    positionX = int(position[0])
    positionY = int(position[1])

    canvas.create_oval(20+(positionX*squareSize),20+(positionY*squareSize),squareSize+(positionX*squareSize),squareSize+(positionY*squareSize), tags="player")


    
def start():
    step = 0.5*squareSize #calculate step size depending on maze size
    generalDirections = ["top", "left", "right", "bottom"]
    mazeSteps = []

    def detectColissions(): #returns true if player collides with another object
        p = canvas.coords('player')
        overlapingList = canvas.find_overlapping(p[0], p[1], p[2], p[3])
        if checkFinish():
            return FALSE
        return len(overlapingList) > 1
    
    def checkFinish(): #checks if user collides with finish line
        finishTag = list(canvas.find_withtag("finish"))[0]
        p = canvas.coords('player')
        return finishTag in canvas.find_overlapping(p[0], p[1], p[2], p[3]) and len(canvas.find_overlapping(p[0], p[1], p[2], p[3])) == 2

    def invertDir(dir):
        if dir == "left":
            return "right"
        if dir == "right":
            return "left"
        if dir == "top":
            return "bottom"
        if dir == "bottom":
            return "top"

    def makeStep(dir): #makes step and check for collison, revert that step on collison
        if dir == "left":
            canvas.move("player",-step,0)
            if detectColissions():
                canvas.move("player",step,0)  
            else:
                mazeSteps.append(dir)
        if dir == "right":
            canvas.move("player",step,0)
            if detectColissions():
               canvas.move("player",-step,0)
            else:
                mazeSteps.append(dir)
        if dir == "top":
            canvas.move("player",0,-step)
            if detectColissions():
                canvas.move("player",0,step) 
            else:
                mazeSteps.append(dir)
        if dir == "bottom":
            canvas.move("player",0,step)
            if detectColissions():
                canvas.move("player",0,-step)
            else:
                mazeSteps.append(dir)

    while checkFinish() == FALSE:
        time.sleep(0.2)
        for i in generalDirections:
           if len(mazeSteps):
                if invertDir(i) != mazeSteps[-1]: #prevent making same steps again
                    makeStep(i)
           else: makeStep(i)
    




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
submitBtn = Button(frame1, text="Start", bg="blue", command=start)
submitBtn.place(x=0,y=90)
frame2 = Frame(win, width=500, height=500)
frame2.place(x=200, y=0)
canvas=Canvas(frame2, width=500, height=500, bg="blue")
canvas.pack()







win.mainloop()