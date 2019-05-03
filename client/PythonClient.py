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


def delete(chapter, root):
    def wrapper():
        print("client wrapper")
        client.deleteChapter(chapter)
        root.update()
    return wrapper


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
    # frame = Frame(root, bg='azure3', bd=5)
    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side='right')
    # root.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=root.yview)
    i = 0.15
    for chapter in client.getChapter():
        link = Label(root, text=chapter, fg="grey24", cursor="hand2", background='azure3')
        link.bind("<Button-1>", client.getChapter)
        link.place(relx=0.15, rely=i)
        link.config(font=("Courier", 30))
        buttonDelete = Label(root, text="Удалить", background='azure3', fg='grey20', cursor="hand2", font=("Courier", 20))
        buttonDelete.bind("<Button-2>", delete(chapter, root))
        buttonDelete.place(relx=0.75, rely=i+0.005)
        buttonAdd = Label(root, text="Добавить", background='azure3', fg='grey20', cursor="hand2", font=("Courier", 20))
        buttonAdd.bind("<Button-3>", client.getChapter)
        buttonAdd.place(relx=0.85, rely=i+0.005)
        i += 0.1

    root.mainloop()
    transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))

