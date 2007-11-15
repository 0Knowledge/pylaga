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
#	The Menu.
#
#       Its a generic menu object, it takes 1 parameter (or more but they are optional), and thats an array of strings to display
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars

##takes a tuple of menuitem strings as input
#a generic menu class
#very effective
#not very powerful
#a string starting with "!" is not selectable
class Menu:
	def __init__(self, menuitems,fontsize=45,logo=globalvars.logo,fadein=True, selector=globalvars.playership[0]):
		self.menusurface=pygame.Surface((globalvars.WIN_RESX,globalvars.WIN_RESY))
		self.menusurfacerect=self.menusurface.get_rect()
		self.font_size=fontsize #these do fairly obvious things
		self.font = pygame.font.Font(globalvars.defaultfont,self.font_size)
		self.offset_x=100
		self.offset_y=200
		self.spacing=10
		self.selection=0
		if fadein:
			self.fadein=10
		else:
			self.fadein=255
		self.fadeinmax=255
		self.fadeinspeed=5
		self.allobjects=[]
		self.logo=logo
		self.logorect=self.logo.get_rect()
		self.selector=selector
		self.allobjects.append(self.logorect)
		self.menuitems=menuitems
		self.disp_menu(self.menuitems)
		
		
	def disp_menu(self,menuitems):
		self.menuimgs=[]
		self.menurects=[]
		self.selectionlist=[]
		x=0
		for menuitem in menuitems:    #render all the strings that were inputted
			if menuitem.startswith("!"):
				menuimg=self.font.render(menuitem[1:], 1, globalvars.menucolor, globalvars.bgcolor)
			else:
				menuimg=self.font.render(menuitem, 1, globalvars.menucolor, globalvars.bgcolor)
			menurect=menuimg.get_rect()
			if not self.menuimgs:
				menurect.topleft=(self.offset_x,self.offset_y)
				#print "The first menurect is at %s"%menurect
			else:
				menurect.topleft=(self.offset_x,self.menurects[x-1].bottom+self.spacing)
				#print "The next  menurect is at %s"%menurect
			if not menuitem.startswith("!"): #if it doesnt start with '!', add it to the possible selectionlist
				self.selectionlist.append(menurect.top-self.offset_y)
			self.menuimgs.append(menuimg)
			self.menurects.append(menurect) 
			self.allobjects.append(menurect)
			x+=1
		
		self.menurect=pygame.Rect(self.menurects[0].topleft,self.menurects[len(self.menurects)-1].bottomright)
		self.selectedrect=pygame.Rect(self.menurect.left-60,self.menurect.top,50,self.menurect.height)
		self.allobjects.append(self.selectedrect)
		self.selectedimg=pygame.Surface(self.selectedrect.size)
		self.selectedimgrect=self.selectedimg.get_rect()
		self.shipimg=pygame.transform.rotate(self.selector,-90)
		self.move=self.menurects[0].height+self.spacing
		
		#fixes the odd bug of the selector appearing in odd spots
		self.change_selection(self.selection)
		
		x=0 #I know i can do enumerate but who cares.
		for menuimg in self.menuimgs:   #draw all the images to the display
			self.menusurface.blit(menuimg,self.menurects[x])
			#print "Displaying menu item at %s"%self.menurects[x]
			x+=1
		self.menusurface.blit(self.selectedimg,self.selectedrect)
		self.menusurface.blit(self.logo,self.logorect)
		#globalvars.surface.blit(self.menusurface,self.menusurfacerect)

		#pygame.display.flip()
	
	#generic selection changing class, not really used by outside
	#unless they know what they're doing
	def change_selection(self,selection):
		try:
			y=self.selectionlist[selection]
		except:
			#print "BAD SELECTION"
			#If we can't find anything to select, just choose the first one we can
			try:
				y=self.selectionlist[0]
				self.selection=0
			except:
				print "I give up, not displaying an image at all\n YOU SUCK"
				y=-50
		self.selectedimg.fill((0,0,0))
		self.selectedimg.blit(self.shipimg,pygame.Rect(0,y,50,50))
		#self.menusurface.blit(self.shipimg,pygame.Rect(self.selectedrect.left,self.selectionlist[selection],50,50))
		self.menusurface.blit(self.selectedimg,self.selectedrect)
		globalvars.surface.blit(self.menusurface,self.menusurfacerect)

		pygame.display.update(self.selectedrect)
	
	#simple methods to move selction up or down
	def change_selection_up(self):
		if self.selection >0:
			self.selection-=1
			self.change_selection(self.selection)
		
	def change_selection_down(self):
		if self.selection < len(self.selectionlist)-1:
			self.selection+=1
			self.change_selection(self.selection)
		
	#a mouse oritened change_selection
	def change_selection_pos(self, pos):
		changed=False
		x=0
		for menuitem in self.menurects:
			if menuitem.collidepoint(pos):
				if not self.menuitems[x].startswith("!"):
					if self.selection!=x:
						self.selection=x
						changed=True
			x+=1
		if changed:
			self.change_selection(self.selection)
			
		#just for shits and giggles:
		#self.selectedimgrect.topleft=pos
		#self.menusurface.blit(self.shipimg,self.selectedimgrect)
	
	#useful so that a random mouseclick doesnt do anything
	def mouse_is_anywhere(self,pos):
		for menuitem in self.menurects:
			if menuitem.collidepoint(pos):
				return True
		return False
	
	#returns selection (duh)
	def get_selection(self):
		return self.selection
	
	#this is a rather nasty hack
	#it calls the given function and rerenders the screen
	#in concept this should create a hierarchy of menus
	#but i still dont like the concept of requiring the menulist to pass it a function
	#change or something
	def disp_special(self,menufunction):
		#print "displaying about"
		#self.renderstr("This is a simple python game\nits a space shooter.\nWritten By: RJ Marsan\nOriginal: Derek Mcdonald",25)
		menufunction()
		self.rerender()
		return
	
	#updates the screen
	def render(self):
		if self.fadein < self.fadeinmax:
			self.menusurface.set_alpha(self.fadein,pygame.RLEACCEL)
			globalvars.surface.blit(self.menusurface,self.menusurfacerect)
			#pygame.display.update(self.allobjects)
			pygame.display.flip()
			self.fadein+=self.fadeinspeed
			
			
		return
	
	#redraws the screen entirely
	def rerender(self):
		globalvars.surface.blit(self.menusurface,self.menusurfacerect)
		pygame.display.flip()
	