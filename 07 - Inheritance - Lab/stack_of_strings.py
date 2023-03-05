class Stack:
    
    def __init__(self):
        self.data = []

    def push(self,element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        reversed_list = reversed(self.data)
        reversed_str_list = [str(x) for x in reversed_list]
        final_str = ", ".join(reversed_str_list)
        return f"[{final_str}]"
    
