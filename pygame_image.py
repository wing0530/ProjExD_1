import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    original1 = pg.image.load("fig/pg_bg.jpg")
    flipped1 = pg.transform.flip(original1,True,False)
    original2 = pg.image.load("fig/pg_bg.jpg")
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(original1, [-tmr, 0])
        screen.blit(flipped1, [1600-tmr, 0])
        screen.blit(original1, [3200-tmr, 0])
        screen.blit(img,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()