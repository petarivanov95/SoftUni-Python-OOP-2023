class IntegerList:
    def __init__(self, *args):
        self.int_lst = [x for x in args if isinstance(x, int)]

    def add(self, val):
        if not isinstance(val, int):
            raise ValueError
        self.int_lst.append(val)
        return self.int_lst

    def remove_index(self, idx):
        if not 0 <= idx < len(self.int_lst):
            raise IndexError
        return self.int_lst.pop(idx)

    def get(self, idx):
        if not 0 <= idx < len(self.int_lst):
            raise IndexError
        return self.int_lst[idx]

    def insert(self, el, idx):
        if not isinstance(el, int):
            raise ValueError
        if not 0 <= idx < len(self.int_lst):
            raise IndexError

        self.int_lst.insert(idx, el)

    def get_biggest(self):
        return max(self.int_lst)

    def get_index(self, el):
        return self.int_lst.index(el)


