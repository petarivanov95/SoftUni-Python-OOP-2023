# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called")
#         func()
#         print("After the function is called")
#
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print("Hello")
#
# hello()
#
#
# def outer():
#     a = 25
#     name = 'Python'
#
#     def inner(prefix):
#         print(prefix, name)
#
#     return inner

def layer_1():
    def layer_2(num2):
        print(num2 * 'Layer 2 ')
        def layer_3(num3):
            print(num3 * 'Layer 3 ')
        return layer_3
    return layer_2


b = layer_1()
c = b(3)
d = c(4)



