class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for j in range(i+1,len(nums)):
                if v+nums[j] == target:
                    return [i,j]