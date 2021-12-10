import turtle as turtle
import random
import cv2
import numpy as np
import sys

# Image Recognition and Handling
try:
	name = sys.argv[1]
except:
	name = "color.png"
img = cv2.imread(name)

# Adding Image Contrast
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
limg = cv2.merge((cl,a,b))

img = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)

# Initializing Turtle Screen
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

# Defining base constants
DOT_SIZE = 10
GAP = DOT_SIZE + 2

# Modifying image width and height to match screen dimensions
if img.shape[1] > img.shape[0]:
	MULT = screen.window_width() / img.shape[1]
else:
	MULT = screen.window_height() / img.shape[0]

MULT /= GAP

WIDTH = int(img.shape[1] * MULT)
HEIGHT = int(img.shape[0] * MULT)

number_of_dots = WIDTH * HEIGHT

screen.setup(height=HEIGHT*GAP, width=WIDTH*GAP)
img_resize = cv2.resize(img, (WIDTH, HEIGHT))

# Indexing color channels from image
r = img_resize[:, :, 0]
g = img_resize[:, :, 1]
b = img_resize[:, :, 2]

turtle.colormode(255)
turtle.tracer(0, 0)

# Initializing Turtle object
T = turtle.Turtle()

T.speed("fastest")
T.penup()
T.goto(-screen.window_width()/2, screen.window_height()/2)
T.hideturtle()

T.setheading(0)

# Drawing the dots
for dot_count in range(1, number_of_dots + 1):

	hor_pos = (dot_count-1) % WIDTH
	ver_pos = (dot_count-1) // WIDTH
	color = (r[ver_pos][hor_pos], g[ver_pos][hor_pos], b[ver_pos][hor_pos])
	
	T.dot(DOT_SIZE, color)
	T.forward(GAP)

	if dot_count % WIDTH == 0:
		T.setheading(-90)
		T.forward(GAP)

		T.setheading(180)
		T.forward(WIDTH * GAP)

		T.setheading(0)
		turtle.update()

screen.exitonclick()