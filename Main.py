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
				game.shift(1)
			if e.key == K_2:
				game.shift(2)
			if e.key == K_3:
				game.shift(3)
			if e.key == K_4:
				game.shift(4)
			if e.key == K_5:
				game.shift(5)
			if e.key == K_0:
				game.lifeCount = 0

	screen.fill((145,145,145))
	game.run()

	display.flip()
quit()