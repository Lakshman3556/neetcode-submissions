class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row,Cols=len(matrix),len(matrix[0])
        l,r=0,Row*Cols-1
        while l<=r:
            m=l+(r-l)//2
            ro=m//Cols
            co=m%Cols
            if target>matrix[ro][co]:
                l=m+1
            elif target<matrix[ro][co]:
                r=m-1
            else:
                return True
        return False                
        