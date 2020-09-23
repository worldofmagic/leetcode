def maxsubarray(nums):
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    max_sum = nums[0]
    for i in range(n):
        for j in range(i+1, n+1):
            print("sum is {0}, i is {1}, j is {2}".format(sum(nums[i:j]), i, j))
            if max_sum is None or max_sum < sum(nums[i:j]):
                max_sum = sum(nums[i:j])
    return max_sum


nums = [-2,1]
a = maxsubarray(nums)
