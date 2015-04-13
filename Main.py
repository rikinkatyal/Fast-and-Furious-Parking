from pygame import *

from Game import *


screen = display.set_mode((1024,768))
game = Game(screen)
running = True

while running:
	for e in event.get():
		if e.type == QUIT:
			running = False
		if e.type == KEYDOWN:
			if e.key == K_1:
				game.livesCt = 1
			if e.key == K_2:
				game.livesCt = 2
			if e.key == K_3:
				game.livesCt = 3
			if e.key == K_4:
				game.livesCt = 4
			if e.key == K_5:
				game.livesCt = 5
			if e.key == K_0:
				game.livesCt = 0

	screen.fill((145,145,145))
	game.run()

	display.flip()
quit()