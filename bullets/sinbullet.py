from bullet import Bullet
import math

class SinBullet(Bullet):
	def __init__(self,bulletlist,**kw):
		self.kw=kw
		Bullet.__init__(self,bulletlist)
		self.inc=.2
		self.c=0
		self.width=30
		self.speed=10
		#print "kwargs are ",kw
		#print "kwargs are ",self.kw
		self.mid=self.kw['mid']
		
	def update(self):
		#print self.
		self.rect.left=self.mid+self.width*math.sin(self.c)
		self.c+=self.inc
		
		self.rect.top-=self.speed
		if self.rect.bottom <= 0 or self.health <= 0:
			self.parentlist.remove(self)