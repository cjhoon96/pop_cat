import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((680,665))

pop_open = pg.image.load("./pop_img/popcat_open.png")
pop_close = pg.image.load("./pop_img/popcat_close.png")
open_sound = pg.mixer.Sound("./pop_sound/pop_open")

scr = pop_open

done = False
click = False
while not done:
    screen.fill((0,0,0))
    
    screen.blit(scr, (0,0))
    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:# If user release what he pressed.
            click = True
        elif event.type == pg.MOUSEBUTTONUP:# If user press any key.
            click= False
        elif event.type == pg.QUIT: # If user clicked close.
            done= True 

    if click:
        scr = pop_open
        screen.fill((0,0,0))
        screen.blit(scr, (0,0))
        pg.display.flip()
        pygame.mixer.Sound.play(open_sound)
    elif not click:
        scr = pop_close
        screen.fill((0,0,0))
        screen.blit(scr, (0,0))
        pg.display.flip()


pg.quit()
sys.exit()
