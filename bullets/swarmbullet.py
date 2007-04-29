from bullet import Bullet
import random

class SwarmBullet(Bullet):
	def __init__(self,bulletlist):
		Bullet.__init__(self,bulletlist)
		self.x=1
		self.xran = random.uniform(1,6)
		self.y=self.plot(self.x)
		self.bspeed=.6
		self.xspeed=.1

	def update(self):
		self.y=self.plot(self.x - self.xran)
		self.rect.move_ip(self.bspeed,self.y) #remember it STARTS at the highest Y value
		if self.rect.bottom <= 0 or self.health <= 0:
			self.parentlist.remove(self)
		self.x+=self.xspeed

	def plot(self,x):
		return -(x**2)