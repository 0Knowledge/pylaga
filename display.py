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
#	Blah. the display. points, health and healthbar
#
#       this whole file needs to be cleaned up to adhere to the globalvars more, im lazy.
#	Scratch that. we need to get rid of globalvars alltogehther. DEATH TO GLOBAL VARS! 
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars

############
#just a temporary object so that health doesnt error when you dont add an object
class dummy:
	health=50
	life=0
###################
##i needed to make this an object becuase i couldnt figure out how to
#make it globally available but also writable
#meh
class Points(pygame.sprite.Sprite):
	total_points=0
	temp=0 #if its changed, temp changes to 1 (slightly speeds things up)
	pointstr="points:"
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.font = pygame.font.Font(globalvars.defaultfont, globalvars.points_text_size)
		self.rect = pygame.Rect(globalvars.points_x, globalvars.points_y, 10, 10) ###changee
        	self.textimg=self.font.render(self.pointstr, 0, (128, 128, 128))
		self.textrect=self.textimg.get_rect()
		self.pointsimg=self.font.render(str(self.total_points), 0, (128, 128, 128))
		self.pointsrect=self.pointsimg.get_rect()
		self.pointsrect.move_ip(0,self.textrect.height)
		self.image= pygame.Surface((self.textrect.width,self.pointsrect.height+self.textrect.height))
		globalvars.normalize_img(self.image)
		#self.image.set_alpha(100)
		pygame.Surface.blit(self.image,self.textimg,self.textrect)
		pygame.Surface.blit(self.image,self.pointsimg,self.pointsrect)
		temp=1

	def add_points(self,points):
		self.total_points+=points
		self.temp=1
	
	def set_points(self,points):
		self.total_points=points
		self.temp=1
		
	def get_points(self):
		return self.total_points
	
	def sub_points(self,points):
		self.total_points-=points
		self.temp=1
	
	def update(self):
		if self.temp!=0:
                        self.image.fill(globalvars.bgcolor,self.pointsrect)
			self.pointsimg=self.font.render(str(self.total_points), 0, (128, 128, 128))
			self.pointsrect=self.pointsimg.get_rect()
                        self.pointsrect.move_ip(0,self.textrect.height)
			pygame.Surface.blit(self.image,self.pointsimg,self.pointsrect)
			self.temp=0
	
	def draw(self):
		text = self.font.render(self.pointstr+str(self.total_points), 0, (128, 128, 128))
		globalvars.surface.fill((0,0,0),self.rect)
    		globalvars.surface.blit(text, (globalvars.points_x,globalvars.points_y))
#####################

###################
##K the deal with all these surfaces is I want 2 pieces of text on 1 image, and this is the way to go
##tracks the health of an object withthe attribute health
class Health(pygame.sprite.Sprite):
	temp=0 #if its changed, temp changes to 1 (slightly speeds things up)
	healthstr="health:"
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.a=dummy()
		self.last_health=1234
		self.font = pygame.font.Font(globalvars.defaultfont, globalvars.points_text_size)
		self.rect = pygame.Rect(globalvars.health_x, globalvars.health_y, 10, 20) ###changeee
		self.textimg=self.font.render(self.healthstr, 0, (128, 128, 128))
		self.textrect=self.textimg.get_rect()
		self.healthimg=self.font.render(str(self.a.health), 0, (128, 128, 128))
		self.healthrect=self.healthimg.get_rect()
		self.healthrect.move_ip(0,self.textrect.height)
		self.image= pygame.Surface((self.textrect.width,self.healthrect.height+self.textrect.height))
		globalvars.normalize_img(self.image)
		#self.image.set_alpha(100)points
		pygame.Surface.blit(self.image,self.textimg,self.textrect)
		pygame.Surface.blit(self.image,self.healthimg,self.healthrect)
		temp=1
	
	def link_sprite(self,sprite):
		self.a=sprite
		#print "Linked %s with the health display"%sprite
		
	def get_health(self):
		return self.a.health
	
	def get_temp(self):
		return self.temp

	def get_size(self):
                return pygame.Rect.union(self.healthrect,self.textrect)
	
	def update(self):
		if self.last_health != self.a.health:
			self.image.fill(globalvars.bgcolor,self.healthrect)
			self.healthimg=self.font.render(str(self.a.health), 0, (128, 128, 128))
			self.healthrect=self.healthimg.get_rect()
                        self.healthrect.move_ip(0,self.textrect.height)
			pygame.Surface.blit(self.image,self.healthimg,self.healthrect)
			#print "Health Decreased to "+str(self.total_health)
			self.last_health=self.a.health

		
	def draw(self):
		text = self.font.render(str(self.a.health), 0, (128, 128, 128))
		globalvars.surface.fill((0,0,0),self.rect)
    		globalvars.surface.blit(text, (globalvars.points_x,globalvars.points_y))
#####################

		
class HealthBar(pygame.sprite.Sprite):
        offset=globalvars.healthbar_offset_y
        offsetx=globalvars.healthbar_offset_x
	width=globalvars.healthbar_width
	
	def __init__(self, health):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.top=health.get_size().bottom
		self.rect = pygame.Rect(self.offsetx, self.offset+self.top, 5, 110) ###changeee
		self.image= pygame.Surface((self.width,110))
		globalvars.normalize_img(self.image)
		self.healthobject=health
		self.last_health=globalvars.max_health
		pygame.draw.rect(self.image,(128,128,128),pygame.Rect(0,0,self.width,self.last_health))
		
	
	def update(self):
		currenthealth=self.healthobject.get_health()
		#print Health.total_health
		if self.last_health != currenthealth:
			if self.last_health < currenthealth:
				pygame.draw.rect(self.image,(128,128,128),pygame.Rect(0,0,self.width,currenthealth))
			self.last_health=currenthealth
			pygame.draw.rect(self.image,globalvars.bgcolor,pygame.Rect(0,0,self.width,globalvars.max_health-currenthealth))
#####################

class LivesBar(pygame.sprite.Sprite):
        offset=10
        offsetx=5
	width=35
	length=200
	left=0
	size=(30,30)
	
	def __init__(self, health,objabove):
		print "lives added"
		self.player=health.a
		self.h=health
		print "player is: %s"%self.player
		self.lastlife=-100
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.top=objabove.rect.bottom+5
		self.rect = pygame.Rect(self.offsetx, self.offset+self.top, self.left, self.length) ###changeee
		self.image= pygame.Surface((self.width,200))
		globalvars.normalize_img(self.image)
		self.image.blit(globalvars.screen,self.image.get_rect())
		self.playerimage=pygame.transform.scale(globalvars.playership[0],self.size)
		self.playerimage.set_colorkey(globalvars.bgcolor,pygame.RLEACCEL)
		self.playerrect=self.playerimage.get_rect()
		self.update()
		
	def update(self):
		if self.player != self.h.a:  #cuz of that fuckin dummy obj
			self.player=self.h.a
		currenthealth=self.player.life
		#print "Health is: %s"%currenthealth
		if self.lastlife != currenthealth:
			self.lastlife=currenthealth
			#print "Updating to %s"%currenthealth
			for x in range(self.lastlife):
				self.playerrect.topleft=(0,x*(self.playerrect.height+10))
				self.image.blit(globalvars.screen,self.playerrect)
				self.image.blit(self.playerimage,self.playerrect)
			self.playerrect.topleft=(0,(self.lastlife+1)*(self.playerrect.height+10))
			self.image.blit(globalvars.screen,self.playerrect)
