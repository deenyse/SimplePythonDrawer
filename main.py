from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import messagebox
from random import *


def save():
    filename = f'image_{randint(0, 10000)}.png'
    image1.save(filename)
    messagebox.showinfo('Сохранение', 'Сохранено под названием %s' % filename)


def activate_paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill='black', outline="black", width=0)
    #draw.ellipse((x1, y1, x2, y2), fill='black', width=0)


root = Tk()
root.resizable(width=False, height=False)

cv = Canvas(root, width=1280, height=720, bg='white')

image1 = PIL.Image.new('RGB', (1280, 720), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', activate_paint)
cv.pack(expand=1, fill=BOTH)

btn_save = Button(text="save", command=save, bg='black', fg='white', font=('Comic Sans MS', 30))
btn_save.pack()

root.mainloop()