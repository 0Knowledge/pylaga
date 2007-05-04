def start(p):
	p.enemy_rows=3
	p.enemy_cols=5
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("Gun","Bullet",p.playerbulletmanager,2)
	from enemy import Enemy
	from gun import EnemyGun
	from bullet import EnemyBullet
	p.enemyclass=Enemy
	p.enemygunclass=EnemyGun
	p.enemybulletclass=EnemyBullet
