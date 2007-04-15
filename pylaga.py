#!/usr/bin/env python
#Galaga VERSION .12!
#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Main class
#################################################################################################################
#
#
#	This is the main class. the class that superceedes all other classes.
#	Its short and sweet but thats the point
#
#general exception handler
#(because if theres an error in any of these imports itll just die w/o warning)
def exception_handler():
    import traceback,sys
    type, info, trace = sys.exc_info()
    tracetop = traceback.extract_tb(trace)[-1]
    tracetext = 'File %s, Line %d' % tracetop[:2]
    if tracetop[2] != '?':
        tracetext += ', Function %s' % tracetop[2]
    exception_message = '%s:\n%s\n\n%s\n"%s"'
    message = exception_message % (str(type), str(info), tracetext, tracetop[3])
    if type not in (KeyboardInterrupt, SystemExit):
        print message
    raise

#import pygame os and sys libraries
try:
	import pygame, os, sys, math, random
	from pygame.locals import*
	import globalvars
	from bullet import Bullet, EnemyBullet
	from background import BackgroundManager, bgstars
	from enemy import Enemy, EnemyManager
	from player import Player
	from stage import Stage
	from display import *
	from menu import Menu
	from game import Gamelolz
	from menulists import MenuLists, menulists
except:
	exception_handler()
	sys.exit(0)

if not pygame.font: print 'Warning, fonts disabled'
#################################################################################################################
#
#
#	simple class to manage the entire game..... it helps with organization
#
#
class pylaga:
	def __init__(self):
		self.game=Gamelolz(self)
		self.menu=menulists
		
		self.menu.init_menu()
		self.game.start()
		while self.menu.exit_menu(self.game.points):
			self.game.start()
		

##the one line that starts the game
#if __name__ == "__main__":
#	lolz=pylaga()
lolz=pylaga()