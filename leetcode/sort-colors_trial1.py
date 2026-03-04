class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
        
        white = red

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[white], nums[i] = nums[i], nums[white]
                white += 1