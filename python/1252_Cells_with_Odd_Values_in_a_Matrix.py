class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [ [0]*n for i in range(m)]
        c=0
        for i in indices:
            a=i[0]
            b=i[1]
            for j in range(n):
                mat[a][j]+=1
            for k in range(m):
                mat[k][b]+=1
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2!=0:
                    c+=1
        return c