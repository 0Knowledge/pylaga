class TrueBFG(Gun):
	def shoot(self,rect):
		left=rect.left
		centery=rect.centery
		width=rect.width
		for x in range(10):
			a=self.bullet(self.gunlist)
			a.set_pos(left-(width*x)+200,centery)
			a.damage=self.damage
			a.health=2
			self.gunlist.add(a)