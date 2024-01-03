"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
# Not very optimized / Memory, but good runtime

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        elem = [] 
        # flattened = sum(mat, []) # .join
        # numberElements = len(mat[:]) * len(mat[0][:]) # square matrix
        for i in mat:
            elem += i
        
        if len(elem) == r*c:
            mat = []
            for i in range(0, len(elem), c): # increments of C i / 0 -> 2 -> 4
                mat.append(elem[i:i + c]) # slicing through flattened list
            return mat
        return mat

mat = [[1,2],[3,4]]
r = 1
c = 4
print(Solution().matrixReshape(mat,r,c))

mat = [[1,2],[3,4]]
r = 2
c = 4
print(Solution().matrixReshape(mat,r,c))
