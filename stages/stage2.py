def start(p):
	p.enemy_rows=3
	p.enemy_cols=6
	p.enemyodds=100
	import globalvars
	#globalvars.bgcolor=(0,0,50)  ##a small hack to change the background color
	#p.p.background.fill(globalvars.bgcolor)
	#p.p.clear_screen()
	
	#a little example of how to change the background
	#i'll make an API later, for now these things can modify Anything if you know how
	#big IF cuz this program is big and confusing
	p.p.bgstars.star_color=(128,128,0)
	
	for player in p.playermanager:
		player.change_gun("ParabolaGun","WeirdFuckinBullet",p.playerbulletmanager)