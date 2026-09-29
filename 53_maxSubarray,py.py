class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = nums[0]
        sum = nums[0]
        
        for num in nums[1:]:
            cur = max(num, cur + num)
            sum = max(sum, cur)
        
        return sum