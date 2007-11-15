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
#	The player class
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import explosion
from globalvars import playership,explosion_speed,gamewindow,max_health,playershipanimation,playerdmg,playerdmgani,damagelevel,init_lives, x, y
import globalvars  #what the fuck. try this. print out 'x' and you'll see it disagrees with globalvars.x. that makes no sense, either way its why im importing it
from bullet import *
from gun import *
from guns import *
from bullets import *

################
#origional program had a few boring player lines, so i made it an object, cuz objects are cool
class Player(pygame.sprite.Sprite):
	health=max_health
	
	def __init__(self,parent,secondparent,gun):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.parent=parent
		self.secondparent=secondparent
		self.image= playership[0]
		self.rect = self.image.get_rect()
		self.state=0
		self.imglen=len(playership)
		self.imglen2=len(playershipanimation)
		self.playership=playership
		self.playershipani=playershipanimation
		self.speed=10
		self.gun=gun
		self.life=init_lives
		self.wait_on_dead=0            #don't yell at me for making these. garrett suggested it.
		self.wait_on_dead_limit=100    #everything is his fault.
					       #IT MAKES THE CODE UGLY. UGLY!!!!
	
	def get_pos(self):
		return self.rect
	
	def move(self, x,y):
		if self.wait_on_dead:
			return
		self.rect.topleft=(x,y)
		
	def move_one(self,direction):
		if self.wait_on_dead:
			return
		elif direction == 1:
			self.rect.left+=self.speed
			if not self.in_range(self.rect): #if it goes out of the range, move it back
				self.rect.left-=self.speed
		elif direction == 0:
			self.rect.left-=self.speed
			if not self.in_range(self.rect):
				self.rect.left+=self.speed
	
	def move_one_left(self,**kwargs):
		self.move_one(0)
	
	def move_one_right(self,**kwargs):
		self.move_one(1)
	
	
	def in_range(self,rect):
		if gamewindow.contains(rect):
			return True
		return False
	
	def set_pos(self, tempx,tempy):
		self.rect.move_ip(tempx,tempy)
	
	def set_hit(self,health):
		self.state=1
		self.health-=health
		if self.health <= damagelevel:
			#print "Changed to dmged img"
			if self.playership != playerdmg:
				self.playershipani=playerdmgani
				self.playership=playerdmg
		if self.health <= 0 and self.life > 0:
			self.health=max_health
			print "AKK dead! but luckily you got %s lives and %s health"%(self.life,self.health)
			self.life-=1
			explosion.Explode(self,self.secondparent)
			if self.playership != playership:
				self.playershipani= playershipanimation
				self.playership= playership
			self.wait_on_dead=1
		
		
	def shoot(self):
		self.gun.shoot(self.rect)
		
	def change_gun(self,gun,bullet,slist,damage=1,**kw):
		try: 
			a=eval(gun)
			#print "gun is %s"%a
			b=eval(bullet)
			#print "bullet is %s"%b
			c=a(slist,b,damage,**kw)
			#print "final gun is %s"%c
			self.gun=c
		except:
			print "GUN COULD NOT BE LOADED"
			#import AHH
			#AHH.ahh(1)
		
	def update(self):  #yay for update...
		if not self.wait_on_dead:
			if self.state > 0:
				self.image=self.playership[self.state/explosion_speed]
				self.state+=1
				if self.state >= self.imglen*explosion_speed:
					self.state=0
					self.image=playership[0]
			else:
				self.image=self.playershipani[(globalvars.asdf/4)%self.imglen2]
		else:
			self.wait_on_dead+=1
			if self.wait_on_dead > self.wait_on_dead_limit:
				self.wait_on_dead=0
				self.move(globalvars.x,y)
			else:
				self.rect.topleft=(-100,-100)
###################

