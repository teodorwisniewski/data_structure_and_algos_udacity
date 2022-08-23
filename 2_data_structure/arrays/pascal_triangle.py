

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]


    output_row = [1]

    for i in range(1, n+1):

        previous_row = output_row
        output_row = [1]

        for j in range(1, i):

            num = previous_row[j] + previous_row[j-1]
            output_row.append(num)

        output_row.append(1)

    return output_row


if __name__ == "__main__":

    l0 = nth_row_pascal(0)
    assert [1] == l0

    l1 = nth_row_pascal(1)
    assert [1, 1] == l1

    l2 = nth_row_pascal(2)
    assert [1, 2, 1] == l2

    l3 = nth_row_pascal(3)
    assert [1, 3, 3, 1] == l3

    l4 = nth_row_pascal(4)
    assert [1, 4, 6, 4, 1] == l4

    l4 = nth_row_pascal(5)
    assert [1, 5, 10, 10, 5, 1] == l4