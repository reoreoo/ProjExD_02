import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bomb = pg.Surface((20, 20))  # 練習1:透明のSurfaceを作る
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)  # 練習1:半径10の円を生成
    bomb_rct = bomb.get_rect()  #練習2:爆弾を
    bomb_rct.centerx = random.randint(0, WIDTH)
    bomb_rct.centery = random.randint(0, HEIGHT)
    bomb.set_colorkey((0, 0, 0))
    vx, vy = +5, +5


    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bomb_rct.move_ip(vx, vy)
        screen.blit(bomb, bomb_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()