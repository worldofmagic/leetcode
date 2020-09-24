def mypow(x: float, n: int):
    if n == 0:
        return 1
    elif n > 0:
        temp = n
        res = 1
        while temp > 0 :
            res = res * x
            print(res)
            temp -=1
        return x
    else :
        temp = n
        res = 1/x
        if n == -1:
            return res
        else:
            while temp < 0:
                res = res / x
                temp += 1
            return res



print(mypow(2.00000,10))