#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
#################################################################################################################
#
#	A simple bullet class, and a subclass, EnemyBullet
#
#
#
#
#import pygame os and sys libraries
import pygame, os, sys, math, random, globalvars

#cuz pygame doesnt have keyhold:


class InputManager:
	KEYHOLD=1339
	def __init__(self,parent):
		self.p=parent
		self.keydowndict={}
		self.keyupdict={}
		self.keyholddict={}
		self.mousemovedict={}
		self.mouseclickdict={}
		self.keyhold=[]
		
	def registerEvent(self,eventtype,event,reaction):
		if eventtype == pygame.KEYDOWN:
			dict=self.keydowndict
		if eventtype == pygame.KEYUP:
			dict=self.keyupdict
		if eventtype == InputManager.KEYHOLD:
			dict=self.keyholddict
		if eventtype == pygame.MOUSEMOTION:
			dict=self.mousemovedict
			if event=="all":
				event=[(0,0,0),(0,1,0),(1,0,1),(0,0,1),(0,1,1),(1,1,1),(1,0,0),(1,1,0)]
		if eventtype == pygame.MOUSEBUTTONDOWN:
			dict=self.mouseclickdict
			if event=="all":
				event=[1,2,3]
		
		
		if type(event) == type(1):
			if dict.has_key(event):
				print "overriding event %s"%event
			dict[event]=reaction
		else:
			for e in event:
				dict[e]=reaction
		print "registering new event(s) %s for %s"%(event,reaction)

			
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
			
				
				
	def standardInputs(self):
		self.registerEvent(pygame.KEYDOWN,pygame.K_q,self.sysexit)
		self.registerEvent(pygame.KEYDOWN,pygame.K_ESCAPE,self.sysexit)
		
		
		
	#a few standard inputs	
	def mousemove(self,p):
		tempx=pygame.mouse.get_pos()[0]-p.player.rect.width/2
		## Just to make sure we don't get the ship way out there:
		if tempx > globalvars.xmax: #if its outside the globalvars.window, just stick it as far as possible
			p.player.move(globalvars.xmax,globalvars.y)
		elif tempx < globalvars.xmin:
			p.player.move(globalvars.xmin,globalvars.y)
		elif abs(tempx-globalvars.x) > globalvars.smooth_scroll_var1:  #smooth scrolling if the mouse gets far from the ship
			p.player.move(p.player.get_pos().left+(tempx-p.player.get_pos().left)/globalvars.smooth_scroll_var2,globalvars.y)
		else:		#if it gets down to this point, 
				#we've passed all sanity checks so just move it
			p.player.move(tempx,globalvars.y)
	
	def playershoot(self,p):
		p.pshoot()
			
			
			
			
			
			
			
			
			
			
					#if event.type == pygame.QUIT:
				#sys.exit(0)
			#if event.type == pygame.MOUSEMOTION:
				#pygame.event.get()
				#tempx=pygame.mouse.get_pos()[0]-self.player.rect.width/2
				### Just to make sure we don't get the ship way out there:
				#if tempx > globalvars.xmax: #if its outside the globalvars.window, just stick it as far as possible
					#self.player.move(globalvars.xmax,globalvars.y)
				#elif tempx < globalvars.xmin:
					#self.player.move(globalvars.xmin,globalvars.y)
				#elif abs(tempx-globalvars.x) > globalvars.smooth_scroll_var1:  #smooth scrolling if the mouse gets far from the ship
					#self.player.move(self.player.get_pos().left+(tempx-self.player.get_pos().left)/globalvars.smooth_scroll_var2,globalvars.y)
				#else:		#if it gets down to this point, 
						##we've passed all sanity checks so just move it
					#self.player.move(tempx,globalvars.y)
						
			### if the mouse is clicked, shoot!
			#if event.type == pygame.MOUSEBUTTONDOWN:
				#self.pshoot()
			
			### if 'q' is pressed, quit
			#if event.type == pygame.KEYDOWN:
				#if event.key == pygame.K_q:
					#sys.exit(0)
				#if event.key == pygame.K_p:
					#menulists.pause_menu()
				#if event.key == pygame.K_ESCAPE:
					#sys.exit(0)
				##keyboard controls
				#if event.key == pygame.K_LEFT:
					#self.leftkeydown=1
				#if event.key == pygame.K_RIGHT:
					#self.rightkeydown=1
				#if event.key == pygame.K_SPACE:
					#self.pshoot()

			
			##keyboard controls
			#if event.type == pygame.KEYUP:
				#if event.key == pygame.K_LEFT:
					#self.leftkeydown=0
				#if event.key == pygame.K_RIGHT:
					#self.rightkeydown=0	
		
					
		#if self.leftkeydown: self.player.move_one(0)
		#if self.rightkeydown: self.player.move_one(1)
		
		#pygame.event.clear()
		
	def sysexit(self,p):
		sys.exit(0)
	def die(self,p):
		sys.exit(1)