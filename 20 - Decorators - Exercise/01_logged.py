def logged(func):
    def wrapper(*args):
        print(f"you called func{args}")
        result = func(*args)
        print(func.__name__)
        print(f'it returned {result}')
    return wrapper

@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))
