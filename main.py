from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import filedialog as fd


def save(*args):
    source = fd.asksaveasfilename(initialfile='Untitled.png', defaultextension=".png")
    image1.save(f'{source}')


def activate_paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill='black', outline="black", width=0)
    draw.ellipse((x1, y1, x2, y2), fill='black', outline="black", width=0)


root = Tk()
root.resizable(width=False, height=False)

cv = Canvas(root, width=1280, height=720, bg='white')

image1 = PIL.Image.new('RGB', (1280, 720), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', activate_paint)
root.bind("S", save)

cv.pack(expand=1, fill=BOTH)


root.mainloop()