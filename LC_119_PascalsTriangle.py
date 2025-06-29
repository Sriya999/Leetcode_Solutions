class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        traingle=[]
        #first row
        traingle.append([1])
        for i in range(1,rowIndex+1):
            row=[]
            row.append(1)
            #sum up 2 elements
            for j in range(1,i):
                row.append(traingle[i-1][j-1]+traingle[i-1][j])
            #insert 1 at row end
            row.append(1)
            traingle.append(row)#add this row to traingle
        return traingle[rowIndex]
