import os, sys, math
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage


def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    Создаёт миниатюры для каждого изображения в каталоге
    :param imgdir:
    :param size:
    :param subdir:
    :return:
    """
    thumbdir =os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)
    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)
            thumbs.append((imgfile, thumbobj))
        else:
            print('making', thumbpath)
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath)
                imgobj.thumbnail(size, Image.ANTIALIAS)
                imgobj.save(thumbpath)
                thumbs.append((imgfile, imgobj))
            except:
                print('Skipping: ', imgpath)
    return thumbs


class ViewOne(Toplevel):
    """
    Открывает одно изображение в новом окне
    :param Toplevel:
    :return:
    """
    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        imgobj = PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width, imgobj.height())
        self.savephoto = imgobj #Важно сохранять ссылку на изображение

def viewer(imgdir, kind=Toplevel, cols=None):
        """
        Создаёт окно с миниатюрами для каталога с изображениями
        :param selfimgdir:
        :param kind:
        :param cols:
        :return:
        """
        win = kind()
        win.title('Viewer: ' + imgdir)

        thumbs = makeThumbs(imgdir)
        if not cols:
            cols = int(math.floor(math.sqrt(len(thumbs))))
        savephotos = []
        while thumbs:
            thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
            row = Frame(win)
            row.pack(fill=BOTH)
            for (imgfile, imgobj) in thumbsrow:
                size = max(imgobj.size)
                photo = PhotoImage(imgobj)
                link = Button(row, image=photo)
                handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
                link.config(command=handler, width=size, height=size, bg='black')
                link.pack(side=LEFT, expand=YES)
                savephotos.append(photo)
        quit = Button(win, text='Quit', command=win.quit, bg='beige')
        quit.pack(fill=X)
        return win, savephotos


if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'imgs'
    main, save = viewer(imgdir, kind=Tk)
    mainloop()
