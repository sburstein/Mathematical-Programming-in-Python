class Matrix:
    def __init__(self, dimensions = None, matrixData = None): #rows, cols, dimensions, m,n
        


        if dimensions is None and matrixData is None:
           raise ValueError ("Neither dimensions nor matrixData were passed as input in function call.")
        

        if matrixData is not None:
            self.mat = matrixData

            '''
            for row in range(len(matrixData)):
                for column in range(len(matrixData[0])):
                    mat[row][column] = matrixData[row][column]
            '''
        
        elif dimensions is not None:
            
            self.m = dimensions[0] # m = rows
            self.n = dimensions[1] # n = columns
            
            self.mat = [[0]*self.n for row in range(self.m)]


        self.numRows = len(self.mat)
        self.numCols = len(self.mat[0])

        
    def __getitem__(self, position):
        
        j = position[0]
        k = position[1]
        
        return self.mat[j][k]


    def __setitem__(self, position, val):

        j = position[0]
        k = position[1]

        self.mat[j][k] = val
        return self.mat

    def __add__(self, otherMat):

        numRows = self.numRows
        numCols = self.numCols

        retMat = [[0]*numCols for row in range(numRows)]
        for row in range(numRows):
            for col in range(numCols):
                retMat[row][col] = self.mat[row][col] + otherMat.mat[row][col]
        return Matrix(matrixData = retMat)

    def __sub__(self, otherMat):

        numRows = self.numRows
        numCols = self.numCols

        retMat = [[0]*numCols for row in range(numRows)]
        for row in range(numRows):
            for col in range(numCols):
                retMat[row][col] = self.mat[row][col] - otherMat.mat[row][col]
        return Matrix(matrixData = retMat)

    def __iadd__(self, otherMat):
        
        numRows = self.numRows
        numCols = self.numCols

        for row in range(numRows):
            for col in range(numCols):
                self.mat[row][col] = self.mat[row][col] + otherMat.mat[row][col]
        return self


    def __eq__(self, otherMat):
        return (self.mat == otherMat.mat)        

    
    def __str__(self):

        return '\n'.join([' '.join([str(self[row, col]) for col in range(self.numCols)]) for row in range(self.numRows)])
        
    '''
    def __repr__(self):
        return str(self.mat)
    '''

    @classmethod


    def size(self):
        
        numRows = self.numRows
        numCols = self.numCols

        return (numRows, numCols)
    
    def deepcopy(self):

        numRows = self.numRows
        numCols = self.numCols
        newMat = Matrix(dimensions = (numRows, numCols))

        for row in range(numRows):
            for col in range(numCols):
                newMat.mat[row][col] = self.mat[row][col]

        return newMat
    
    #def dot(mat, other):
        


        


if __name__ == "__main__":
    
    print("\ndimensions Input Test:\n")
    dimTest = Matrix((4,4))
    print(dimTest)

    print("\nmatrixData Input Test:\n")
    a_mat = Matrix(matrixData = [
    [0,3,2,1], 
    [4,0,2,5],
    [8,2,0,2],
    [0,1,2,0]
    ])
    print(a_mat)
  
    print("\ndeepcopy Test:\n")
    print("~original 'a_mat' matrix~\n")
    print(a_mat)
    c_mat = a_mat.deepcopy()
    c_mat[0,0] = 9
    print("\n~deepcopy 'c_mat' matrix~\n")
    print("~w/ (0,0) value changed to 9~\n")
    print(c_mat)
    print("\nthis indicates deepcopy works since a_mat (0,0) value did not change.\n")


    #initializing second matrix for other tests.
    b_mat = Matrix(matrixData = [
    [0,3,2,1], 
    [4,0,7,4],
    [1,2,0,2],
    [0,1,2,0]
    ])
    
    print("__iadd__ += Test:\n")
    print("Matrix a_mat:\n")
    print(a_mat)
    print("\nMatrix b_mat:\n")
    print(b_mat)

    a_mat += b_mat
    print("\nMatrix a_mat += b_mat:\n")
    print(a_mat)

    d_mat = Matrix(matrixData = [
    [7,2,6,1], 
    [4,0,7,2],
    [9,6,0,2],
    [0,2,5,8]
    ])

    e_mat = Matrix(matrixData = [
    [1,1,0,1], 
    [3,0,1,1],
    [0,2,0,2],
    [0,1,3,1]
    ])

    print("\nMatrix d_mat:\n")
    print(d_mat) 
    print("\nMatrix e_mat:\n")
    print(e_mat)

    print("\n__add__ Test (d_mat + e_mat):\n")
    add_mat = d_mat + e_mat
    print(add_mat)

    print("\n__sub__ Test (d_mat - e_mat):\n")
    sub_mat = d_mat - e_mat
    print(sub_mat)

    print("\n__getitem__ Test:")
    print("\ngetitem (3,3) from d_mat = 8\n")
    print(d_mat[3,3])


    print("\n__setitem__ Test:")
    print("\ngetitem (0,0) from d_mat to 1 (was 7)\n")
    d_mat[0,0] = 1
    print(d_mat)

    #print("\nsize Test:")
    #print("\size of d_mat = (4,4)")
    #d_mat_size = d_mat.size()
    #print(d_mat_size)
    #error in size code....

    print("\n__eq__ Test:")
    print("\nd_mat == e_mat --> FALSE\n")
    eq_check1 = d_mat == e_mat
    print(eq_check1)

    print("\nd_mat == d_mat --> TRUE\n")
    eq_check2 = d_mat == d_mat
    print(eq_check2)










  
    



