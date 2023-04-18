import threading

class Thread(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self)
        self.target = target
        self.RUN = threading.Event()

    def stop(self):
        self.RUN.set()

    def run(self):
        while self.RUN.is_set() is not True:
            self.target()
