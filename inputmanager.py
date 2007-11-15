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
#	The Input manager, because we desperately needed it
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random, globalvars

class InputManager:
	#cuz pygame doesnt have keyhold:
	KEYHOLD=1339 #dont ask what it means
	
	def __init__(self,parent):
		self.p=parent
		self.keydowndict={}
		self.keyupdict={}
		self.keyholddict={}
		self.mousemovedict={}
		self.mouseclickdict={}
		self.keyhold={} # this Neeeeeds to be a dict, or else keys get stuck in the list more than once, and never let go
		self.standardInputs()
		
	def registerEvent(self,eventtype,event,reaction):
		if eventtype == pygame.KEYDOWN:
			dict=self.keydowndict
		elif eventtype == pygame.KEYUP:
			dict=self.keyupdict
		elif eventtype == InputManager.KEYHOLD:
			dict=self.keyholddict
		elif eventtype == pygame.MOUSEMOTION:
			dict=self.mousemovedict
			if event=="all":
				event=[(0,0,0),(0,1,0),(1,0,1),(0,0,1),(0,1,1),(1,1,1),(1,0,0),(1,1,0)]
		elif eventtype == pygame.MOUSEBUTTONDOWN:
			dict=self.mouseclickdict
			if event=="all":
				event=[1,2,3]
		
		
		if type(event) == type(1):
			#if dict.has_key(event):
			#	print "overriding event %s for %s"%(event,reaction)
			#else:
			#	print "registering new event(s) %s for %s"%(event,reaction)
			dict[event]=reaction
		else:
			for e in event:
				dict[e]=reaction
			#print "registering new event(s) %s for %s"%(event,reaction)

			
	def check(self,events):
		#pygame.event.pump()  #somewhere in their docs it said this line was a good idea
		for event in events:
			if event.type==pygame.KEYDOWN:
				self.keyhold[event.key]=True 
				if event.key in self.keydowndict:
					#print self.keydowndict[event.key]
					self.keydowndict[event.key](parent=self.p,event=event)
			if event.type==pygame.KEYUP:
				try: del self.keyhold[event.key];
				except: pass;
				if event.key in self.keyupdict:
					#print self.keyupdict[event.key]
					self.keyupdict[event.key](parent=self.p,event=event)
			if event.type==pygame.MOUSEMOTION:
				if event.buttons in self.mousemovedict:
					self.mousemovedict[event.buttons](parent=self.p,event=event)
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button in self.mouseclickdict:
					self.mouseclickdict[event.button](parent=self.p,event=event)
					
		for event in self.keyhold:
			if event in self.keyholddict.keys():
				self.keyholddict[event](parent=self.p,event=event)
			
				
	#just to clean things up	
	def standardInputs(self):
		self.registerEvent(pygame.KEYDOWN,pygame.K_q,self.sysexit)
		self.registerEvent(pygame.KEYDOWN,pygame.K_ESCAPE,self.sysexit)
	
	#a few essential inputs
	def null(self,parent,event):
		pass		
	def sysexit(self,parent,event):
		sys.exit(0)
	def die(self,parent,event):
		sys.exit(1)