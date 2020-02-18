class SquareIterator:
    def __init__(self,start,end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        resume = self.current ** 2
        self.current += 1
        return resume

for num in SquareIterator(1,4):
    print(num)