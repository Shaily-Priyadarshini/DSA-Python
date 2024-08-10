import copy
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = len(matrix[0])
    newArr = matrix.copy()
    print(newArr)

    def makeRowZero(r):
        # print(r)
        for i in range(m):
            newArr[r][i] = 0
        # print(newArr)
        return

    def makeColZero(c):
        # print(c)
        for i in range(n):
            newArr[i][c] = 0
        # print(newArr)
        return

    for i in range(n):
        for j in range(m):
            # print(matrix[i][j])
            if matrix[i][j] == 0:
                makeRowZero(i)
                makeColZero(j)
    return newArr
# matrix=[[1,1,1],[1,0,1],[1,1,1]]
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
newArr=copy.deepcopy(matrix)
print(newArr)
matrix[0][0]=5
print(matrix)
print(newArr)

# print(setZeroes(matrix))