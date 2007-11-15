#!/usr/bin/env python
#Galaga VERSION .12!
#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Main class
#######################################################################
#    This file is part of pylaga.  in fact its the main file of pylaga
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
import os, sys
#little fix so py2exe can find the right modules
ROOTDIR=os.getcwd()
sys.path.append(ROOTDIR) 
try:
	import pygame,math, random
	from pygame.locals import*
	import globalvars
	from bullet import Bullet, EnemyBullet
	from background import BackgroundManager
	from enemy import Enemy, EnemyManager
	from player import Player
	from stage import Stage
	from display import *
	from menu import Menu
	from game import Gamelolz
	from menulists import MenuLists, menulists
	from inputmanager import InputManager
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
		global inputmanager #because everyone should be able to access it.
		self.inputmanager=InputManager(self.game)
		#pygame.register_quit(self.inputmanager.sysexit)
		self.menu.init_menu()
		self.game.start()
		while self.menu.exit_menu(self.game.points):
			self.game.start()
		

##the one line that starts the game
#if __name__ == "__main__":
#	lolz=pylaga()
lolz=pylaga()
