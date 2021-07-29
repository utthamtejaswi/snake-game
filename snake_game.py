import pygame
import random
import pygame.font

pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake_game")


def text(breadth,length,snake_length,snake_breadth,points):
        text=font.render(".",10, (255, 255, 255))
        text_box = ((breadth,length))
        screen.blit(text,text_box)

        text_snake=font.render(points*".",10, (255, 255, 255))
        text_box_snake = ((snake_breadth,snake_length))
        screen.blit(text_snake,text_box_snake)

        text_points=font.render("points: "+str(points),10, (255, 255, 255))
        text_box_points = ((350,50))
        screen.blit(text_points,text_box_points)


done = False
length=random.randint(0,450)
breadth=random.randint(0,450)
snake_length=250
snake_breadth=250
points=5


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_r:
                                screen.fill((0,0,0))
                                points=5
                                length=random.randint(0,450)
                                breadth=random.randint(0,450)
                        if event.key==pygame.K_UP:
                                snake_length-=1
                                screen.fill((0,0,0))
                        if event.key==pygame.K_DOWN:
                                snake_length+=1
                                screen.fill((0,0,0))
                        if event.key==pygame.K_LEFT:
                                snake_breadth-=1
                                screen.fill((0,0,0))
                        if event.key==pygame.K_RIGHT:
                                snake_breadth+=1
                                screen.fill((0,0,0))
        text(length,breadth,snake_length,snake_breadth,points)
        pygame.display.flip()
