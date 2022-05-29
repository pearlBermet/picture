from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import photo_editor


class GUI:
    def __init__(self, c):
        self.c = c

    def select(self):
        self.img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        self.image = Image.open(self.img_path)
        self.image.thumbnail((550, 600))
        self.image_initial = self.image
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.img

    def filterPhoto(self, filter):
        filter = filters.get()
        self.image = photo_editor.filterImage(self.image_initial, filter)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def resizePhoto(self, size):
        size = resizing.get()
        self.image = photo_editor.resize(self.image, size)
        self.image.thumbnail((550, 600))
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def waterMark(self):
        text = str(entry_text.get())
        self.image = photo_editor.waterMark(self.image, text)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def rotatePhoto(self, angle):
        rotate = int(rotation.get())
        self.image = photo_editor.rotate(self.image, rotate)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def save(self):
        filename = entryFileName.get()
        complete_name = os.path.join('./images', filename+'.png')
        self.image.save(complete_name)


tk = Tk()
tk.geometry("900x700")
tk.title('AUI Photo Editor')
c = Canvas(tk, width=900, height=700)
c.pack()

g = GUI(c)

rotate = Label(tk, text='Rotate: ', font=("ariel 17 bold"))
rotate.place(x=630, y=65)
angles = [0, 45, 90, 180, 270, 360]
rotation = ttk.Combobox(tk, width=13, values=angles, font=('italic'))
rotation.place(x=725, y=67)
rotation.bind("<<ComboboxSelected>>", g.rotatePhoto)

waterMark = Label(tk, text='WaterMark: ', font=("ariel 17 bold"))
waterMark.place(x=245, y=65)
entry_text = Entry(tk, width=25)
entry_text.place(x=380, y=73)
button1 = Button(text='Print', font=('underline'), relief=RAISED, command=g.waterMark)
button1.place(x=535, y=65)

resize = Label(tk, text='Size:', font=("ariel 17 bold"))
resize.place(x=630, y=10)
sizes = ['1920x1080', '1280x720', '1080x1080', '720x720', '640x360']
resizing = ttk.Combobox(tk, width=13, values=sizes, font=('italic'))
resizing.bind("<<ComboboxSelected>>", g.resizePhoto)
resizing.place(x=725, y=14)

filter = Label(tk, text="Filter:", font=("ariel 17 bold"))
filter.place(x=245, y=10)
f = ['NONE', 'BLUR', 'CONTOUR', 'DETAIL', 'EMBOSS', 'EDGE_ENHANCE_MORE', 'FIND_EDGES', 'SHARPEN', 'SMOOTH']
filters = ttk.Combobox(tk, width=23, values=f, font=("italic"))
filters.bind("<<ComboboxSelected>>", g.filterPhoto)
filters.place(x=320, y=14)

select = Button(tk, text='Select image', width=19, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=g.select)
select.place(x=5, y=240)

entryName = Label(tk, text='Save as: ', font=("ariel 12 bold"))
entryName.place(x=1, y=297)
entryFileName = Entry(tk, width=25)
entryFileName.place(x=71, y=300)
save = Button(tk, text='Save', width=19, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=g.save)
save.place(x=5, y=320)

entryName = Label(tk, text='All rights reserved', font=("ariel 10"))
entryName.place(x=550, y=700)

exit = Button(tk, text='Exit', width=19, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=tk.destroy)
exit.place(x=5, y=370)

img = ImageTk.PhotoImage(Image.open("logo/new_aiu_logo.png"))
logo = Label(tk, image=img)
logo.place(x=0, y=0)

tk.mainloop()
