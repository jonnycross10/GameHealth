import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

running = True
while running:
	screen.fill((0,255,255))

	pygame.draw.rect(screen,(0,255,0), (100,100,100,50), 75)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	

pygame.quit()
