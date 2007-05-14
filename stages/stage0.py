#Being the first stage, it has the responsibility of initializing All game variables that arent already
#essentially it doesnt enjoy the lazyness that the other stages get
#k so the file is just 1 function, start(obj)
# obj is usually the stage object that called it, but i suppose it could change
# if you REALLY want to. and you think yer coool, you can do p.p.ANYTHING and get the entire game object
# or if you were feeling completely devilish you could do p.p.parent and get the entire program object.
# BWAHAHAHAHAHHAAHAHAHA
import globalvars
def start(p):
	p.enemy_rows=4
	p.enemy_cols=5
	p.enemyodds=100
	p.enemy_damage=10
	from enemy import Enemy
	from gun import EnemyGun
	from bullet import EnemyBullet
	p.enemyclass=Enemy
	p.enemygunclass=EnemyGun
	p.enemybulletclass=EnemyBullet
