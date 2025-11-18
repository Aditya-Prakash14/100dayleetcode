class Solution(object):
    def maxSubArray(self, nums):
        cursum = nums[0]
        overallsum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(nums[i], cursum + nums[i])
            overallsum = max(overallsum, cursum)
        return overallsum
