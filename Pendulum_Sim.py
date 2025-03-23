import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum Simulation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def pendulum_simulation(theta0, time_span, dt):
    """Simulates a simple pendulum."""
    g = 9.8  # Acceleration due to gravity
    L = 1.0  # Length of the pendulum
    time = np.arange(0, time_span, dt)
    theta = np.zeros_like(time)
    theta[0] = theta0
    omega = 0.0  # Angular velocity

    for i in range(1, len(time)):
        alpha = -g / L * np.sin(theta[i - 1])  # Angular acceleration
        omega += alpha * dt
        theta[i] = theta[i - 1] + omega * dt

    return time, theta

theta0 = np.pi / 4
time_span = 10.0
dt = 0.01

time, theta = pendulum_simulation(theta0, time_span, dt)

i = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if i < len(time):
        x = WIDTH // 2 + int(200 * np.sin(theta[i]))
        y = HEIGHT // 4 + int(200 * np.cos(theta[i]))

        pygame.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT // 4), (x, y), 2)
        pygame.draw.circle(screen, RED, (x, y), 20)

        i += 1
    else:
        i=0

    pygame.display.flip()
    clock.tick(1 / dt)

pygame.quit()