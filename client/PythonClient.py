#!/usr/bin/env python

from tkinter import *
from client import Row
import sys

sys.path.append('../gen-py')

from VBScriptTutorial import TutorialService
from VBScriptTutorial.ttypes import *
from VBScriptTutorial.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def delete(chapter):
    def wrapper():
        print("client wrapper")
        client.deleteChapter(chapter)
        root.update()
    return wrapper

def openFullText(chapter):
    window = Toplevel(root)
    text = Text(window, width=20, height=10)
    text.pack(side=LEFT)
    text.insert(END, client.getFullText(chapter))
    scroll = Scrollbar(window, command=text.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scroll.set)

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

    i = 0.15
    eval_link = lambda x: (lambda p: openFullText(x.cget("text")))
    delete_link = lambda x: (lambda p: delete(x.cget("text")))
    for chapter in client.getChapter():
        link = Label(root, text=chapter, fg="grey24", cursor="hand2", background='azure3')
        link.bind("<Button-1>", eval_link(link))
        link.place(relx=0.15, rely=i)
        link.config(font=("Courier", 30))
        buttonDelete = Label(root, text="Удалить", background='azure3', fg='grey13', cursor="hand2", font=("Courier", 20))
        buttonDelete.bind("<Button-2>", delete_link(buttonDelete))
        buttonDelete.place(relx=0.65, rely=i+0.005)
        buttonEdit = Label(root, text="Редактировать", background='azure3', fg='grey13', cursor="hand2", font=("Courier", 20))
        buttonEdit.bind("<Button-3>", client.getChapter)
        buttonEdit.place(relx=0.75, rely=i+0.005)
        i += 0.1
    root.mainloop()
    transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))

