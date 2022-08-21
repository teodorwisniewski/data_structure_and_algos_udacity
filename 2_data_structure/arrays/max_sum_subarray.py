'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
'''


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    current_sum = arr[0]
    max_sum = arr[0]
    for el in arr[1:]:
        current_sum = max(current_sum + el, el)
        max_sum = max(current_sum, max_sum)

    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    arr = [1, 2, 3, -4, 6]
    solution = 8  # sum of array

    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, -5, -4, 1, 6]
    solution = 7  # sum of last two elements

    test_case = [arr, solution]
    test_function(test_case)

    arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
    solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

    test_case = [arr, solution]
    test_function(test_case)