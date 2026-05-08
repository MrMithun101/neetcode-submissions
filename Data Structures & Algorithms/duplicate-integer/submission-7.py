class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #check if there's a duplicate

        seen = []

        for i in nums:
            if i in seen:
                return True
            seen.append(i)
        
        return False

        
        