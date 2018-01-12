from tkinter import *
import os, sys
from PIL.ImageTk import PhotoImage

imgdir = '.'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        win = Toplevel()
        win.title(imgfile)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        savephotos.append(imgobj)
    except:
        pass
mainloop()