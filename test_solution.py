import solution
"""Acceptance tests
● Test 1:
○ board: [4, 3]
○ snake: [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
○ depth: 3
Result: 7
● Test 2:
○ board: [2, 3]
○ snake: [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
○ depth: 10
Result: 1
● Test 3:
○ board: [10, 10]
○ snake: [[5,5], [5,4], [4,4], [4,5]]
○ depth: 4
Result: 81"""


def test_numberOfAvailableDifferentPaths_1():
    board = [4, 3]
    snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth = 3
    result = 7

    actual = solution.numberOfAvailableDifferentPaths(board,snake,depth)
    expected = result

    message = f"The actual value is {actual} and the expected value is {expected}"
    assert actual is expected, message


def test_numberOfAvailableDifferentPaths_2():
    board = [2, 3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth = 10
    result = 1

    actual = solution.numberOfAvailableDifferentPaths(board, snake, depth)
    expected = result

    message = f"The actual value is {actual} and the expected value is {expected}"
    assert actual is expected, message


def test_numberOfAvailableDifferentPaths_3():
    board = [10, 10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    depth = 4
    result = 81

    actual = solution.numberOfAvailableDifferentPaths(board, snake, depth)
    expected = result

    message = f"The actual value is {actual} and the expected value is {expected}"
    assert actual is expected, message


if __name__ == '__main__':

    try:
        test_numberOfAvailableDifferentPaths_1()
        test_numberOfAvailableDifferentPaths_2()
        test_numberOfAvailableDifferentPaths_3()
    except AssertionError:
        raise

