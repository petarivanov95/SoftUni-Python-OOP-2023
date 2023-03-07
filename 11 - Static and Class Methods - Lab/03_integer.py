class Integer:
    def __init__(self, value):
        self.value = value

    # Class method to create an Integer object from a float value
    @classmethod
    def from_float(cls, float_value):
        # Check if the input value is a float
        if isinstance(float_value, float):
            # Convert the float to an int and create a new Integer object
            return cls(int(float_value))
        else:
            # Return an error message if the input is not a float
            return "value is not a float"
        
    # Class method to create an Integer object from a Roman numeral string
    @classmethod
    def from_roman(cls, value):
        # Dictionary to store Roman numeral values
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0

        # Loop through each character in the input string
        for i in range(len(value)):
            # If the current character is larger than the previous one, subtract twice the previous value
            if i != 0 and rom_val[value[i]] > rom_val[value[i-1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                # Otherwise, add the current value to the running total
                int_val += rom_val[value[i]] 

        # Create a new Integer object with the calculated integer value
        return cls(int_val)

    # Class method to create an Integer object from a string value
    @classmethod
    def from_string(cls, value):
        # Check if the input value is a string
        if not isinstance(value, str):
            # Return an error message if the input is not a string
            return f"wrong type"

        # Convert the string to an int and create a new Integer object
        return cls(int(value))


# Create a new Integer object with value 10 using the standard constructor
first_num = Integer(10)
print(first_num.value)

# Create a new Integer object with value 4 using the from_roman class method
second_num = Integer.from_roman("IV")
print(second_num.value)

# Try to create an Integer object from a float value
print(Integer.from_float("2.6"))

# Try to create an Integer object from a non-string value
print(Integer.from_string(2.6))