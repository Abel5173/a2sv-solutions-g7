class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        
        for i in range(n, 1, -1):
            maxIndex = arr.index(max(arr[:i]))
            if maxIndex == (i - 1):
                continue
            if maxIndex != 0:
                arr[:maxIndex + 1] = reversed(arr[:maxIndex + 1])
                res.append(maxIndex + 1)
            
            arr[:i] = reversed(arr[:i])
            res.append(i)
        return res
