import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
#
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x2,x1=light_x,initial_tx
y2,y1=light_y,initial_ty
s=''
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if x2==x1 and y2<y1:
        s='N'
        y1=y1-1
    elif x2>x1 and y2<y1:
        s=('NE')
        x1=x1+1
        y1=y1-1
    elif x2>x1 and y2==y1:#3
        s="E"
        x1=x1+1
    elif x2>x1 and y2>y1:#4
        s="SE"
        x1=x1+1
        y1=y1+1
    elif x2==x1 and y2>y1:#5
        s="S"
        y1=y1+1

    elif x2<x1 and y2>y1:#6
        x1=x1-1
        y1=y1+1
        s="SW"
    elif x2<x1 and y2==y1:#7
        x1=x1-1
        s="W"
    elif x2<x1 and y2<y1:#8
         x1=x1-1
         y1=y1-1
         s="NW"
    else:
        break

    print(s)


