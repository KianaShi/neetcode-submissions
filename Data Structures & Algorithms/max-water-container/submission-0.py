class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        hl = heights[l]
        hr = heights[r]
        m = min(hl, hr)
        result = m * r
        while l < r - 1:
            if hl < hr:
                l += 1
                if heights[l] > hl:
                    w = r - l
                    hl = heights[l]
                    result = max(result, w * min(hl, hr))
            else:
                r -= 1
                if heights[r] > hr:
                    w = r - l
                    hr = heights[r]
                    result = max(result, w * min(hl, hr))
        return result
                    

            
                

                
        