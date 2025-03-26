import pygame as py
import math
import random

py.init()

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
RANDOM_COLOR = random.randrange(10, 240)
RANDOM_COLOR_1 = random.randrange(10, 240)
RANDOM_COLOR_2 = random.randrange(10, 240)

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Gravitational Planet Sim")
clock = py.time.Clock()

G = 0.1
frame_count = 0

def calculate_initial_velocity(new_planet, planets,G):
    """Calculates and sets the initial velocity for a new planet."""

    closest_planet = planets[0]
    closest_distance = float('inf')
    for planet in planets:
        dx = new_planet["position"][0] - planet["position"][0]
        dy = new_planet["position"][1] - planet["position"][1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance < closest_distance:
            closest_distance = distance
            closest_planet = planet

    if closest_distance != 0:
        orbital_velocity = math.sqrt((G * closest_planet["mass"]) / closest_distance)
        perpendicular_x = -(new_planet["position"][1] - closest_planet["position"][1])
        perpendicular_y = new_planet["position"][0] - closest_planet["position"][0]
        magnitude = math.sqrt(perpendicular_x**2 + perpendicular_y**2)
        if magnitude != 0:
            perpendicular_x /= magnitude
            perpendicular_y /= magnitude
            new_planet["velocity"] = [perpendicular_x * orbital_velocity, perpendicular_y * orbital_velocity]
    else:
        new_planet["velocity"] = [0, 0]

# Initial Planets
planets = [
    {
        "position": [400, 300],
        "mass": 400,
        "velocity": [0, 0],
        "color": (0, 0, 255)
    }
]

# Set initial velocity for the orbiting planet


running = True

while running:

    clock.tick(60)
    screen.fill(BLACK)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = py.mouse.get_pos()
            new_planet = {
                "position": [mouse_X, mouse_Y],
                "mass" : random.randrange(10,40),
                "velocity": [0,0],
                "color" :(random.randrange(10,240),random.randrange(10,240),random.randrange(10,240))
            }

            calculate_initial_velocity(new_planet, planets,G)
            planets.append(new_planet)
    
    # Calculation for Gravitionl forces that updates Velocity
    for i,planet1 in enumerate(planets):
        force_x = 0
        force_y = 0
        for j,planet2 in enumerate(planets):
            if i != j: # Do not apply planet to itself.
                dx = planet2["position"][0] - planet1["position"][0]
                dy = planet2["position"][1] - planet1["position"][1]
                R = math.sqrt(dx**2 + dy**2)
                if R !=0:
                    force = G * planet1["mass"] * planet2["mass"] / R**2
                    force_x += force * dx / R
                    force_y += force * dy / R

        #Apply total force to velocity.
        planet1["velocity"][0] += force_x / planet1["mass"]
        planet1["velocity"][1] += force_y / planet1["mass"]
        

            
    # Update and draw plants
    for planet in planets:
        planet["position"][0] += planet["velocity"][0]
        planet["position"][1] += planet["velocity"][1]
        py.draw.circle(screen, planet["color"], (int(planet["position"][0]), int(planet["position"][1])), int(math.sqrt(planet["mass"])))

    py.display.flip()