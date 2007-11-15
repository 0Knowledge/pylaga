#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py

#######################################################################
#    This file is part of pylaga.
#
#    Pylaga is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pylaga is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Pylaga.  If not, see <http://www.gnu.org/licenses/>.
#
#    YAY FOR LONG LICENSES!!!! screw you society.
#######################################################################

#################################################################################################################
#
#
#	arguably the most important class, this is the game object
#	it *is* the game. in an object.
#
#import pygame os and sys libraries
try:
	import pygame, os, sys, math, random
	from pygame.locals import*
	import globalvars
	from bullet import Bullet, EnemyBullet
	from background import BackgroundManager
	from enemy import Enemy, EnemyManager
	from player import Player
	from stage import Stage
	from display import *
	from menu import Menu
	from menulists import MenuLists,menulists
	import ecollision #testing class for smarter collisions
	from gun import Gun
	from event import Event
except:
	print "A File Was Missing. CHECK!"
	#sys.exit(0)

if not pygame.font: print 'Warning, fonts disabled'
#################################################################################################################
	
#now for the actual game class (I like classes. lets make classes of everything. rainbows are fun.)
class Gamelolz:
	#This is the __init__ 
	#its important.
	def __init__(self,parent):  
		self.parent=parent
		globalvars.asdf = 0
		##some key vars, the works
		self.lagcount=0		
		#a little hack so that the background works nicer
		self.background=globalvars.screen
		#make the rectlist to handle dirty updating
		self.updaterects=[]
		#background object
		self.bgstars=BackgroundManager()
		##make the lists to handle various sprites
		self.list_enemys=EnemyManager()
		self.player_list=pygame.sprite.RenderUpdates()
		self.list_allie_shots=pygame.sprite.OrderedUpdates()
		self.enemy_shots=pygame.sprite.RenderUpdates()
		self.token_list=pygame.sprite.RenderUpdates()
		##make a new stage object
		self.stage=Stage(self,self.list_enemys,self.player_list,self.enemy_shots,self.list_allie_shots)
		#self.setup_events()
		self.new_display()
	
	def new_display(self):
		self.side_panel= pygame.sprite.RenderUpdates()
		self.points=Points()
		self.side_panel.add(self.points)
		self.health=Health()
		self.healthbar=HealthBar(self.health)
		self.livesbar=LivesBar(self.health,self.healthbar)
		self.side_panel.add(self.healthbar)
		self.side_panel.add(self.health)
		self.side_panel.add(self.livesbar)
		
	#clears all the variables
	def clear_vars(self):
		self.leftkeydown=0
		self.rightkeydown=0
		self.points.set_points(0)
		globalvars.x=400
		globalvars.y=globalvars.WIN_RESY-60
		self.stage.set_stage(0)
		self.list_enemys.empty()
		self.list_allie_shots.empty()
		self.player_list.empty()
		self.enemy_shots.empty()
		print "Game Restarted"
		
	def register_inputs(self):
		import defaultinputs
		defaultinputs.setup(self.inputmanager,self)

		
	#define function to draw player ship on X, Y plane
	def pship(self):
		self.player_list.clear(globalvars.surface,self.background)
		self.updaterects+=self.player_list.draw(globalvars.surface)
	
	#Define function to move the enemy ship
	def emove(self):
		self.list_enemys.clear(globalvars.surface, self.background)
		self.updaterects+=self.list_enemys.draw(globalvars.surface)
	
	
				
	#So i'm trying out having the program check for collisions, instead of the enemy objects
	#i think i might switch to the objects, but still keep this function just hand the computing to the object
	#seems most efficient
	def test_collision(self):
		todie=ecollision.groupcollide(self.list_enemys, self.list_allie_shots,0,0,ecollision.BOTTOM)
		#todie=pygame.sprite.groupcollide(self.list_enemys, self.list_allie_shots,0,0)
		#print todie
		for enemy,bullet in todie.iteritems():
			bullet.set_hit(1)
			enemy.hit(bullet.damage)
			self.points.add_points(1)
		for q in pygame.sprite.spritecollide(self.player, self.enemy_shots,0):
		#for q in ecollision.spritecollide(self.player, self.enemy_shots,0,ecollision.TOP):
			#print "ZOMFG SHOTZORZ"
			self.player.set_hit(q.damage)
			self.enemy_shots.remove(q)
		#if self.token_list:
		#	for token in ecollision.spritecollide(self.player, self.token_list,0, ecollision.TOP):
		#		print token
	
	#if there are no enemys left, go to the next stage
	def check_done(self):
		if not globalvars.asdf%20 and not self.list_enemys: #the %20 lets it wait a fraction of a second
			self.stage.next_stage()
	
	#checks to see if we can expand the ranges of the bots so its nice and.... umm... nice.
	def check_rows(self):
		if globalvars.asdf % 20==0:
			self.list_enemys.check_enemy_rows()
					
        #major hack just to get this thing playable..... sorry
	def again(self):
                if self.player.health <= 0:
                        return False
                return True
		
	
	#this is called if the player shoots... to be honest i dont know why this is a function
	def pshoot(self,**args):
		self.player.shoot()
	
	#draws the bullet.... duh. come on dude.
	def drawbullets(self):
		#for x in self.list_allie_shots:
			#x.draw()
		self.list_allie_shots.clear(globalvars.surface,self.background)
		self.enemy_shots.clear(globalvars.surface,self.background)
		self.updaterects+=self.list_allie_shots.draw(globalvars.surface)
		self.updaterects+=self.enemy_shots.draw(globalvars.surface)
	
	#...
	def drawsidepanel(self):
		if globalvars.asdf%5==0:
			self.side_panel.update()
		self.side_panel.clear(globalvars.surface,self.background)
		self.updaterects+=self.side_panel.draw(globalvars.surface)
		
	#dont ask why i made this a function, i made draw<asdf> for everythign else 
	#so figured id make this too
	def drawtokens(self):
		if self.token_list:
			self.token_list.clear(globalvars.surface,self.background)
			self.updaterects+=self.token_list.draw(globalvars.surface)
		
	#goes through all the arrays and makes each of them move 1 space, simple and easy yet it deserves a comment...
	def tick(self):
		self.bgstars.update()
		self.list_allie_shots.update()
		self.list_enemys.update()
		self.enemy_shots.update()
		self.token_list.update()
		self.player.update()
	
	######################
	#heres a bunch of metafunctions
	#i break it up so its really easy to add new features
	#like if we ant a counter? add something to check() and draw()
	#all of these are called once per frame
	def check(self):
		self.check_done()
		self.test_collision()
		self.check_rows()
		self.list_enemys.shoot(self.stage.enemyodds)


	
	def draw(self):
		self.updaterects+=self.bgstars.draw()
		self.updaterects+=self.bgstars.clear()
		self.drawbullets()
		self.pship()
		self.emove()
		self.drawsidepanel()
		self.drawtokens()
	
	#does just what it sounds like.....
        def clear_screen(self):
                globalvars.surface.fill(globalvars.bgcolor)
		pygame.display.flip()
	
	#for debugging info mostly... No entirely
	def dispvars(self):
		print "The Enemy Array size is:",len(self.list_enemys.sprites())
		print "The Player Shot Array size is:",len(self.list_allie_shots.sprites())
		print "The Enemy Shot Array size is:",len(self.enemy_shots.sprites())
	
	#does lots and lots of stuff, it really needs to be cleaned up
	def input(self, events):
		self.inputmanager.check(events)
	
	def mousemove(self,parent,event):
		tempx=pygame.mouse.get_pos()[0]-parent.player.rect.width/2
		## Just to make sure we don't get the ship way out there:
		if tempx > globalvars.xmax: #if its outside the globalvars.window, just stick it as far as possible
			parent.player.move(globalvars.xmax,globalvars.y)
		elif tempx < globalvars.xmin:
			parent.player.move(globalvars.xmin,globalvars.y)
		elif abs(tempx-globalvars.x) > globalvars.smooth_scroll_var1:  #smooth scrolling if the mouse gets far from the ship
			parent.player.move(parent.player.get_pos().left+(tempx-parent.player.get_pos().left)/globalvars.smooth_scroll_var2,globalvars.y)
		else:		#if it gets down to this point, 
				#we've passed all sanity checks so just move it
			parent.player.move(tempx,globalvars.y)
	##################################################################################################################                


	#pretty simple
	def start(self):
		self.clear_vars()
		self.player=Player(self.player_list,self.token_list,Gun(self.list_allie_shots,Bullet))
		self.player_list.add(self.player)
		self.player.set_pos(globalvars.x,globalvars.y)
		self.health.link_sprite(self.player)
		self.inputmanager=self.parent.inputmanager
		self.register_inputs()
		self.loop()

	#Yeah see this one does all of the work
	def loop(self):
		#start loop
		while self.again():
			
			#refresh self.background...needs to be done once in a while
			if globalvars.asdf>=globalvars.REFRESH_TIME:
				#self.clear_screen()
				globalvars.asdf=0
			globalvars.asdf+=1
			
			#check everythign and see if changes need to be made
			self.check()
			
			#move everything 1
			self.tick()
						
			#initiate input function
			self.input(pygame.event.get())
			
			#draw everything
			self.draw()
			
			#applies the smart screen updating
			#globalvars.surface.set_alpha(150,pygame.RLEACCEL)       ......dont ask why
			#globalvars.surface2.blit(globalvars.surface,globalvars.surfacerect)
			pygame.display.update(self.updaterects)
			self.updaterects=[]
			
			#pauses and waits
			self.time= globalvars.clock.get_time()
			if self.time > globalvars.FPS:
				timeittook=globalvars.clock.tick(globalvars.FPS-(self.time-globalvars.FPS))
				print "Lag at frame %s\t%sms"%(globalvars.asdf,self.time)
			else:
				timeittook=globalvars.clock.tick(globalvars.FPS)
			#if timeittook > 1000/globalvars.FPS:
			#	print "LAG:"+str(self.lagcount)+" at "+str(timeittook)+"ms"
				#self.dispvars()
			#	self.lagcount+=1
			#print globalvars.clock.get_fps()
