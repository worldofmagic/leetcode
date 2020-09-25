def mypow(x: float, n: int):
    if n == 0:
        return 1
    elif n > 0:
        temp = n
        res = 1
        while temp > 0:
            res = res * x
            print(res)
            temp -= 1
        return x
    else:
        temp = n
        res = 1/x
        if n == -1:
            return res
        else:
            while temp < 0:
                res = res / x
                temp += 1
            return res


# print(mypow(2.00000,10))

def test(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    i = 0
    j = col-1
    while i < row and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
    print(123)
    return False


matrix = [[1]]
target = 1
test(matrix, target)
