def reverse_text(string):
    end = len(string) - 1 

    while end >= 0:
        yield string[end]
        end -= 1



for char in reverse_text("step"):
    print(char, end='')
