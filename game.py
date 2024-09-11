import pygame
pygame.init()


swidth = 500
shight = 500
win = pygame.display.set_mode((swidth, shight))
pygame.display.set_caption("First Game")

x = 50
y = 425
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while (run):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < swidth - vel - width:
        x += vel
    if keys[pygame.K_w] and y > vel:
        y -= vel
    if not(isJump): 
        if keys[pygame.K_s] and y < shight - vel - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount ** 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (100, 200, 100), (x, y, width, height))
    pygame.display.update()

pygame.quit()