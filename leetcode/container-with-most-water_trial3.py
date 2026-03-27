class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_a = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_a = max(max_a, h*w)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_a
