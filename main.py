from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

pizza = new_matrix()
print_matrix(pizza)

"""
add_edge(pizza, 130, 130, 0, 90, 150, 0)
add_edge(pizza, 50, 150, 0, 130, 130, 0)
add_edge(pizza, 130, 130, 0, 90, 150, 0)
add_edge(pizza, 130, 130, 0, 90, 150, 0)
add_edge(pizza, 130, 130, 0, 90, 150, 0)
"""
p1 = [[4, 4],
      [2, 5],
      [0, 5],
      [0, 6]]

p2 = [[4,4],
      [2,2],
      [20,8],
      [20,10],
      [19,12],
      [18,14],
      [16,16],
      [12,18],
      [7,18],
      [6,17],
      [6,16],
      [0,6],
      [2,6],
      [4,5],
      [4,4]]

p3 = [[10,15],
      [8,15],
      [7,14],
      [7,13],
      [8,12],
      [10,12],
      [11,13],
      [11,14],
      [10,15]]

p4 = [[8,4],
      [7,5],
      [7,6],
      [8,7],
      [10,7],
      [11,6],
      [11,5]]

p5 = [[7,11],
      [5,11],
      [4,10],
      [4,9],
      [5,8],
      [7,8],
      [8,9],
      [8,10],
      [7,11]]

p6 = [[20,8],
      [20,7],
      [2,1],
      [2,2]]

p7 = [[6,16],
      [11,16],
      [14,15],
      [16,13],
      [17,11],
      [18,8],
      [19,8]]

p8 = [[14,11],
      [12,11],
      [11,10],
      [11,9],
      [12,8],
      [14,8],
      [15,9],
      [15,10],
      [14,11]]

def add_connections(p):
    for i in range(len(p)-1):
        add_edge(pizza, p[i][0]*20 + 50, p[i][1]*20 + 50, 0, p[i+1][0]*20 + 50, p[i+1][1]*20 + 50, 0)

add_connections(p1)
add_connections(p2)
add_connections(p3)
add_connections(p4)
add_connections(p5)
add_connections(p6)
add_connections(p7)
add_connections(p8)
        
draw_lines(pizza, screen, color)



#draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
