from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
theta = 0
while True:
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)

    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)

    while (x > 30):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)


    while (theta < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + 200 * math.cos(math.radians(theta)), 200 + 200 * math.sin(math.radians(theta)))
        theta = theta + 2
        delay(0.01)

    theta = 0

    
close_canvas()
