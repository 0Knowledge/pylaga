#2007-04-1 RJ Marsan
#Pylaga
#Original: 2007-02-20 Derek Mcdonald 
#Subclass of pylaga.py
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
				