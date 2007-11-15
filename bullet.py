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
#	A simple bullet class, and a subclass, EnemyBullet
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random, globalvars
################
##A bullet class, simple as hell, but it does keep track of its location and saves the main thread some work
class Bullet(pygame.sprite.Sprite):  
	
	
	def __init__(self, parentlist,**kw):
		self.parentlist=parentlist
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = globalvars.shot  #sets the image
		self.rect = self.image.get_rect()  #sets the rect associated with the image
		self.bspeed=globalvars.BULLET_SPEED #sets the speed
		self.health=1
		self.damage=1
		#self.kw=kw
	
	#k all this does what it looks like, no comment needed save this one
	
	#try to just do x.rect.topleft=asdf, cuz it works the same as this
	def set_pos(self, tempx,tempy):
		self.rect.topleft=(tempx,tempy)
		#self.rect.move_ip(tempx,tempy)
		
	def set_hit(self,h=1):
		self.health-=h
		if self.health <= 0:
			self.parentlist.remove(self)
		
	def set_speed(self, speed):
		self.bspeed=speed
		
	def update(self):
		self.rect.move_ip(0,-1*(self.bspeed)) #remember it STARTS at the highest Y value
		if self.rect.bottom <= 0 or self.health <= 0:
			self.parentlist.remove(self)

########
#extention of bullet class to draw bullets
#it needs to know what list its been added to
class EnemyBullet(Bullet):
	def __init__(self, parentlist):
		self.parentlist=parentlist
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = globalvars.eshot  #sets the image
		self.rect = self.image.get_rect()  #sets the rect associated with the image
		self.bspeed=globalvars.BULLET_SPEED #sets the speed
		self.health=1
		self.damage=1
		
	def update(self):
		self.rect.move_ip(0,(self.bspeed)) #remember it STARTS at the highest Y value
		if self.rect.bottom > globalvars.WIN_RESY:
			self.parentlist.remove(self)
#################

#class BigFuckinBullet(Bullet):
	#def __init__(self, parentlist):
		#self.parentlist=parentlist
		#pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		#self.image = globalvars.shot  #sets the image
		#self.rect = self.image.get_rect()  #sets the rect associated with the image
		#self.bspeed=globalvars.BULLET_SPEED #sets the speed
		#self.health=1
	
	#def update(self):
	
class WeirdFuckinBullet(Bullet):
	def __init__(self,bulletlist):
		Bullet.__init__(self,bulletlist)
		self.x=1
		self.y=self.plot(self.x)
		self.bspeed=1
		self.xspeed=.1
		
	def update(self):
		self.y=self.plot(self.x)
		self.rect.move_ip(self.bspeed,self.y) #remember it STARTS at the highest Y value
		if self.rect.bottom <= 0 or self.health <= 0:
			self.parentlist.remove(self)
		self.x+=self.xspeed
		
		
	def plot(self,x):
		return -(x**2)
		
		