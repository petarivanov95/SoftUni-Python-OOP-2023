# LEGB
# Local scope - ref to vars defined w/n a foo, which are accessible only within that function.
# Enclosing scope consists of any enclosing functions that contain local variables, which can be accessed by inner functions.
# Global scope includes variables defined at the top level of a module or script, which are accessible throughout the entire module.
# Built-in scope contains Python's built-in functions and attributes, which are available in any module or script without importing.


# x = 'global x'

def test1():
    y = 'local y'
    print(y)

# test1() # 'local y'


def test2():
    x = 'local x'
    print(x)

# test2() # 'local x'
# print(x) # 'global x'


def test3():
    global x
    x = 'new local x turned global'
    print(x)

# test3() # 'new local x turned global'
# print(x) # 'new local x turned global'


def outer1():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

# outer1()
# inner x
# outer x


def outer2():
    x = 'outer x'

    def inner():
        print(x)

    inner()
    print(x)

# outer2()
# outer x
# outer x


def outer3():
    x = 'outer x'

    def inner():
        nonlocal x # affects the enclosing scope but not the global
        x = 'inner x'
        print(x)

    inner()
    print(x)

# outer3()
# inner x
# inner x


x = 'global x'
def outer4():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer4()
print(x)
# inner x
# outer x
# global x