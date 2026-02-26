class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Toarr2 = {v: i for i, v in enumerate(arr2)}

        def customComparator(item):
            if item in arr1Toarr2:
                return (0, arr1Toarr2[item])
            else:
                return (1, item)

        arr1.sort(key=customComparator)
        return arr1