#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	The Menu.
#
#       Its a generic menu object, it takes 1 parameter, and thats an array of strings to display
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random
import globalvars

##takes a tuple of menuitem strings as input
#a generic menu class
#very effective
class Menu:
    def __init__(self, menuitems):
        self.font_size=45 #these do fairly obvious things
	self.offset_x=100
	self.offset_y=200
        self.spacing=10
        self.selection=0
        self.font = pygame.font.Font(globalvars.defaultfont,self.font_size)
        self.menuimgs=[]
        self.menurects=[]
        x=0
        for menuitem in menuitems:    #render all the strings that were inputted
            menuimg=self.font.render(menuitem, 1, globalvars.menucolor)
            menurect=menuimg.get_rect()
            if not self.menuimgs:
                menurect.move_ip(self.offset_x,self.offset_y)
            else:
                menurect.move_ip(self.offset_x,self.menurects[x-1].bottom+self.spacing)
            self.menuimgs.append(menuimg)
            self.menurects.append(menurect) 
            x+=1

	self.menurect=pygame.Rect(self.menurects[0].topleft,self.menurects[len(self.menurects)-1].bottomright)
	self.selectedrect=pygame.Rect(self.menurect.left-60,self.menurect.top,50,self.menurect.height)
	self.selectedimg=pygame.Surface(self.selectedrect.size)
	self.shipimg=pygame.transform.rotate(globalvars.playership[0],-90)
	self.move=self.menurects[0].height+self.spacing
	self.selectedimg.blit(self.shipimg,pygame.Rect(0,self.selection*self.move,50,50))
	x=0
	for menuimg in self.menuimgs:   #draw all the images to the display
            globalvars.surface.blit(menuimg,self.menurects[x])
            x+=1
	globalvars.surface.blit(self.selectedimg,self.selectedrect)
	globalvars.surface.blit(globalvars.logo,globalvars.logo.get_rect())
	pygame.display.flip()

    #generic selection changing class, not really used by outside
    #unless they know what they're doing
    def change_selection(self,selection):
        self.selectedimg.fill(globalvars.bgcolor)
        self.selectedimg.blit(self.shipimg,pygame.Rect(0,selection*self.move,50,50))
        globalvars.surface.blit(self.selectedimg,self.selectedrect)
        pygame.display.update(self.selectedrect)

     #simple methods to move selction up or down
    def change_selection_up(self):
        if self.selection >0:
            self.selection-=1
        self.change_selection(self.selection)

    def change_selection_down(self):
        if self.selection <len(self.menurects):
            self.selection+=1
        self.change_selection(self.selection)

    #a mouse oritened change_selection
    def change_selection_pos(self, pos):
        changed=False
        x=0
        for menuitem in self.menurects:
            if menuitem.collidepoint(pos):
                if self.selection!=x:
                    self.selection=x
                    changed=True
            x+=1
        if changed:
            self.change_selection(self.selection)

    #useful so that a random mouseclick doesnt do anything
    def mouse_is_anywhere(self,pos):
        for menuitem in self.menurects:
            if menuitem.collidepoint(pos):
                return True
        return False

    #returns selection (duh)
    def get_selection(self):
        return self.selection

#i'll do these later
    
    def disp_about(self):
        return

    def disp_help(self):
        return
    
        
	
    
