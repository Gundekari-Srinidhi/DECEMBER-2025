class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_size=float('inf')
        left=0
        n=len(nums)
        curr_sum=0
        for right in range(n):
            curr_sum+=nums[right]
            while curr_sum>=target:
                window_size=min(window_size,right-left+1)
                curr_sum-=nums[left]
                left+=1
        if window_size!=float('inf'):
            return window_size
        else:
            return 0
        