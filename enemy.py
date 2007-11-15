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
#	The All Important Enemy class, and its manager EnemyManager
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from bullet import EnemyBullet

#####################
class EnemyManager(pygame.sprite.RenderUpdates):
	def __init__(self):
		pygame.sprite.RenderUpdates.__init__(self)
		self.asdf=0
		self.transition_speed=5
		self.transition_time=150/self.transition_speed
		self.current_transition=0
		
	def shoot(self,odds):
		self.asdf=random.randint(0,odds)
		if self.asdf < len(self):
			self.sprites()[self.asdf].shoot()
	
	def update(self):
		if self.current_transition<self.transition_time:
			for e in self:
				e.update(self.transition_speed)
			self.current_transition+=1
		else:
			for e in self:
				e.update(0)
				
	def check_enemy_rows(self):
		#simple sorting algorithm to find the highest values
			highest=globalvars.xmin
			lowest=globalvars.xmax
			for enemy in self:
				if enemy.get_range()[1] > highest:
					highest=enemy.get_range()[1]
				if enemy.get_range()[0] < lowest:
					lowest=enemy.get_range()[0]
			highest=globalvars.xmax-highest
			lowest=lowest-globalvars.xmin
			if highest != 0 or lowest != 0: #makes things |--| this much more efficient
				for enemy in self:
					erange=enemy.get_range()
					enemy.set_range(erange[0]-lowest,erange[1]+highest)

#################
#origional program had a few boring enemy lines, so i made it an object, cuz objects are cool
class Enemy(pygame.sprite.Sprite):
	enx=0
	eny=30
	#enspeed=globalvars.init_enemy_speed
	#envel=1
	#en_globalvars.xmax=globalvars.xmax #come in very handy when there is more than 1 enemy
	#en_globalvars.xmin=globalvars.xmin #yeah what the first one said.^^
	#en_state=(-1)*(1)
	#image = globalvars.enemyship
	
	
	def __init__(self, parent, gun, health=1):
		self.parent=parent
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.enspeed=globalvars.init_enemy_speed
		self.envel=1
		self.en_xmax=globalvars.xmax
		self.en_xmin=globalvars.xmin
		self.en_state=(-1)*(1)
		self.image=globalvars.enemyship
		self.rect = self.image.get_rect()
		self.health=health
		self.gun=gun
	
	#def get_pos(self):
		#return self.enx,self.eny
	
	def set_pos(self, tempx,tempy):
		self.rect.move_ip(tempx,tempy)
		
	def set_speed(self, speed):
		self.enspeed=speed
		
	def set_range(self,tempmin,tempmax):
		self.en_xmax=tempmax
		self.en_xmin=tempmin
	
	def get_range(self):
		return self.en_xmin,self.en_xmax
	
	def set_health(self,health):
		self.health=health
		
	def hit(self,damage):
		self.health-=damage
		if self.health <= 0:
			self.en_state=0
	
	def update(self, transition_speed):  #yay for update...
		#this is actually surgy's code but i adapted it to my own and rewrote it
		#so it uses god damn <s and >s not ==s and !=s... terrible programming.
		if transition_speed > 0:
			self.rect.bottom+=transition_speed
		elif self.envel <= 0:
			if self.rect.left < self.en_xmax:
				self.rect.right+=self.enspeed
			elif self.rect.left >= self.en_xmax:
				self.envel = 1
		else:
			if self.rect.left > self.en_xmin:	
				self.rect.right+=((-1)*self.enspeed)
			elif self.rect.left <= self.en_xmin:
				self.envel = 0
		self.next_state()
			
	#-1 is normal, 0 is exploding, up to 4 are the animations for it
	def set_state(self, varr):
		self.en_state=varr
		
	def next_state(self):
		if self.en_state>=0 and self.en_state<5:
			self.image=globalvars.explosions[self.en_state]
			self.en_state+=1
		elif self.en_state>4:
			self.parent.remove(self)
	
	#return the state
	def get_state(self):
		return self.en_state
	
	def shoot(self):
		self.gun.shoot(self.rect)
###################

class Enemy2(Enemy):
	def __init__(self, parent, gun, health=1):
		Enemy.__init__(self, parent, gun, health=1)
		self.image=globalvars.enemyship2
