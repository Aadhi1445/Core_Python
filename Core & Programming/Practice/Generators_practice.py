class Num:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        pass