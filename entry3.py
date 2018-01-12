from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'


def fetch(vars):
    for v in vars:
        print('Input => "%s"' % v.get())


def makeform(root,field):
    form = Frame(root)
    left = Frame(form)
    rite = Frame(form)
    form.pack(fill=X, expand=YES)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)

    vars = []
    for field in fields:
        lab = Label(left, width=5, text=field)
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        vars.append(var)
    return vars


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root,text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()