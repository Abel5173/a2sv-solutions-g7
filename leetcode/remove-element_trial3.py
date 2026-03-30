class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        f = list(filter(lambda x: x != val, nums))
        k = len(f)

        for i in range(k):
            nums[i] = f[i]

        return k

            