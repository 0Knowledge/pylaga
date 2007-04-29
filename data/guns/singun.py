

class SinGun(Gun):
	def shoot(self,rect):
		for x in [-1,1]:
                	a=self.bullet(self.gunlist,mid=rect.centerx)
                	a.rect.midtop=rect.midtop
                	a.damage=self.damage
			a.inc=a.inc*x
                	self.gunlist.add(a)
		for x in [8,12]:
			a=self.bullet(self.gunlist,mid=rect.centerx)
                	a.rect.midtop=rect.midtop
                	a.damage=self.damage
			a.inc=0
			a.speed=x
                	self.gunlist.add(a)
