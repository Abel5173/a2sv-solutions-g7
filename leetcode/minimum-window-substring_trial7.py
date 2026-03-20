class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)
        left = 0

        char_cnt = Counter(t)
        t_char = 0

        min_str = ""
        min_len = float('inf')

        for r in range(size):
            curr = s[r]
            if curr in char_cnt:
                char_cnt[curr] -= 1
                if char_cnt[curr] == 0:
                    t_char += 1
                
            while t_char == len(char_cnt):
                left_char = s[left]
                if left_char in char_cnt:
                    if char_cnt[left_char] == 0:
                        t_char -= 1
                    char_cnt[left_char] += 1
            
                if (r-left+1) < min_len:
                    min_len = (r-left+1)
                    min_str = s[left:left+min_len]
                left += 1
        
        return min_str 