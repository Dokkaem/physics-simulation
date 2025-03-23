import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rain drops")

raindrops =[]
num_raindrops = 10 


running = True


for _ in range(num_raindrops):
    x = random.randint(0, WIDTH)
    y = 0
    velocity = random.randrange(5,10)
    raindrops.append([x,y, velocity])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock = pygame.time.Clock()

    screen.fill((255,255,255))



    for raindrop in raindrops:
        raindrop[1] += raindrop[2]

        if raindrop[1] > HEIGHT:
            raindrop[1] = 0
            raindrop[0] = random.randint(0, WIDTH)
            raindrop[2] = random.randint(5,15)
        
        pygame.draw.circle(screen, (0,0,255), (raindrop[0],raindrop[1]),3)


    pygame.display.flip()
    clock.tick(60)