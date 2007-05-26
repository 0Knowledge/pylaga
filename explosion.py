#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	The explosion class... for explosions
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from token import Token
from pygame.transform import chop,rotate
from pygame.locals import *

################
#I dunno what im really doing
class ExplosionPiece(Token):	
	def __init__(self,parent,image,initialloc):
		#print "asplosion"
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.parent=parent
		self.initimage=image
		self.image= image
		self.rect = self.image.get_rect()
		self.rect.center=initialloc
		self.deltax=random.randint(3,7)
		self.deltay=random.randint(-9,-3)
		self.inity=self.rect.top
		self.rotation=10
		self.angle=self.rotation
		
	def update(self):
		if self.deltay%1<.01:
			self.image=rotate(self.initimage,self.angle)
			self.angle+=self.rotation
		self.rect.centerx+=self.deltax
		self.rect.top+=self.deltay
		self.deltay+=.2
		if self.rect.top > globalvars.WIN_RESX:
			self.parent.remove(self)
###################

def Explode(obj,objlist):
	pieces=quarter(obj.image,2)
	for x,y in enumerate([-1,-2,1,2]):
		piece = ExplosionPiece(objlist,pieces[x],obj.rect.center)
		piece.deltax*=y
		piece.rotation*=y
		objlist.add(piece)
		
def quarter(image,size):
	pieces=[]
	imgrect=image.get_rect()
	imgrect.width=imgrect.width/size
	imgrect.height=imgrect.height/size
	for x in range(size):
		for y in range(size):
			imgrect.left=imgrect.width *(-x)
			imgrect.top =imgrect.height*(-y)
			img = pygame.Surface(imgrect.size)
			globalvars.normalize_img(img)
			img.blit(image,imgrect)
			pieces.append(img)
	return pieces
