#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	stage manager
#
#	Needs lots of improvement
#	...thats never a good thing to hear
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from enemy import Enemy
from bullet import *
from gun import *
from menulists import MenuLists,menulists

#####################
##turns out makin the stages be a class was a really good idea. makes it SOO much easier.
class Stage:
	current_stagenum=0
	datadir=globalvars.DATADIR[:len(globalvars.DATADIR)-1]+".stages.stage"
	
	#gotta have the stage remember all the lists its going to be added to
	def __init__(self,enemymanager,playermanager,enemybulletmanager,playerbulletmanager):
		self.enemymanager=enemymanager
		self.playermanager=playermanager
		self.enemybulletmanager=enemybulletmanager
		self.enemyodds=globalvars.enemy_bullet_odds
		self.playerbulletmanager=playerbulletmanager
		#initial stage file
		file=self.datadir+str(0)
		execstr="import "+file
		try:
			exec execstr
			self.current_stage=eval(file)
		except:
			import pylaga
			pylaga.exception_handler()
			sys.exit(1)
		
	
	def next_stage(self):
		#woo, k so this dynamically loads the stage files
		self.current_stagenum+=1
		file=self.datadir+str(self.current_stagenum)
		execstr="import "+file
		print "Changing stage to %s"%file
		try:
			exec execstr
			self.current_stage=eval(file)
		except:
			self.current_stagenum-=1
			print "Stage could not be loaded!"
			
		self.enemymanager.current_transition=0
		
		#draw the new enemys
		self.draw_enemys()
		
		#for now just set the initial gun(change btw.)
		for player in self.playermanager:
			player.gun=ParabolaGun(self.playerbulletmanager,WeirdFuckinBullet)
	
	def set_stage(self, stage):
		self.current_stagenum=stage
	
	def get_stage(self):
		return self.enemy_stages[self.current_stage]
	
	#draws all the enemys you ask it
	def draw_enemys(self):
		#k so now some recursive loops:
		for enemycol in range(self.current_stage.enemy_cols):	
			#now for the rows
			for enemyrow in range(self.current_stage.enemy_rows):
				#make a new enemy object:
				tempenemy=Enemy(self.enemymanager,Gun(self.enemybulletmanager,EnemyBullet))
				#this ones a long one, but it works:
				tempenemy.set_pos(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.ymin+enemyrow*(globalvars.enemy_height+globalvars.enemy_spacing_y)-150)
				#this one is even worse, but works even better:
				tempenemy.set_range(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.xmax-(self.current_stage.enemy_cols-enemycol)*(globalvars.enemy_height+globalvars.enemy_spacing_x))                                                                                                     
				#now add the temp enemy to the array and we're good to go
				self.enemymanager.add(tempenemy)
				
	
#####################