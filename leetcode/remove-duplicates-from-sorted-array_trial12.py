class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums.sort()
        temp = list(set(nums))
        temp.sort()

        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)