import turtle
import wall

#x = wall.wall(20,30)
def main(): 
	wd = turtle.Screen()
	wd.tracer(0,0)
	walls = []
<<<<<<< HEAD
	A = (0,190)
	B = (150,190)
	C = (150, -140)
	D = (-160, -140)
	E = (-160, 180)
	F = (130, 180)
	G = (130, -120)
	H = (-140, -1
	walls.append(wall.wall((A, B))
	walls.append(wall.wall(B, (150, -140)))
	walls.append(wall.wall((150, -140), (-160, -140)))
	walls.append(wall.wall((-160, -140), (-160, 180)))
	walls.append(wall.wall((-160, 180), (130, 180)))
 	walls.append(wall.wall((130, 180), (130, 120)))
	walls.append(wall.wall((130, 120), (-140, -120)))
	walls.append(wall.wall((-140, -120), (-140, 160)))
	walls.append(wall.wall((-140, 160), (120, 160)))
	walls.append(wall.wall((120, 160), (120, -110)))
	walls.append(wall.wall((120, -110), (-120, -110)))
	walls.append(wall.wall((-120, -110), (-130, 120)))
	walls.append(wall.wall((-130, 120), (0, 110)))
	walls.append(wall.wall((0, 110), (110, 130)))
=======
	walls.append(wall.wall((300, 400), (-300, 400)))
	walls.append(wall.wall((-300, 400), (-100, -50)))
	walls.append(wall.wall((-100, -50), (100,-50)))
	walls.append(wall.wall((100, -50), (100, 100)))
	walls.append(wall.wall((100,100), (100, -70)))
 	walls.append(wall.wall((100, -70), (-400, 100)))
>>>>>>> 7daa93a63bd5233f1ac4e8d6023074fd6d05282d
	wd.tracer (1,10)
	player = turtle.Turtle()

	running = True 
	while(running):
		player.fd(1)
		for w in walls: 
			if(w.collision_check(player)):
				running = False
	
<<<<<<< HEAD
	walls.append(wall.wall((-100, 100), (100, 100)))
=======
	walls.append(wall((-100, 100), (100, 100)))
>>>>>>> 7daa93a63bd5233f1ac4e8d6023074fd6d05282d
	wd.tracer (1,10)
	player = turtle.Turtle()

	running = True 
	while(running):
		player.fd(1)
		for w in walls: 
			if(w.collision_check(player)):
				running = False

if __name__=='__main__':
	main()
<<<<<<< HEAD
=======
	
>>>>>>> 7daa93a63bd5233f1ac4e8d6023074fd6d05282d


