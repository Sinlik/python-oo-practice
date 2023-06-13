"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start):
        self.start = start
        self.original_start = start
    def generate(self):
        self.start += 1
        return self.start
    def reset(self):
        self.start = self.original_start
