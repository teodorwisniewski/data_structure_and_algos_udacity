
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    new_array = []
    remainder = 1
    for number in reversed(arr):
        number += remainder
        if number > 9:
            new_number = number - 10
            new_array.append(new_number)
            remainder = 1
        else:
            new_array.append(number)
            delta_to_add = 0
            remainder = 0
    if remainder:
        new_array.append(remainder)
    return list(reversed(new_array))



if __name__ == "__main__":
    # Test cases
    print(add_one([1, 2, 3]))
    print(add_one([1, 2, 9]))
    print(add_one([1, 9, 9]))
    print(add_one([9, 9, 9]))

