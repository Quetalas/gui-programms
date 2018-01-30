""" Текстовый редактор и компонент на Python/tkinter
Используется также в PyMailGui и PyView
Дополнительные возможности:
    + Подсветка синтаксиса
    + Изображения на кнопках
"""

Version = '2.1'
import sys, os

from tkinter import *
from tkinter.filedialog import Open, SaveAs
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor
# from guimaker import *

# общие настройки
try:
    import textConfig
    configs = textConfig.__dict__
    print('Find configs')
except:
    configs = {}
    print('no configs')
