#Being the first stage, it has the responsibility of initializing All game variables that arent already
#essentially it doesnt enjoy the lazyness that the other stages get
#k so the file is just 1 function, start(obj)
# obj is usually the stage object that called it, but i suppose it could change
def start(p):
	p.enemy_rows=4
	p.enemy_cols=5
	p.enemyodds=100
	p.enemy_damage=3