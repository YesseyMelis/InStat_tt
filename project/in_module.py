from out_module import OutModule


class InModule:

    def __init__(self):
        self.i = iter(OutModule())

    def __repr__(self):
        return str(next(self.i))
