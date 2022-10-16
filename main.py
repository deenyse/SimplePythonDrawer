from PIL import Image, ImageDraw
from tkinter import filedialog as fd
from tkinter import Tk, Canvas, BOTH

def saveImage(*args):
    pathToSave = fd.asksaveasfilename(initialfile='Untitled.png', defaultextension=".png")
    pillowImage.save(pathToSave)

def drawPoint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill='black', outline="black", width=0)
    draw.ellipse((x1, y1, x2, y2), fill='black', outline="black", width=0)


root = Tk()
root.resizable(width=False, height=False)

cv = Canvas(root, width=1280, height=720, bg='white')

pillowImage = Image.new('RGB', (1280, 720), 'white')
draw = ImageDraw.Draw(pillowImage)

cv.bind('<B1-Motion>', drawPoint)
cv.bind('<ButtonRelease-1>', drawPoint)
root.bind("S", saveImage)

cv.pack(expand=1, fill=BOTH)


root.mainloop()