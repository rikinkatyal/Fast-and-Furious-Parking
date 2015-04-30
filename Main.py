from pygame import *

from Game import *
from time import time as cTime

init()

screen = display.set_mode((1024,768))
display.set_caption("Fast and Furious Parking")
game = Game(screen)
running = True
menuScreen = False
levelScreen = False
gameScreen = True
fpsfont = font.SysFont("monospace", 15)
gameCount = 1

mClock = time.Clock()

while running:
	for e in event.get():
		if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
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
	if menuScreen:
		pass
	elif levelScreen:
		pass
	elif gameScreen:
		if gameCount:
			game.sTime(cTime())
			gameCount = 0
		game.run()

	mClock.tick(72)

	fps = fpsfont.render(str("FPS: %.4f" % mClock.get_fps()), 1, (255,255,255))
	screen.blit(fps, (900, 10))

	display.flip()
quit()