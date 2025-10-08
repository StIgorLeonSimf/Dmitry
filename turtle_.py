from turtle import *

shape('turtle')
colormode(255)
pensize(5)
speed(1)
# color('yellow', 'green')
r = 79
g = 11
b = 49
color((r, g, b))
rf = 143
gf = 14
bf = 77
fillcolor((rf, gf, bf))

# begin_fill()
# for _ in range(3):
#     forward(200)
#     left(120)
# # fd(200)
# # lt(120)
# # fd(200)
# # lt(120)
# end_fill()
#
# # rt(180)
# # penup()
# # fd(250)
# # pendown()
# # rt(180)
#
# penup()
# goto(-250, 0)
# pendown()
#
# for _ in range(3):
#     forward(200)
#     left(120)
# x = 0
# for i in range(200, 99, -50):  # 200, 150, 100
#     begin_fill()
#     for _ in range(3):
#         forward(i)
#         left(120)
#     end_fill()
#     penup()
#     x -= 200
#     goto(x, 0)
#     pendown()
# penup()
# goto(0, 0)
# pendown()


for i in range(100, 24, -25):
    fillcolor(rf, gf, bf)
    for _ in range(8):
        begin_fill()
        circle(i)
        end_fill()
        rt(45)
    rf += 25
    gf += 2
    bf += 15
mainloop()
