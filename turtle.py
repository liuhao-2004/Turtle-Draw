import turtle as t
import math
import random

x, y = 35 * math.cos(10) - 4, 313 + (35 * math.sin(10))
x_y = [[0, 300], [0, 250], [x - 1, 165], [x + 18, 120], [15, 40],
       [-500, -240], [x + 25, 220], [x + 30, 200], [x + 30, 170], [x - 23, 205],
       [x - 15, 185], [x, 165], [50, 300]]
# [-400, -230]
t.speed(0)
t.screensize(800, 600, "lightblue")  # lightblue   #87CEEB
t.penup()
t.goto(x_y[0][0], x_y[0][1])
t.pendown()
t.seth(-90)
t.fd(180)
t.left(20)
t.fd(300)

t.penup()
t.goto(x_y[0][0], x_y[0][1])
t.pendown()
t.seth(45)
t.fd(50 * math.sqrt(2))
t.seth(-90)
t.fd(180)
t.left(25)
t.fd(350)

t.penup()
t.goto(x_y[0][0], x_y[0][1])
t.pendown()
t.seth(190)
t.fd(35)
t.seth(45)
t.fd(50 * math.sqrt(2) + 5)
t.right(45)
t.fd(10)
t.right(135)
t.fd(50)
t.seth(10)
t.fd(10)
t.seth(44.7)
t.fd(54)
t.right(45)
t.fd(9)

t.penup()
t.goto(x_y[1][0], x_y[1][1])
t.pendown()
t.seth(-90)
t.right(30)
t.fd(45)
t.left(60)
t.fd(45)
t.seth(190)
t.fd(-x + 2)
t.right(70)
t.fd(45)

t.penup()
t.goto(x, y)
t.pendown()
t.seth(-90)
t.fd(50)
t.right(30)
t.fd(45)
t.seth(10)
t.fd(-x + 2)

t.penup()
t.goto(x_y[2][0], x_y[2][1])
t.pendown()
t.seth(-90)
t.fd(340)
t.seth(0)
t.fd(10)
t.left(90)
t.fd(290)
t.seth(-90)
t.circle(6, -180)
t.seth(-70)
t.fd(295)

t.penup()
t.goto(x_y[3][0], x_y[3][1])
t.pendown()
t.seth(-90)
t.pencolor("pink")
t.fd(295)

t.penup()
t.goto(x_y[4][0], x_y[4][1])
t.pendown()
t.pencolor("black")
t.seth(-85)
t.fd(210)

t.begin_fill()
t.penup()
t.goto(x_y[5][0], x_y[5][1])
t.pendown()
t.seth(8)
t.fd(1100)
t.seth(-40)
t.fd(30)
t.seth(-172)
t.fd(1100)
t.seth(144)
t.fd(30)
t.color("gray")
t.end_fill()

lens_1 = 500
for i in range(6, 9):
    t.penup()
    t.goto(x_y[i][0], x_y[i][1])
    t.pendown()
    t.seth(240)
    t.fd(lens_1)
    lens_1 -= 33

lens_2 = 600
for j in range(9, 12):
    t.penup()
    t.goto(x_y[j][0], x_y[j][1])
    t.pendown()
    t.seth(230)
    t.fd(lens_2)
    lens_2 -= 50

k = 7
lens = 600
while k:
    t.penup()
    t.goto(x_y[12][0], x_y[12][1])
    t.pendown()
    t.seth(-40)
    t.fd(lens)
    k -= 1
    x_y[12][1] -= 20
    lens -= 20

m = 2
x_ = 15
y_ = 20
lens = 400
while m:
    x_y[12][0] += x_
    x_y[12][1] -= y_
    t.penup()
    t.goto(x_y[12][0], x_y[12][1])
    t.pendown()
    t.seth(-40)
    t.fd(lens)
    x_ += 5
    y_ += 20
    m -= 1
    lens -= 50
name = "燕山大学"
t.penup()
t.goto(25, 250)
t.seth(-90)
# t.pendown()
t.pencolor("red")
for n in name:
    t.write(n, align="center", font=("华文行楷", 35, "normal"))
    t.fd(50)

yz = [[-300, 300], [-250, 290], [200, 250]]
for y in range(3):
    t.penup()
    t.goto(yz[y][0], yz[y][1])
    t.seth(0)
    t.pendown()
    t.pensize(2)
    t.color("#0f0f28")
    t.circle(-40, 50)
    t.seth(60)
    t.circle(-40, 50)
t.begin_fill()
t.pencolor("orange")
t.penup()
t.goto(420, 300)
t.seth(0)
t.pendown()
t.circle(100, -90)
t.seth(0)
t.fd(100)
t.seth(-90)
t.fd(100)
t.color("orange")
t.end_fill()

tree_xy = [[-100, -300], [250, -300]]
tree_high = [80, 120]
for tree_ in range(2):
    pen = t.Turtle()
    pen.speed(0)
    pen.color("brown")
    pen.width(2)
    pen.penup()
    pen.goto(tree_xy[tree_][0], tree_xy[tree_][1])
    pen.pendown()


    def draw_tree(branch_len, t, level):
        if branch_len < 5:
            t.color("pink")
            t.stamp()
            t.color("brown")
        else:
            angle = random.randint(20, 45)
            sf = random.uniform(0.6, 0.8)
            t.pensize(branch_len / 10)
            t.fd(branch_len)
            t.left(angle)
            draw_tree(branch_len * sf, t, level + 1)
            t.right(angle * 2)
            draw_tree(branch_len * sf, t, level + 1)
            t.left(angle)
            t.backward(branch_len)

            if level == 0:
                t.color("green")
                t.stamp()


    tree_height = tree_high[tree_]
    pen.left(90)
    pen.backward(tree_height)
    pen.pendown()
    draw_tree(tree_height, pen, 0)

t.hideturtle()

t.done()
