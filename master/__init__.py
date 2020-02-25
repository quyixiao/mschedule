import zerorpc
import threading
from .config import MASTERURL
from .cm import ConnectionManager


class Master:
    def __init__(self):
        self.server = zerorpc.Server(ConnectionManager())

    def start(self):
        self.server.bind(MASTERURL)
        self.server.run()

    def shutdown(self):
        self.server.close()
