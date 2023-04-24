file = open("soubor.txt", "r")
size = file.readline().split(" ")
rowCount = int(size[0])
columnCount = int(size[1])

for _ in range(rowCount):
    print(file.readline())

for _ in range(columnCount):
    print(file.readline())
