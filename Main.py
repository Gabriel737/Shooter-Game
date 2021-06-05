import pygame
#hello
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, scale:int) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(scale*img.get_width()), int(scale*img.get_height())))
        self.rect = img.get_rect()
        self.rect.center = (x, y)

    def draw(self) -> None:
        screen.blit(self.image, self.rect)


player = Soldier(200, 200, 3)
player2 = Soldier(400, 200, 3)

run = True
while run:

    player.draw()
    player2.draw()

    for event in pygame.event.get():
        # Quit Game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()