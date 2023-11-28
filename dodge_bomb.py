import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

delta = {
    pg.K_UP:(0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0)
}

def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数 rctはこうかんとんor爆弾SurfaceのRect
    戻り値: 横方向、縦方向判定結果(画面内:True/画面外:False)
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:  # 横はみだし判定
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  # 縦はみだし判定
        tate = False
    return (yoko, tate)


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 1.0)
    
    lst=[]
    x=0
    for i in range(8):  
        kk = pg.transform.rotozoom(kk_img, x, 2.0)
        lst.append(kk)
        x += 45

    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400  #コウカトン初期座標
    bomb = pg.Surface((20, 20))  # 練習1:透明のSurfaceを作る
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)  # 練習1:半径10の円を生成

    bomb_rct = bomb.get_rect()  #練習2:爆弾を
    bomb_rct.centerx = random.randint(0, WIDTH)
    bomb_rct.centery = random.randint(0, HEIGHT)
    bomb.set_colorkey((0, 0, 0))
    vx, vy = +5, +5  # 横速度、縦速度

    clock = pg.time.Clock()
    tmr = 0  
    s=0  # リストの変数の初期値
    time = 50  # 爆弾時間の初期値
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bomb_rct):  # 爆弾が当たると
            kk_img = pg.image.load("ex02/fig/4.png")
            kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
            time = 0  #爆弾に当たって時間を0にして下のGameOverを発動させるため
        if time == 30:
            print("GameOver")
            return
        time += 1
        
        key_lst= pg.key.get_pressed()
        sum_mv = [0,0]
        for k, tpl in delta.items():
            if key_lst[k]:  # 練習2　キーが押されたら
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]  

                if sum_mv[0] == -5 and sum_mv[1] == 5:
                    s = 1
                elif sum_mv[0] == 0 and sum_mv[1] == 5:
                    s = 2
                elif sum_mv[0] == 5 and sum_mv[1] == 5:
                    s = 3
                elif sum_mv[0] == 5 and sum_mv[1] == 0:
                    s = 4
                elif sum_mv[0] == 5 and sum_mv[1] == -5:
                    s = 5
                elif sum_mv[0] == 0 and sum_mv[1] == -5:
                    s = 6
                elif sum_mv[0] == -5 and sum_mv[1] == -5:
                    s = 7
                else:
                    s = 0

        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])

        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        newimg = lst[s]
        if time <= 30:
            newimg = kk_img
        screen.blit(newimg, kk_rct)

        # 爆弾
        bomb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bomb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bomb_rct.move_ip(vx, vy)
        
        screen.blit(bomb, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()