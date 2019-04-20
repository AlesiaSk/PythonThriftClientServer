#!/usr/bin/env python

from tkinter import *

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
    root.title("First Tkinter Window")
    button = Button(command=client.getChapter(), text=u"Спрятать/показать")
    button.grid()
    root.mainloop()

    transport.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))
