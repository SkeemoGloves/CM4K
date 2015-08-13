import turtle
class wall: 
	def __init__(self, pos1, pos2):
		self._pos1 = pos1
		self._pos2 = pos2
		self.t = turtle.Turtle()
		self.t.penup() 
		self.t.goto(pos1)
		self.t.pendown()
		self.t.goto(pos2)
	#cd Desktopdef collision_check( self, turtle
	
def main():
	w = turtle.Screen()
	player = turtle.Turtle()
	wall((30,-60), (30, 60))
	while (True):
		player.fd(1) 
	w.exitonclick()
if __name__=='__main__':
	main()
		
