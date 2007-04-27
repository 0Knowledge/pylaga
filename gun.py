#2007-04-10 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	The Base 'Gun' Class and several derivatives
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random, globalvars, bullet

#So i just realized i need to explain how these are created.
#it asks for the list that the bullets are added to, the Bullet class that it creates bullets out of
#and how much damage this gun will cause (not mandatory)
class Gun:
	"""
		basically just a simple class to make shooting simpler
	"""
	def __init__(self,gunlist,Bullet,damage=1):
		self.gunlist=gunlist
		self.bullet=Bullet
		self.damage=damage
		
	def shoot(self,rect):
		a=self.bullet(self.gunlist)
		a.set_pos(rect.centerx-a.rect.width/2,rect.centery)
		a.damage=self.damage
		self.gunlist.add(a)

class BigFuckinGun(Gun):
	def shoot(self,rect):
		left=rect.left
		centery=rect.centery
		width=rect.width
		for x in range(4):
			a=self.bullet(self.gunlist)
			a.set_pos(left+(width*x)/4,centery)
			a.damage=self.damage
			a.health=2
			self.gunlist.add(a)
			
class ParabolaGun(Gun):
	def shoot(self,rect):
		centerx=rect.centerx
		centery=rect.centery
		for x in [-2,2]:
			a=self.bullet(self.gunlist)
			a.bspeed=x
			a.set_pos(centerx,centery)
			a.damage=self.damage
			self.gunlist.add(a)
			
class EnemyGun(Gun):
		
	def shoot(self,rect):
		a=self.bullet(self.gunlist)
		a.set_pos(rect.centerx,rect.centery)
		a.damage=self.damage
		self.gunlist.add(a)

		