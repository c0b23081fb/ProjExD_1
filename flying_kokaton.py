import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img_rct = kk_img.get_rect()
    kk_img_rct.center = 300,200
    tmr = 0
   
    
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        xk = 0  #x軸
        yk = 0  #y軸
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg2_img,[x+1600,0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg2_img,[x+4800,0])
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            yk = -1
        if key_lst[pg.K_DOWN]:
            yk = +1
        if key_lst[pg.K_LEFT]:
            xk = -1
        if key_lst[pg.K_RIGHT]:
            xk = +2
        kk_img_rct.move_ip((xk-1,yk))
        
        
        screen.blit(kk_img,kk_img_rct)
       
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()