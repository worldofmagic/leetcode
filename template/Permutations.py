# Subset
from itertools import combinations, product

def subsethelper(numbers):
    result = []
    for i in range(2, len(numbers)):
        for i in combinations(numbers, i):
            result.append(list(i))
    return result

def subsethelper_with_dup(numbers):
    result = []
    for i in range(2, len(numbers)):
        for i in product(numbers, repeat = i):
            result.append(list(i))
    return result

a = subsethelper_with_dup([1,2,3,4,5])
print(a)