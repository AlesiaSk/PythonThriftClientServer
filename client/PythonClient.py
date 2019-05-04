#!/usr/bin/env python

from tkinter import *
import sys

from functools import partial
sys.path.append('../gen-py')

from VBScriptTutorial import TutorialService
from VBScriptTutorial.ttypes import *
from VBScriptTutorial.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def delete(chapter, event):
    print("client wrapper")
    client.deleteChapter(chapter)
    root.update()


def edit(chapter):
    window = Toplevel(root)


def openFullText(chapter):
    print(chapter)
    window = Toplevel(root)
    text = Text(window, width=20, height=10)
    text.pack(side=LEFT)
    text.insert(END, client.getFullText(chapter))
    scroll = Scrollbar(window, command=text.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scroll.set)

def delete_link(item,ev):
    print(item.cget("text"))

try:
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = TutorialService.Client(protocol)

    # Connect!
    transport.open()

    root = Tk()
    root.title("Thrift Client")
    root.state('zoomed')
    root.configure(background='azure3')
    menu = Menu(root)
    menu.add_command(label="Открыть")
    menu.add_command(label="Новый")
    menu.add_command(label="Редактировать")
    menu.add_command(label="Удалить")
    root.config(menu=menu)
    lbox = Listbox(selectmode=EXTENDED, width=100)
    addButton = Button(root, text="Add", width=15, height=2)
    addButton.pack(side=LEFT, padx=10, pady=10)
    deleteButton = Button(root, text="Delete", command=partial(delete, lbox.get(ACTIVE)), width=15, height=2)
    deleteButton.pack(side=LEFT, padx=10, pady=10)
    openButton = Button(root, text="Open", command=partial(openFullText, lbox.get(ACTIVE)), width=15, height=2)
    openButton.pack(side=LEFT, padx=10, pady=10)
    editButton = Button(root, text="Edit", width=15, height=2)
    editButton.pack(side=LEFT, padx=10, pady=10)
    lbox.pack(side=LEFT, fill=Y)
    scroll = Scrollbar(command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)
    lbox.config(yscrollcommand=scroll.set)


    i = 0.15
    eval_link = lambda x: (lambda p: openFullText(x.cget("text")))

    for chapter in client.getChapter():
        # link = Label(root, text=chapter, fg="grey24", cursor="hand2", background='azure3', font=("Courier", 30))
        # link.bind("<Button-1>", eval_link(link))
        lbox.insert(0, chapter)
        # buttonDelete = Label(root, text="Удалить", background='azure3', fg='grey13',
        #                      cursor="hand2", font=("Courier", 20))
        #
        # buttonDelete.bind("<Button-1>", partial(delete_link, link))
        # buttonDelete.place(relx=0.65, rely=i+0.005)
        # buttonEdit = Label(root, text="Редактировать", background='azure3', fg='grey13',
        #                    cursor="hand2", font=("Courier", 20))
        # buttonEdit.bind("<Button-1>", link)
        # buttonEdit.place(relx=0.75, rely=i+0.005)
        # i += 0.1
    root.mainloop()
    transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))

