"THESE TWO DO THE SAME THING"

@decorate
def target():
    print('running target()')

def target():
    print('running target()')
target = decorate(target)

# -------------------

def deco(func):
    def inner():
        print('running inner()')
    return inner  

@deco
def target():  
    print('running target()')

target()  
target

def deco(func):
    def inner():
        func()
        print('running inner()')
    return inner  

@deco
def target():  
    print('running target()')

target()

# -----------------------------

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

