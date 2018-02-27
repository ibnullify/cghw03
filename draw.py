from display import *
from matrix import *

#goes through a matrix and draws all the lines between points
def draw_lines( matrix, screen, color ):
    #this is in case you have an odd number of points in your matrix
    if (len(matrix) % 2) == 1:
        x = matrix[len(matrix)-1][0]
        y = matrix[len(matrix)-1][0]
        z = matrix[len(matrix)-1][0]
        a = matrix[len(matrix)-1][1]
        matrix.append([x,y,z,a])
    #this iterates through and draws lines connected adjacent points
    i = 0
    while i < len(matrix):
        x0 = matrix[i][0]
        y0 = matrix[i][1]
        x1 = matrix[i+1][0]
        y1 = matrix[i+1][1]
        draw_line(x0, y0, x1, y1, screen, color)
        i += 2 # increment two at a time 

#adds two points to a given matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    #two points make an edge
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

#adds a point to a given matrix
def add_point( matrix, x, y, z=0 ):
    #just adds the point
    #I could've checked for an odd number of points here, but that's done in draw_lines
    matrix.append([x,y,z,1])
   


#my draw_line code is a little long
def draw_line( x0, y0, x1, y1, screen, color ):
    
    
    #find out which of the 4 quadrants it falls under
    dx = x1 - x0
    dy = y1 - y0

    if (dx < 0):
        #limits us to quadrants 1 - 4
        draw_line( x1, y1, x0, y0, screen, color)
        return

    if (dx == 0):
        #vertical line
        draw_vertical( x0, y0, y1, screen, color)
        return

    if (dy == 0):
        #horizontal line
        draw_horizontal( y0, x0, x1, screen, color)
        return

    if (dy > 0):
        if (dx > dy):
            octant = 1
        else:
            octant = 2
    else:
        if (dy*-1 < dx):
            octant = 8
        else:
            octant = 7

    draw(x0, y0, x1, y1, octant, screen, color)


def draw ( x0, y0, x1, y1, octant, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = -1*(x1 - x0)

    #Octant 1 and 5, slope is less than 1 but greater than 0
    if (octant == 1):
        #print "octant 1"
        d = 2*A + B
        #print "outside while"
        while (x <= x1):
            #print "inside while"
            plot(screen, color, x, y)
            #print "plotted"
            if (d > 0):
                y += 1
                d += 2*B
            x += 1
            d += 2*A
        return
    
    #Octant 2 and 6, slope is greater than 1
    if (octant == 2):
        #print "octant 2"
        d = A+2*B
	while (y <= y1):
	    plot(screen, color, x, y)
	    if (d<0):
		x += 1	
		d += 2*A
	    y += 1
	    d += 2*B
    #Octant 3 and 7, slope is less than -1
    if (octant == 7):
        #print "octant 7"
        d = A - 2*B
	while (y >= y1):
	    plot(screen, color, x, y)
	    if (d > 0):
		x += 1
		d += 2*A
	    y -= 1
	    d -= 2*B
    #Octant 4 and 8, slope is less than 0 but greater than -1
    if (octant == 8):
        #print "octant 8"
        d = 2*A - B
	while (x <= x1):
	    plot(screen, color, x, y)
	    if (d < 0):
		y -= 1
		d -= 2*B
	    x += 1
	    d += 2*A

def draw_vertical( x, y0, y1, screen, color):
    for i in range( y1 - y0 ):
        plot(screen, color, x, y0 + i)

def draw_horizontal( y, x0, x1, screen, color):
    for i in range( x1 - x0 ):
        plot(screen, color, x0 + i, y)
