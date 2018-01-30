"""
Подмешиваемый во фреймы класс;
Реализует общие методы вызова стандартных диалогов,
запуска программ, простых инструментов отображения текста
и т.д.; Метод quit требует, чтобы этот класс подмешивался к классу Frame
( или его производным)
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from scrolledtext import ScrolledText
from launchmodes import PortableLauncher, System


class GuiMixin:
    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        pass

    def help(self):
        self.infobox('RTFM', 'See figure 1...')

    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__ # объект класса экземпляра
        myclass(new, *args) # прикрепить экземпляр к новому классу

    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)()
if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)

        def other(self):
            self.spawn('guimixin.py')
    TestMixin().mainloop()