def start(p):
	p.enemy_rows=4
	p.enemy_cols=6
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("BigFuckinGun","Bullet",p.playerbulletmanager)
	p.p.bgstars.star_color=(150,0,0)