class ReplayCache:
    def __init__(self):
        self.used=set()
    def seen(self,n):
        return n in self.used
    def mark(self,n):
        self.used.add(n)
