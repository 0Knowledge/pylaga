import pygame
from inputmanager import InputManager
from menulists import menulists
def setup(p,game):
	p.registerEvent(pygame.KEYDOWN,pygame.K_q,p.sysexit)
	p.registerEvent(pygame.KEYDOWN,pygame.K_ESCAPE,p.sysexit)
	p.registerEvent(pygame.MOUSEMOTION,"all",game.mousemove)
	p.registerEvent(pygame.MOUSEBUTTONDOWN,1,game.pshoot)
	p.registerEvent(pygame.KEYDOWN,pygame.K_SPACE,game.pshoot)
	p.registerEvent(InputManager.KEYHOLD,pygame.K_LEFT,game.player.move_one_left)
	p.registerEvent(InputManager.KEYHOLD,pygame.K_RIGHT,game.player.move_one_right)
	p.registerEvent(pygame.KEYDOWN,pygame.K_p,menulists.pause_menu)