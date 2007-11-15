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
#	A few premade menu objects
#
#       Makes it easier on my brain
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars
from menu import Menu
from inputmanager import InputManager

##takes a tuple of menuitem strings as input
#a generic menu class
#very effective (hah. not anymore bitches!)
class MenuLists:
            ############the menu functions###########
	def init_menu(self):
                self.clear_screen()
		menu=Menu(("Play!","About","Help","Exit"))
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        sys.exit(0)
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
	def exit_menu(self,points):
                self.clear_screen()
                pygame.mouse.set_visible(1)
		menu=Menu(("Again?","About","Help","Exit","!Score: %s"%points.get_points()))
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        return False
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		return True


	def pause_menu(self,**kwargs):
                #self.clear_screen()
                pygame.mouse.set_visible(1)
		pygame.event.set_grab(0)
		menu=Menu(("Resume","About","Help","Exit"),45,globalvars.logo)
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
                                if selection == 1:
                                        menu.disp_special(self.about_menu)
                                if selection == 2:
                                        menu.disp_special(self.help_menu)
                                if selection == 3:
                                        sys.exit(0)
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
	#This one is different from teh above 3
	#it is a wrapper for a submenu thats just text and a back command
	def special_menu(self,menuarray):
		menu=Menu(menuarray,30,globalvars.logo)
		selection=-1
		while True:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
                                if selection == 0:
                                        break
			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		
	def about_menu(self):
		self.special_menu(("!This is a small galaga clone written in Python","!Written By:","!     RJ Marsan","!Original:","!     Derek Mcdonald","!Version: %s"%globalvars.VERSION,"!","Back"))
	
	def help_menu(self):
		self.special_menu(("!Help:","!     Left: Left Arrow or Mouse","!     Right: Right Arrow or Mouse","!     Shoot: Space or Mouse Left","!     Pause: p","!     Exit: q or esc","!","Back"))
		
	#NOT DONE YET
	def buy_menu(self,menulist):
                #self.clear_screen()
                pygame.mouse.set_visible(1)
		pygame.event.set_grab(0)
		menuarry=[]
		execarry=[]
		for (a,b) in menulist:
			menuarry.append(a)
			execarry.append(b)
		menu=Menu(menuarry,30,globalvars.logo)
		selection=-1
		goagain=True
		while goagain:
			events=pygame.event.get()
			selection=self.menu_action(events,menu)
			if selection >= 0:
				exec execarry[selection]

			menu.render()
			globalvars.clock.tick(globalvars.FPS)
		self.clear_screen()
		pygame.mouse.set_visible(0)
		pygame.event.set_grab(1)
		
		
	#generic processor of inputs. bwaha.
	#hah omgpwneddeprecated
	def menu_action(self, events, menu):
                selection=-1
                pygame.event.pump()
                for event in events:
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        sys.exit(0)
				if event.key == pygame.K_ESCAPE:
					sys.exit(0)
                                if event.key == pygame.K_UP:
                                        menu.change_selection_up()
                                if event.key == pygame.K_DOWN:
                                        menu.change_selection_down()
                                if event.key == pygame.K_RETURN:
                                        selection=menu.get_selection()
                        if event.type == pygame.MOUSEMOTION:
                                menu.change_selection_pos(event.pos)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                menu.change_selection_pos(event.pos)
                                if menu.mouse_is_anywhere(event.pos):
                                        selection=menu.get_selection()
                return selection
        ############the menu functions###########
	
	def clear_screen(self):
                globalvars.surface.fill(globalvars.bgcolor)
		pygame.display.flip()

#since this object only really needs to be made once:
global menulists
menulists=MenuLists()