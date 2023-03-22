def square(x):
    return x * x


# f = square(5)
# print(f) # 25

# f = square
# print(f) # <function square at 0x0000020398F489A0>


def my_map(func, arg_list):
    result = []
    for item in arg_list:
        result.append(func(item))
    return result


# squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares) # [1, 4, 9, 16, 25]

def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger("HOWDY")
log_hi() # Log: HOWDY

