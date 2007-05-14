def start(p):
	p.enemy_rows=4
	p.enemy_cols=7
	p.enemyodds=100
	p.p.bgstars.star_color=(0,128,128)
	for player in p.playermanager:
		player.change_gun("swarmgun.SwarmGun","swarmbullet.SwarmBullet",p.playerbulletmanager,2)
	
	from enemy import Enemy2
	from gun import EnemyGun2
	p.enemyclass=Enemy2
	p.enemygunclass=EnemyGun2
	p.enemy_damage=20