from pygame import *

from Game import *

init()

screen = display.set_mode((1024,768))
game = Game(screen)
running = True
fpsfont = font.SysFont("monospace", 15)

mClock = time.Clock()

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

	mClock.tick(60)

	fps = fpsfont.render(str("%.4f" % mClock.get_fps()), 1, (255,255,255))
	screen.blit(fps, (950, 10))

	display.flip()
quit()