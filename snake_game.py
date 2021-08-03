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
count_length=0
count_breadth=0
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
                        if event.type == pygame.KEYDOWN:
                                if event.key==pygame.K_r:
                                        screen.fill((0,0,0))
                                        points=5
                                        length=random.randint(0,450)
                                        breadth=random.randint(0,450)
                                if event.key==pygame.K_UP:
                                        count_length=0
                                        count_breadth=2
                                if event.key==pygame.K_DOWN:
                                        count_length=1
                                        count_breadth=2
                                if event.key==pygame.K_LEFT:
                                        count_length=2
                                        count_breadth=0
                                if event.key==pygame.K_RIGHT:
                                        count_length=2
                                        count_breadth=1
        if(count_length==0): 
                snake_length-=0.1
                screen.fill((0,0,0))
        elif(count_length==1):
                snake_length+=0.1
                screen.fill((0,0,0))
        elif(count_breadth==0):
                snake_breadth-=0.1
                screen.fill((0,0,0))
        elif(count_breadth==1):
                snake_breadth+=0.1
                screen.fill((0,0,0))
        text(length,breadth,snake_length,snake_breadth,points)
        pygame.display.flip()
