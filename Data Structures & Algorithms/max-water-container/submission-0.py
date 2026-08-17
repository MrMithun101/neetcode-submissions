class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            #width
            width = r-l

            #height
            max_height = min(heights[l], heights[r])

            #max water
            max_water = max(max_water ,width * max_height)

            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
               
        
        return max_water
        

        

        