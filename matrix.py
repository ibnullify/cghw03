import math


def print_matrix( matrix ):
    #even though I'd rather print it horizontal (each point is a column) it wouldn't fit on a screen
    for y in range(len(matrix)):
        print "| ",
        for x in range(4):
            #these if statements are just for lining up the numbers
            if (matrix[y][x]) < 10:
                print "  " + str(matrix[y][x]),
            elif (matrix[y][x]) < 100:
                print " " + str(matrix[y][x]),
            else:
                print matrix[y][x],
            #print matrix[y][x],
        print " |"
    
#goes through a matrix and sets the diagonal to 1 and everything else to 0
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #We need to be sure that the columns in m1 is the same as m2
    if len(m1[0]) != len(m2):
        print "You can't multiply these matrices"
        pass
    #Make a new matrix to avoid changing the matrix you're working on because the values will alter mid-calculation
    product = new_matrix( len(m1), len(m2[0]))
    for row in range( len(product) ):
        for col in range( len(product[0]) ):
            for i in range( len(m2) ):
                product[row][col] += m1[row][i] * m2[i][col]
    for row in range( len(product) ):
        for col in range( len(product[0]) ):
            m2[row][col] = product[row][col]

#makes a 4 x 4 matrix with all values 0
def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

'''
c = new_matrix()
print_matrix(c)

c[1][3] = 8
print_matrix(c)

ident(c)
print_matrix(c)
'''
