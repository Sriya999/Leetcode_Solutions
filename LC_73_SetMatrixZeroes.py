class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       """
        Do not return anything, modify matrix in-place instead.
        """
       temp=copy.deepcopy(matrix)#copy to temp
       for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
 
                    #set rows to  zero
                    for k in range(len(matrix[i])):
                        temp[i][k]=0
                    #set cols to zeroes
                    for k in range(len(matrix)):
                        temp[k][j]=0
        #modifing matrix
       for i in range(len(matrix)):
            for j in range(0,len(matrix[i])):
                matrix[i][j]=temp[i][j]

      
        