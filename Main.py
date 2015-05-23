from pygame import *

from Menu import *
from Level import *
from Game import *
from time import time as cTime

init()

screen = display.set_mode((1024,768))
display.set_caption("Fast and Furious Parking")
menu = Menu(screen)
running = True
menuScreen = True
gameScreen = False
fpsfont = font.SysFont("monospace", 15)
road = image.load("res/road_texture.png")
gameCount = 1
mClock = time.Clock()
down = False

while running:
	for e in event.get():
		if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
			running = False
		if e.type == MOUSEBUTTONDOWN:
			down = True
		elif e.type == MOUSEBUTTONUP:
			down = False
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
			if e.key == K_t:
				game.lifeCount = 5
			if e.key == K_r:
				game = Game(screen)
				gameCount = 1

	if menuScreen:
		menu.render(down)
		if not menu.isRunning():
			game = Game(screen)
			gameScreen = True
			menuScreen = False
	elif gameScreen:
		screen.fill((140,140,140))
		if gameCount:
			game.sTime(cTime())
			gameCount = 0
		game.run()

	if down:
		down = False

	mClock.tick(120)

	fps = fpsfont.render(str("FPS: %.4f" % mClock.get_fps()), 1, (255,255,255))
	screen.blit(fps, (900, 10))

	display.flip()
quit()