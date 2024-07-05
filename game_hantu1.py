#step 1: import semua modul

import math as m
from pygame import *
font.init()
init() #instal penting2

#step 2 buat font
font1 = font.Font(None, 80) 
win = font1.render('WOOOooowwwww!KAMU LUMAYAN JUGA', True, (244, 104, 2))
lose = font1.render('DASAR BOT!', True, (180, 0, 0))

font2 = font.Font(None, 36)

#step 3: buat variable untuk simpen gambar
img_back = "hantubg.jpg"  # game background
img_pisau = "pisau.png"  # bullet
img_hero = "mc.png"  # hero
img_enemy = "hantu.png" # enemy
img_tombol = "tombol.png"

#step 4: buat karakter game -> buat kelas (object)
# parent class for other sprites
class character(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.kena_pisau = False

    # method drawing the character on the window
    def reset(self): #upload karakter in screen
        screen.blit(self.image, (self.rect.x,self.rect.y))
    def tabrakan(self, karakter_lain):
        return self.rect.colliderect(karakter_lain)
class main_player(character):
    def moving(self, speed):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= speed
        if keys[K_RIGHT] and self.rect.x < width-50: 
            self.rect.x += speed
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= speed
        if keys[K_DOWN] and self.rect.y < height-50: 
            self.rect.y+=speed
class enemy(character):
    def move_towards_player(self, Player, speed):
        dx, dy = self.rect.x - Player.rect.x, self.rect.y - Player.rect.y
        dist = m.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x -= dx * speed
        self.rect.y-=dy*speed
class wall():
    def __init__(self,x,y,width,height,color):
        self.rect = Rect(x,y,width,height)
        self.color = color
    def draw(self):
        draw.rect(screen,self.color,self.rect)
width = 850
height = 650

screen = display.set_mode((width,height))
display.set_caption("Horor Game")
background = transform.scale(image.load(img_back),(width,height))

hantu_width = 120
hantu_height = 120
hantu_speed = 5
hantu = enemy(img_enemy, 300, 300, hantu_width, hantu_height, hantu_speed)

mc_width = 45
mc_height = 45
mc_speed = 1
mc = main_player(img_hero, 130, 0, mc_width, mc_height, mc_speed)

pisau_width = 45
pisau_height = 45
pisau_speed = 0
pisau = character(img_pisau, 400, 300, pisau_width, pisau_height, pisau_speed)

tombol_width = 90
tombol_height = 90
tombol_speed = 0
tombol = character(img_tombol,430, 280, tombol_width, tombol_height, tombol_speed)

merah = (160, 14, 19)
hijau = (6, 255, 0)
din_1 = wall(0, 0, 8, 640, merah)
din_2 = wall(842, 0, 8, 640, merah)
din_3 = wall(0, 0, 120, 8, merah)
din_4 = wall(185, 0, 657, 8, merah)
din_5 = wall(0, 640, 630, 8, merah)
din_6 = wall(695, 640, 160, 8, merah)
din_7 = wall(115, 0, 8, 120, merah)
din_8 = wall(55, 50, 65, 8, merah)
din_9 = wall(55, 50, 8, 185, merah)
din_10 = wall(185, 0, 8, 60, merah)
din_11 = wall(185, 60, 160, 8, merah)
din_12 = wall(420, 60, 345, 8, merah)
din_13 = wall(765, 60, 8, 530, merah)
din_14 = wall(55, 585, 718, 8, merah)
din_15 = wall(55, 295, 8, 290, merah)
din_16 = wall(690, 590, 8, 58, merah)
din_17 = wall(115, 120, 580, 8, merah)
din_18 = wall(690, 120, 8, 415, merah)
din_19 = wall(120, 527, 575, 8, merah)
din_20 = wall(120, 460, 8, 70, merah)
din_21 = wall(320, 120, 8, 140, merah)
din_22 = wall(200, 460, 420, 8, merah)
din_23 = wall(612, 185, 8, 275, merah)
din_24 = wall(400, 185, 220, 8, merah)
din_25 = wall(200, 185, 120, 8, merah)
din_26 = wall(200, 185, 8, 80, merah)
din_27 = wall(200, 325, 8, 140, merah)
din_28 = wall(200, 320, 80, 8, merah)
din_29 = wall(265, 260, 8, 65, merah)
din_30 = wall(55, 380, 150, 8, merah)
din_31 = wall(120, 185, 8, 200, merah)
din_32 = wall(320, 255, 220, 8, merah)
din_33 = wall(540, 255, 8, 140, merah)
din_34 = wall(265, 385, 280, 8, merah)
din_kel = wall(630, 640, 60, 8, hijau)

fps = time.Clock()
run = True #penanda
while run:
    screen.blit(background, (0,0))
    hantu.reset()
    mc.reset()
    mc.moving(mc_speed)
    pisau.reset()
    tombol.reset()
    din_1.draw()
    din_2.draw()
    din_3.draw()
    din_4.draw()
    din_5.draw()
    din_6.draw()
    din_7.draw()
    din_8.draw()
    din_9.draw()
    din_10.draw()
    din_11.draw()
    din_12.draw()
    din_13.draw()
    din_14.draw()
    din_15.draw()
    din_16.draw()
    din_17.draw()
    din_18.draw()
    din_19.draw()
    din_20.draw()
    din_21.draw()
    din_22.draw()
    din_23.draw()
    din_24.draw()
    din_25.draw()
    din_26.draw()
    din_27.draw()
    din_28.draw()
    din_29.draw()
    din_30.draw()
    din_31.draw()
    din_32.draw()
    din_33.draw()
    din_34.draw()
    din_kel.draw()
    
    for e in event.get():
        if e.type == QUIT:
            quit()
    if mc.tabrakan(din_1) or mc.tabrakan(din_2) or mc.tabrakan(din_3) or mc.tabrakan(din_4) or mc.tabrakan(din_5) or mc.tabrakan(din_6) or mc.tabrakan(din_7) or mc.tabrakan(din_8) or mc.tabrakan(din_9) or mc.tabrakan(din_10) or mc.tabrakan(din_11) or mc.tabrakan(din_12) or mc.tabrakan(din_13) or mc.tabrakan(din_14) or mc.tabrakan(din_15) or mc.tabrakan(din_16 ) or mc.tabrakan(din_17) or mc.tabrakan(din_18) or mc.tabrakan(din_19) or mc.tabrakan(din_20) or mc.tabrakan(din_21) or mc.tabrakan(din_22) or mc.tabrakan(din_23) or mc.tabrakan(din_24) or mc.tabrakan(din_25) or mc.tabrakan(din_26) or mc.tabrakan(din_27) or mc.tabrakan(din_28) or mc.tabrakan(din_29) or mc.tabrakan(din_30) or mc.tabrakan(din_31) or mc.tabrakan(din_32) or mc.tabrakan(din_33) or mc.tabrakan(din_34):
        mc.rect.x = 130
        mc.rect.y = 0
    if mc.tabrakan(tombol):
        din_kel.rect.x = 1000
    display.update()
    fps.tick(100)