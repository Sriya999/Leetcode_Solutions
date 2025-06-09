class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        res=[[0]*n for _ in range(n)] 
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                res[j][n-1-i]=matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=res[i][j]

        
