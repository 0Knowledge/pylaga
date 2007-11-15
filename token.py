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

