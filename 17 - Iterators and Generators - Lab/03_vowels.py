class vowels:
    VOWELS = ['a','e','o','i','u','y']
    def __init__(self, string):
        self.string = string
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < len(self.string):
            idx = self.current
            if self.string[idx].lower() in vowels.VOWELS:
                self.current += 1
                return self.string[idx]
            self.current += 1
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
