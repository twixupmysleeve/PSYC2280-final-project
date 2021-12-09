import turtle as turtle
import random
import cv2
import numpy as np
import sys

name = sys.argv[1]
img = cv2.imread(name)

lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
limg = cv2.merge((cl,a,b))

img = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)

MULT = 0.05
WIDTH = int(img.shape[1] * MULT)
HEIGHT = int(img.shape[0] * MULT)

img_resize = cv2.resize(img, (WIDTH, HEIGHT))

r = img_resize[:, :, 0]
g = img_resize[:, :, 1]
b = img_resize[:, :, 2]

turtle.colormode(255)
turtle.tracer(0, 0)

DOT_SIZE = 5
GAP = DOT_SIZE * 2

screen = turtle.Screen()
screen.setup(height=HEIGHT*GAP, width=WIDTH*GAP)

T = turtle.Turtle()

T.speed("fastest")
T.penup()
T.goto(-screen.window_width()/2, screen.window_height()/2)
T.hideturtle()

T.setheading(0)
number_of_dots = WIDTH * HEIGHT

for dot_count in range(1, number_of_dots + 1):
	hor_pos = (dot_count-1) % WIDTH
	ver_pos = (dot_count-1) // WIDTH
	color = (r[ver_pos][hor_pos], g[ver_pos][hor_pos], b[ver_pos][hor_pos])
	T.dot(DOT_SIZE, color)
	# print(color)
	T.forward(GAP)

	if dot_count % WIDTH == 0:
		# print(color)
		T.setheading(-90)
		T.forward(GAP)
		T.setheading(180)
		T.forward(WIDTH * GAP)
		T.setheading(0)
		turtle.update()

screen.exitonclick()