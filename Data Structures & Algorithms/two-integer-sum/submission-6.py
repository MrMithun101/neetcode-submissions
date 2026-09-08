class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_nums = {}

        for index,value in enumerate(nums):
            diff = target - value
            if diff in seen_nums:
                return [seen_nums[diff],index]
            
            seen_nums[value] = index

        