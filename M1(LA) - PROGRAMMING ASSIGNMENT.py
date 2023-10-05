'''
Input file:-

3x6
0 3 -6 6 4 -5
3 -7 8 -5 8 9
3 -9 12 -9 6 15
'''

f = open("input.txt", "r")
row, col = map(int, f.readline().split("x"))
lst = f.readlines()
mat = []
for i in lst:
	temp = list(map(int, i.split()))
	mat.append(temp)

#first make row scalling and row replacement functions

def scale(matrix, curr_r, curr_c, tot_c, scaler): #function for scaling
    for t in range(curr_c, tot_c): matrix[curr_r][t] = matrix[curr_r][t] / scaler
    return matrix

def replacer(matrix, tot_r, tot_c, curr_r, curr_c): #function for row replacement
    for k in range(tot_r): #loop over rows
        '''
        Then, for each row below the current row, it subtracts a multiple of the current 
        row from the row so that the elements in the current column in the other rows become 0. 
        This operation is performed for all the columns in the matrix.
        '''
        if k == curr_r:
            continue
        factor = matrix[k][curr_c]
        for l in range(curr_c, tot_c):
            matrix[k][l] -= factor * matrix[curr_r][l]

    return matrix

def rref(matrix, a, b):
    m = a
    n = b
    curr_row = 0
    for j in range(n): #loop for column
        if curr_row >= m:
            break
        pivot = matrix[curr_row][j] #the leading entry of the current row and current column is made the pivot
        if pivot == 0.0: #checks if pivot element is 0
            for k in range(curr_row+1, m):
                if matrix[k][j] != 0.0: #looks for next non zero pivot row
                    matrix[curr_row], matrix[k] = matrix[k], matrix[curr_row] #swaps the rows
                    pivot = matrix[curr_row][j] #updates the pivot
                    break
        if pivot == 0.0:
            continue #continues the j-th loop

        matrix = scale(matrix, curr_row, j, n, pivot) #makes the leading entry of the row as 1, by scaling the row by 1/pivot

        matrix = replacer(matrix, m, n, curr_row, j)

        curr_row += 1 #move to next row
    return matrix

def isPivot(matrix, a, col_no, x):
    if matrix[x][col_no] == 0: return False
    ch = 0
    for i in range(a):
        if matrix[i][col_no] != 0: ch += 1
    if ch != 1: return False
    else: return True 

mat2 = rref(mat, row, col)

#Following one of the algo to write parametric form which was discussed in lecture
ct = 0 #to avoid index out of range
para = ''
gen_sol = [0 for i in range(col)]
for c in range(col-1):
    if not isPivot(mat2, row, c, ct):
        temp = [0 for _ in range(col)]
        temp[c] = 1
        for j in range(row):
            if mat2[j][c] != 0: temp[j] = -mat2[j][c]
        para += "x" + "_" + str(c+1) + "*" + str(temp) + "+"
        gen_sol[c] = 0
    else:
        gen_sol[c] = mat2[ct][col-1]
        ct+=1
para += str(gen_sol)

print("Solution: ", para)
