def start(p):
	p.enemy_rows=4
	p.enemy_cols=7
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("ParabolaGun","WeirdFuckinBullet",p.playerbulletmanager)