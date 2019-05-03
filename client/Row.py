from tkinter import *
import webbrowser


class Row:

    def __init__(self, root, chapterName, getChapter):
        self.log = {}
        link = Label(root, text=chapterName, fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", self.callback)
        button = Button(command=getChapter(), text="Кнопка")
        button.grid()
        buttonDelete = Button(command=getChapter(), text="Кнопка")
        buttonDelete.grid()

    def callback(event):
        webbrowser.open_new("http://www.google.com")


print(callable(Row))

