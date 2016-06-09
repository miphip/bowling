from rx import Observer


class Dumper(Observer):
    def __init__(self, name):
        self.name = name

    def on_next(self, v):
        print(self.name, 'on_next', repr(v))

    def on_error(self, ex):
        print(self.name, 'on_error', ex),

    def on_completed(self):
        print(self.name, 'on_completed')
