from gun import Gun

class SwarmGun(Gun):
	def shoot(self,rect):
		centerx=rect.centerx
		centery=rect.centery
		for x in [-3,-2,0,2,3]:
			a=self.bullet(self.gunlist)
			a.bspeed=x
			a.set_pos(centerx,centery)
			a.damage=self.damage
			self.gunlist.add(a)