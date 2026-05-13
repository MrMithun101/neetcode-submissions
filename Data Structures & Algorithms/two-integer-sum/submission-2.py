class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_vals = {} #val : index

        for i, val in enumerate(nums):
            diff = target - val

            if diff in seen_vals:
                return [seen_vals[diff], i]
            
            seen_vals[val] = i


        