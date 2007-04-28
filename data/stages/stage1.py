def start(p):
	p.enemy_rows=3
	p.enemy_cols=5
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("TrueBFG","WeirdFuckinBullet",p.playerbulletmanager)
