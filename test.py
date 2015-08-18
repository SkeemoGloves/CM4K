import turtle
import math
import random

wd = turtle.Screen()
selosh = turtle.Turtle()
selosh.shape("turtle")
def polygon(n,crad,turtle):
	a = (n-2.0)*(180.0/n)
	s = 2.0*math.sin(math.pi/n)*crad
	for i in range(0,n):
		turtle.fd(s)
		turtle.rt(180.0-a)
		turtle.color(random.random(), random.random(), random.random())
for i in range(3, 50):
	polygon(i, 10.0*i, selosh)
wd.exitonclick()

