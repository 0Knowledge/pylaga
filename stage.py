#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	stage manager
#
#	Needs lots of improvement
#	i *think* thats done.
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from enemy import Enemy
from bullet import *
from gun import *
from menulists import MenuLists,menulists
from stages import *

#####################
##turns out makin the stages be a class was a really good idea. makes it SOO much easier.
class Stage:
	current_stagenum=0
	datadir=globalvars.STAGEDIR+"stage"
	
	#gotta have the stage remember all the lists its going to be added to
	def __init__(self,parent,enemymanager,playermanager,enemybulletmanager,playerbulletmanager):
		self.p=parent
		self.enemymanager=enemymanager
		self.playermanager=playermanager
		self.enemybulletmanager=enemybulletmanager
		self.enemyodds=globalvars.enemy_bullet_odds
		self.playerbulletmanager=playerbulletmanager
		#initial stage file
		file=self.datadir+str(0)
		execstr="import "+file
		try:
			if os.name=='nt':  #hax for the fuckin winblowz users
				exec "import stages.stage"+str(0)
				self.current_stage=eval("stages.stage0")
			else:
				self.current_stage=__import__(file)
			self.current_stage.start(self)
		except:
			import pylaga
			pylaga.exception_handler()
			sys.exit(1)
		
	
	def next_stage(self):
		#woo, k so this dynamically loads the stage files
		self.current_stagenum+=1
		file=self.datadir+str(self.current_stagenum)
		print "Changing stage to %s"%file
		try:
			if os.name=='nt':
				exec "import stages.stage"+str(self.current_stagenum)
				self.current_stage=eval("stages.stage"+str(self.current_stagenum))
			else:
				self.current_stage=__import__(file)
			self.current_stage.start(self)
		except:
			self.current_stagenum-=1
			print "Stage could not be loaded!"
			
		self.enemymanager.current_transition=0
		
		#draw the new enemys
		self.draw_enemys()
				
	
	def set_stage(self, stage):
		self.current_stagenum=stage
	
	#draws all the enemys you ask it
	def draw_enemys(self):
		#k so now some recursive loops:
		for enemycol in range(self.enemy_cols):	
			#now for the rows
			for enemyrow in range(self.enemy_rows):
				#make a new enemy object:
				tempenemy=self.enemyclass(self.enemymanager,self.enemygunclass(self.enemybulletmanager,self.enemybulletclass,self.enemy_damage))
				#this ones a long one, but it works:
				tempenemy.set_pos(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.ymin+enemyrow*(globalvars.enemy_height+globalvars.enemy_spacing_y)-150)
				#this one is even worse, but works even better:
				tempenemy.set_range(globalvars.xmin+enemycol*(globalvars.enemy_width+globalvars.enemy_spacing_x),globalvars.xmax-(self.enemy_cols-enemycol)*(globalvars.enemy_height+globalvars.enemy_spacing_x))                                                                                                     
				#now add the temp enemy to the array and we're good to go
				self.enemymanager.add(tempenemy)
				
	
#####################