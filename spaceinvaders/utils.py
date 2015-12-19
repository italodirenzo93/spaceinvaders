class Vec2(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return "( 'x' : {0}, 'y' : {1} )".format(self.x, self.y)
		
	def __str__(self):
		return "Vec2( X : {0}, Y : {1} )".format(self.x, self.y)
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
		
	def __ne__(self, other):
		return not self == other
		
	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)
		
	def __sub__(self, other):
		return Vec2(self.x - other.x, self.y - other.y)