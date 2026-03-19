class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ref = {}
        final = []
        for i in p:
            if i in ref:
                ref[i] += 1
            else:
                ref[i] = 1

        def counter(word, ref):
            check = {}
            for i in word:
                if i not in ref:
                    return False
                if i in check:
                    check[i] += 1
                else:
                    check[i] = 1 
            
            for i in check:
                if check[i] != ref[i]:
                    return False
            
            return True

        i = 0
        j = len(p) - 1

        while i < len(s) and j < len(s):
            if s[j] in ref:
                word = s[i:j+1]
                res = counter(word, ref)
                if res == True:
                    final.append(i)
                i += 1
                j += 1
            else:
                i = j+1
                j = j + len(p)

        return final