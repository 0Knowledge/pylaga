
def start(p):
	p.enemy_rows=4
	p.enemy_cols=7
	p.enemyodds=50
	for player in p.playermanager:
		player.change_gun("BigFuckinGun","Bullet",p.playerbulletmanager)

	
	
if __name__=="__main__":
	class q: pass
	a=q()
	start(a)