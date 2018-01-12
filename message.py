from tkinter import *
from quitter import Quitter

def fetch():
    print('Input => {0}'.format(ent.get()))


ent = Entry()
ent.insert(0,'type words here')
ent.pack(side=TOP, fill=X)

ent.focus()

ent.bind('<Return>', (lambda event: fetch()))
btn = Button(text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter().pack(side=RIGHT)
mainloop()