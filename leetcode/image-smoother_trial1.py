class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                t, cnt = 0, 0

                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        x, y = r+i, c+j
                        if 0 <= x < rows and 0 <= y < cols:
                            t += img[x][y]
                            cnt += 1
                
                res[r][c] = t//cnt
        
        return res


