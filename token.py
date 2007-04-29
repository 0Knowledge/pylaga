#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	The misc object class
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars

################
#The default one just falls until it hits the bottom of the screen, boring much.
class Token(pygame.sprite.Sprite):	
	def __init__(self,parent):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.parent=parent
		self.image= globalvars.token
		self.rect = self.image.get_rect()
		self.speed=3

	def update(self):
		self.rect.top-=self.speed
		if self.rect.top < globalvars.WIN_RESX:
			self.parent.remove(self)
###################

