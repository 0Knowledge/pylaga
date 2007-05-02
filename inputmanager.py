#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
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
		self.keyhold=[]
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
				self.keyhold.append(event.key)
				if event.key in self.keydowndict:
					#print self.keydowndict[event.key]
					self.keydowndict[event.key](self.p)
			if event.type==pygame.KEYUP:
				try: self.keyhold.remove(event.key);
				except: pass;
				if event.key in self.keyupdict:
					#print self.keyupdict[event.key]
					self.keyupdict[event.key](self.p)
			if event.type==pygame.MOUSEMOTION:
				if event.buttons in self.mousemovedict:
					self.mousemovedict[event.buttons](self.p)
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button in self.mouseclickdict:
					self.mouseclickdict[event.button](self.p)
					
		for event in self.keyhold:
			if event in self.keyholddict:
				self.keyholddict[event](self.p)
			
				
	#just to clean things up	
	def standardInputs(self):
		self.registerEvent(pygame.KEYDOWN,pygame.K_q,self.sysexit)
		self.registerEvent(pygame.KEYDOWN,pygame.K_ESCAPE,self.sysexit)
	
	#a few essential inputs
	def null(self,p):
		pass		
	def sysexit(self,p):
		sys.exit(0)
	def die(self,p):
		sys.exit(1)