class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.length = len(self.iterable)-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.length >= 0:
            current = self.iterable[self.length]
            self.length -= 1
            return current
        else:
            raise StopIteration
        
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
