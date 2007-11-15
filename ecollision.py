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
#	A much improved collision detection program
#
#
#
#
################

TOP=0
BOTTOM=1
RIGHT=2
LEFT=3

def spritecollide(sprite, group, die1, direction):
	returnarray=[]
	if direction == TOP:
		for a in group:
			if sprite.rect.top < a.rect.bottom:
				#print "Ah fuck this: %s"%a.rect
				#break  ## the key line that makes everything faster
				if sprite.rect.colliderect(a):
					#print "die %s"%a.rect
					returnarray.append(a)
			#print "next"
	elif direction == BOTTOM:
		for a in group:
			if sprite.rect.bottom > a.rect.top:
				#break  ## the key line that makes everything faster
				if sprite.rect.colliderect(a):
					#print "die %s"%a.rect
					returnarray.append(a)
			#print "next"
			#else:
				#print "Exiting loop at:%s"%a.rect
	
	elif direction == RIGHT:
		for a in group:
			if sprite.rect.left < a.rect.left:
				if sprite.rect.colliderect(a.rect):
					returnarray.append(a)
				
	elif direction == LEFT:
		for a in group:
			if sprite.rect.left > a.rect.left:
				if sprite.rect.colliderect(a.rect):
					returnarray.append(a)

	if die1:
		for a in returnarray:
			group.remove(a)
	return returnarray

def groupcollide(group1, group2, die1, die2, direction):
	returnlist={}
	for g in group1:
		a=spritecollide(g, group2, die2, direction)
		for b in a:
			returnlist[g]=b
	return returnlist
		

def spritecollide2(sprite, group, die1, direction):
	returnarray=[]
	if direction == TOP:
		for a in group:
			if sprite.rect.top > a.rect.bottom:
				break
				#print "Ah fuck this: %s"%a.rect
				#break  ## the key line that makes everything faster
			if sprite.rect.colliderect(a):
				#print "die %s"%a.rect
				returnarray.append(a)
			#print "next"
	elif direction == BOTTOM:
		for a in group:
			if sprite.rect.bottom < a.rect.top:
				#print "giving up"
				break  ## the key line that makes everything faster
			if sprite.rect.colliderect(a):
				#print "die %s"%a.rect
				returnarray.append(a)
			#print "next"
			#else:
				#print "Exiting loop at:%s"%a.rect
	
	#elif direction == RIGHT:
		#for a in group:
			#if sprite.rect.left < a.rect.left:
				#if sprite.rect.colliderect(a.rect):
					#returnarray.append(a)
				
	#elif direction == LEFT:
		#for a in group:
			#if sprite.rect.left > a.rect.left:
				#if sprite.rect.colliderect(a.rect):
					#returnarray.append(a)

	if die1:
		for a in returnarray:
			group.remove(a)
	return returnarray
		
def groupcollide2(group1, group2, die1, die2, direction):
	returnlist={}
	for g in group1:
		a=spritecollide2(g, group2, die2, direction)
		for b in a:
			returnlist[g]=b
	return returnlist
	