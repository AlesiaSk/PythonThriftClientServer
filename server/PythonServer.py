#!/usr/bin/env python

port = 9090

import sys
sys.path.append('../dataBase')

from dataBase import DataBase

sys.path.append('../gen-py')

from VBScriptTutorial import TutorialService
from VBScriptTutorial.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket


class ServerHandler:

    def __init__(self):
        self.log = {}
        self.db = DataBase()

    def getConstants(self):
        print("getConstants()")

    def getChapter(self):
        self.db.getChapterName()


handler = ServerHandler()
processor = TutorialService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")
