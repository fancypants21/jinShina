import pygame

pygame.display.set_caption('First Game')
pygame.init()
window = pygame.display.set_mode((800,800))

class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.vel = 20


class Projectile:
    def __init__(self, x, y, color,height,width):
        self.x = x
        self.y = y 
        self.height = height
        self.width = width
        self.color = color
        self.vel = 30
    def draw(self,window):
        pygame.draw.rect(window, self.color,(self.x, self.y, self.height, self.width))
        
        


        

man = Player(400,600,40,40)
bullets = []
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if 0 < bullet.x < 800:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if len(bullets) < 7:
            bullets.append(Projectile(int(man.x+man.width/2),int(man.y+man.height/2),(0,200,0),20,5))
    if keys[pygame.K_LEFT]:
        man.x -= man.vel
        if man.x < 0:
            man.x = 0
    if keys[pygame.K_RIGHT]:
        man.x += man.vel
        if man.x > 760:
            man.x = 760
    if keys[pygame.K_UP]:
        man.isJump = True
    
    if man.isJump:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= ((man.jumpCount)**2)* 0.5 *neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    window.fill((0,0,0))
    for bullet in bullets:
        bullet.draw(window)
    pygame.draw.rect(window,(0,200,0),(man.x,man.y,man.width,man.height))
    pygame.display.update()
pygame.quit()

        
