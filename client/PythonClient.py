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
    client.getConstants()

    root = Tk()
    root.geometry("600x300")
    root.title("Thrift Client")
    # listbox = Listbox(root)
    # print(client.getChapter())
    # listbox.insert(END, "")

    # for item in client.getChapter():
    #     listbox.insert(END, item)

    i = 0
    for chapter in client.getChapter():
        link = Label(root, text=chapter, fg="blue", cursor="hand2")
        link.bind("<Button-1>", client.getChapter())
        link.grid(row=i, column=1, columnspan=5)
        button = Button(command=client.getChapter(), text="Удалить")
        button.grid(row=i, column=6)
        buttonDelete = Button(command=client.getChapter(), text="Добавить")
        buttonDelete.grid(row=i, column=7)
        i += 1

    root.mainloop()
    transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))
