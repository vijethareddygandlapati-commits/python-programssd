import turtle
polygon=turtle.Turtle()
my_num_side=6
my_side_length=70
my_angle=360.0/my_num_side
for i in range(my_num_side):
    polygon.forward(my_side_length)
    polygon.right(my_angle)
turtle.done()
