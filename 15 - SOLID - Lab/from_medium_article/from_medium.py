
import numpy as np

def math_operations(list_):
    # Compute Average
    print(f"the mean is {np.mean(list_)}")
    # Compute Max
    print(f"the max is {np.max(list_)}")

math_operations(list_ = [1,2,3,4,5])
# the mean is 3.0
# the max is 5



def get_mean(list_):
    '''Compute Mean'''
    print(f"the mean is {np.mean(list_)}")

def get_max(list_):
    '''Compute Max'''
    print(f"the max is {np.max(list_)}")

def main(list_):
    # Compute Average
    get_mean(list_)
    # Compute Max
    get_max(list_)

main([1,2,3,4,5])
# the mean is 3.0
# the max is 5