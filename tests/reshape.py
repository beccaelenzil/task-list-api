def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    rows = len(matrix)
    columns = len(matrix[0])
    if rows*columns != r*c:
        return matrix
    count = 0   
    reshaped_matrix = []
    #reshaped_matrix = [[0]*c for i in range(r)]
    for row_index in range(r):
        reshaped_matrix.append([])
        for col_index in range(c):
            row = count // columns
            col = count % columns
            reshaped_matrix[row_index].append(matrix[row][col])
            count += 1
    return(reshaped_matrix)

print(reshape_matrix([[1,2,3],[4,5,6]], 3, 2))