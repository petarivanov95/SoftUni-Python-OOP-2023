
# solution with functions

num = int(input())

def rhombus_stars(number):
    matrix = []
    for row in range(number * 2 - 1):
        spaces = abs(number - row - 1)
        stars = number - spaces
        row = ' ' * spaces + '* ' * stars
        matrix.append(row)

    return matrix

my_matrix = rhombus_stars(num)
for row in my_matrix:
    print(row)


# # solution with classes
# class Size:

#     def __init__(self):
#         self.size = int(input())  # Prompts the user to enter the size of the rhombus.


# class Rhombus:

#     def __init__(self):
#         self.storage = []  # Initializes an empty list to store the rows of the rhombus.

#     def generate_figure(self, size):
#         for num in range(1, size * 2):
#             row = self.spaces(num, size) + self.stars(num, size)  # Combines spaces and stars to form a row of the rhombus.
#             self.storage.append(row)  # Adds the row to the storage list.

#     @staticmethod
#     def spaces(number, size):
#         return ' ' * abs(number - size)  # Returns a string of spaces that varies in length based on the current row and the size of the rhombus.

#     @staticmethod
#     def stars(number, size):
#         return '* ' * (size - (abs(number - size)))  # Returns a string of stars that varies in length based on the current row and the size of the rhombus.


# class Draw:

#     def __init__(self, data):
#         self.data = data  # Initializes a Draw object with the Rhombus object that contains the rows of the rhombus.

#     def draw_image(self):
#         for row in self.data.storage:
#             print(row)  # Prints each row of the rhombus.


# if __name__ == '__main__':
#     size = Size()  # Prompts the user to enter the size of the rhombus.
#     rhombus = Rhombus()  # Creates a Rhombus object.
#     rhombus.generate_figure(size.size)  # Generates the rows of the rhombus based on the user's input.
#     result = Draw(rhombus)  # Creates a Draw object with the Rhombus object that contains the rows of the rhombus.
#     result.draw_image()  # Prints each row of the rhombus.
