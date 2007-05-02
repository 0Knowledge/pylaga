import pygame
from inputmanager import InputManager
from menulists import menulists
def setup(p,game):
	p.registerEvent(pygame.KEYDOWN,pygame.K_q,p.sysexit)
	p.registerEvent(pygame.KEYDOWN,pygame.K_ESCAPE,p.sysexit)
	p.registerEvent(pygame.MOUSEMOTION,"all",p.mousemove)
	p.registerEvent(pygame.MOUSEBUTTONDOWN,1,p.playershoot)
	p.registerEvent(pygame.KEYDOWN,pygame.K_SPACE,p.playershoot)
	p.registerEvent(InputManager.KEYHOLD,pygame.K_LEFT,game.player.move_one_left)
	p.registerEvent(InputManager.KEYHOLD,pygame.K_RIGHT,game.player.move_one_right)
	p.registerEvent(pygame.KEYDOWN,pygame.K_p,menulists.pause_menu)