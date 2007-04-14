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
	enemy_stages=[(5,2),(6,3),(7,4),(8,4),(9,4)]
	current_stage=0
	
	def __init__(self,enemymanager,playermanager,enemybulletmanager,playerbulletmanager):
		self.enemymanager=enemymanager
		self.playermanager=playermanager
		self.enemybulletmanager=enemybulletmanager
		self.enemyodds=globalvars.enemy_bullet_odds
		self.playerbulletmanager=playerbulletmanager
	
	def add_stage(self, x,y):
		self.enemy_stages.append((x,y))
	
	def next_stage(self):
		
		if len(self.enemy_stages) > self.current_stage+1:
			self.current_stage+=1
		#if self.current_stage!=0:
			#menulists.buy_menu(( ("!Buy A","print 'buy'"),("!Buy Somethin","print 'buysomethinelse'"),("SomethinElse","print 'asdf'"),("Back","goagain=False")))
			
		if self.enemyodds > 15:
			self.enemyodds-=15
		self.enemymanager.current_transition=0
		self.draw_enemys()
		
		for player in self.playermanager:
			player.gun=ParabolaGun(self.playerbulletmanager,WeirdFuckinBullet)
	
	def set_stage(self, stage):
		self.current_stage=stage
	
	def get_stage(self):
		return self.enemy_stages[self.current_stage]
	
	#draws all the enemys you ask it
	def draw_enemys(self):
		#k so now some recursive loops:
		for enemycol in range(self.enemy_stages[self.current_stage][0]):	
			#now for the rows
			for enemyrow in range(self.enemy_stages[self.current_stage][1]):
				#make a new enemy object:
				tempenemy=Enemy(self.enemymanager,Gun(self.enemybulletmanager,EnemyBullet))
				#this ones a long one, but it works:
				tempenemy.set_pos(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.ymin+enemyrow*(globalvars.enemy_height+globalvars.enemy_spacing_y)-150)
				#this one is even worse, but works even better:
				tempenemy.set_range(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.xmax-(self.enemy_stages[self.current_stage][0]-enemycol)*(globalvars.enemy_height+globalvars.enemy_spacing_x))                                                                                                     
				#now add the temp enemy to the array and we're good to go
				self.enemymanager.add(tempenemy)
				
	
#####################