import pygame
import math

def collision(line_start, line_end, circle_center, circle_radius):
    x1, y1 = line_start
    x2, y2 = line_end
    cx, cy = circle_center
    r = circle_radius

    # Used to find t which should be distance between the circle center and the line
    t = ((cx - x1) * (x2 - x1) + (cy - y1) * (y2 - y1)) / ((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Clamp t to [0, 1]
    t = max(0, min(1, t))

    # Calculate closest point
    closest_x = x1 + t * (x2 - x1)
    closest_y = y1 + t * (y2 - y1)

    # Calculate distance
    distance = math.sqrt((closest_x - cx) ** 2 + (closest_y - cy) ** 2)

    # Check for collision
    return distance <= r


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("simple Motion")

#intial position
x = 400
y = 150

circle_center = [x, y]
line_start = (0 , 500)
line_end = (WIDTH, 500)
c_radius = 20

velocity = 0.5    
gravity = 0.5
running = True
cor = 0.9

while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    screen.fill((255,255,255))

    pygame.draw.line(screen, (0,0,0), line_start, line_end, 2)
    pygame.draw.circle(screen, (0,0,255), circle_center, c_radius)
    
    next_y = circle_center[1] + gravity + velocity

    if collision(line_start, line_end, [circle_center[0], next_y], c_radius):
            circle_center[1] = line_start[1] - c_radius
            velocity = -velocity * cor
           
    else:
        velocity += gravity
        circle_center[1] += velocity 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip() #used to update the screen