import pygame
import os
import sys

pygame.font.init()
pygame.mixer.init()
pygame.init()

HealthFont = pygame.font.SysFont("comicsans", 40)
WinnerFont= pygame.font.SysFont("comicsans", 70)
vel=5
bullet_vel= 10
Max_bullet= 4
FPS= 60
Lebar_layar, Tinggi_layar = 900 , 500 
window= pygame.display.set_mode((Lebar_layar, Tinggi_layar))
# border_left= pygame.rect(0, Tinggi_layar, 0, 0)

Yellow_hit= pygame.USEREVENT +1
Red_hit = pygame.USEREVENT +2
RedW= (255, 0, 0)
YellowW = (255, 255, 0)

#loader image
skala=(55, 45)
yellow_ship = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
red_ship = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
Space= pygame.image.load(os.path.join("Assets", "Space.png"))
hitsound=pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
firesound=pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))

#changing the scale
yellow_ship = pygame.transform.rotate(pygame.transform.scale(yellow_ship, skala), 90)
red_ship = pygame.transform.rotate(pygame.transform.scale(red_ship, skala), -90)
Space=pygame.transform.scale(Space, (Lebar_layar, Tinggi_layar))
            
def windows(red, yellow, red_bullet, yellow_bullet, red_heal, yellow_heal):
    window.fill((255,255,255))
    window.blit(Space, (0,0))
    red_health= HealthFont.render("Health: "+str(red_heal), 1, RedW )
    Yellow_health= HealthFont.render("Health: "+str(yellow_heal), 1, YellowW )
    for bullet in red_bullet:
        pygame.draw.rect(window, RedW, bullet)
        
    for bullet in yellow_bullet:
        pygame.draw.rect(window, YellowW, bullet)
    window.blit(Yellow_health, (Lebar_layar - Yellow_health.get_width() - 10, 10 ))
    window.blit(red_health, (10, 10))
    window.blit(yellow_ship, (yellow.x, yellow.y))
    window.blit(red_ship, (red.x,red.y))
    pygame.display.update()


def display_winner(text, warna):
    winner= WinnerFont.render(text, 1 , warna)
    window.blit(winner, (Lebar_layar//2 - winner.get_width()//2, Tinggi_layar//2 - winner.get_height()//2))
    pygame.display.update()
        


def bullet_handle(red, yellow , red_bullet, yellow_bullet):
    for bullet in red_bullet:
        bullet.x += bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_hit))
            red_bullet.remove(bullet)
        elif bullet.x > Lebar_layar:
            red_bullet.remove(bullet)   
    for bullet in yellow_bullet:
        bullet.x -= bullet_vel
        if red.colliderect(bullet) :
            pygame.event.post(pygame.event.Event(Red_hit))
            yellow_bullet.remove(bullet)   
        elif bullet.x < 0:
            yellow_bullet.remove(bullet)

def red_handle_movement(KeyPressed, red):
    if KeyPressed[pygame.K_a]: #kiri
        if red.x - vel < 0: 
            red.x -= red.x
        else:
            red.x-=vel

    if KeyPressed[pygame.K_d]: #kanan
        if red.x + vel > Lebar_layar -  skala[1] or red.x + vel > Lebar_layar/2 - skala[1]//2:
            red.x+= 0
        else:
            red.x+=vel

    if KeyPressed[pygame.K_s]: #bawah
        if red.y + vel > Tinggi_layar - skala[0]:
            red.y += 0
        else:
            red.y+=vel

    if KeyPressed[pygame.K_w]: #atas
        if red.y - vel < 0:
            red.y -= red.y 
        else:
            red.y-=vel

def yellow_handle_movement(KeyPressed, yellow):
    if KeyPressed[pygame.K_LEFT]: #kiri
        if yellow.x - vel < 0 or yellow.x + vel <  Lebar_layar/2 + skala[1]//2: 
            yellow.x -= 0
        else:
            yellow.x-=vel

    if KeyPressed[pygame.K_RIGHT]: #kanan
        if yellow.x + vel > Lebar_layar -  skala[1]:
            yellow.x+= 0
        else:
            yellow.x+=vel

    if KeyPressed[pygame.K_DOWN]: #bawah
        if yellow.y + vel > Tinggi_layar - skala[0]:
            yellow.y += 0
        else:
            yellow.y+=vel

    if KeyPressed[pygame.K_UP]: #atas
        if yellow.y - vel < 0:
            yellow.y -= yellow.y 
        else:
            yellow.y-=vel

def main():
    run= True 
    red= pygame.Rect(100, Tinggi_layar/2 - skala[1]/2, skala[0], skala[1])
    yellow= pygame.Rect(760, Tinggi_layar/2 - skala[1]/2,skala[0], skala[1])
    red_bullet = []
    yellow_bullet= []

    Red_health = 10
    Yellow_health = 10
    #FPS machine
    clock= pygame.time.Clock()
    while run:
        #defining what fps you use
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len (red_bullet) < Max_bullet:
                    firesound.play()
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2, 10, 5)
                    firesound.play()
                    red_bullet.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullet) < Max_bullet:
                    firesound.play()
                    bullet = pygame.Rect(yellow.x , yellow.y + red.height//2, 10, 5)
                    yellow_bullet.append(bullet)
            if event.type == Red_hit:
                hitsound.play()
                Red_health-=1
            if event.type == Yellow_hit:
                hitsound.play()
                Yellow_health-=1    
        windows(red, yellow, red_bullet , yellow_bullet, Red_health, Yellow_health)
        text=""
        if Red_health <= 0:
            text= "Yellow Win!"
            warna= YellowW
        if Yellow_health<=0:
            text= "Red Win!"
            warna= RedW
        if text!="":
            display_winner(text, warna)
            break
        KeyPressed= pygame.key.get_pressed()
        red_handle_movement(KeyPressed, red)
        yellow_handle_movement(KeyPressed, yellow)
        bullet_handle(red, yellow, red_bullet, yellow_bullet)
    main()  

if __name__ == "__main__":
    main()