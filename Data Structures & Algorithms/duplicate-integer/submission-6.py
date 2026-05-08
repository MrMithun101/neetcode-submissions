class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = []

        for i in nums:
            if i in seen:
                return True #There is a Duplicate
            seen.append(i)
        
        else:
            return False #There isn't a Duplicate


        
        