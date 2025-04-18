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
    img_rct = img.get_rect()
    tmr = 0
    img_rct.center = 300,200 
    x = -1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_lst = pg.key.get_pressed()
        
        
        x=key_lst[pg.K_RIGHT]*2-key_lst[pg.K_LEFT]-1
        y=key_lst[pg.K_DOWN]-key_lst[pg.K_UP]
        
        img_rct.move_ip((x,y))


        screen.blit(original1, [-tmr, 0])
        screen.blit(flipped1, [1600-tmr, 0])
        screen.blit(original2, [3200-tmr, 0])
        screen.blit(img,img_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)
        if tmr == 3200:
            tmr=0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()