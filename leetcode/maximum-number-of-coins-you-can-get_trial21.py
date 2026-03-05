class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i = 1
        n = len(piles)//3
        ans = 0
        for j in range(n):
            ans += piles[i]
            i += 2

        return ans