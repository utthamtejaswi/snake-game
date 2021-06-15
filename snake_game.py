import pygame
import random
import pygame.font

pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake_game")


def text(breadth,length):
        text=font.render(".",10, (255, 255, 255))
        text_box = ((breadth,length))
        screen.blit(text,text_box)


done = False
length=random.randint(0,499)
breadth=random.randint(0,499)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                        exit()
                                
        text(length,breadth)
        pygame.display.flip()
