def binarysearch(nums, target):
    if not sum:
        return -1

    start, end = 0, len(nums)-1
    while start+1 < end:
        # python don't have overflow issue, below is recommended for c/c++/java 
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] == target:
            end = mid
        else:
            end = mid - 1
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1

# 给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。
# 如果目标值不在数组中，则返回[-1, -1]

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        
        if not A:
            return [-1,-1]
        if target < A[0]:
            return [-1,-1]
        if target > A[-1]:
            return [-1,-1]
        
        # write your code here
        start, end = 0, len(A)-1
        res = []
        
        # try find left
        while start+1<end:
            mid = start+(end - start)//2
            if A[mid] == target:
                end = mid
            elif A[mid]> target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            res.append(start)
        elif A[end] == target:
            res.append(end)
        else:
            return [-1,-1]
            
        start, end = 0, len(A)-1
        
        # try find right
        while start+1<end:
            mid = start+(end - start)//2
            if A[mid] == target:
                start = mid
            elif A[mid]< target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            res.append(end)
        elif  A[start] == target:
            res.append(start)
        return res

        