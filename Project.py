import pygame
import os
import sys
import time
import random

pygame.init()
diff = input('Выберите режим сложности: легко, средне, сложно, невозможно. - ')

if diff == 'легко':
    width = 720  # Размеры окна
    height = 500
elif diff == 'средне':
    width = 540  # Размеры окна
    height = 360
elif diff == 'сложно':
    width = 400  # Размеры окна
    height = 240
elif diff == 'невозможно':
    width = 240  # Размеры окна
    height = 100

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Zmeyka on Python')
clock = pygame.time.Clock()


def load_image(name):                                                       # Функция загрузки картинки
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def your_score(score):                                                      # Счетчик очков
    score_font = pygame.font.SysFont("calibri", 35)                         # Ввод шрифта для письма
    value = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(value, [0, 0])


def drawing_snake(snake_block, snake_list):                                 # Функция отрисовки змеи
    for x in snake_list:
        pygame.draw.rect(screen, (0, 0, 0), [x[0], x[1], snake_block, snake_block])


def pr(tex, color):                                                         # Функция вывода текста(любого)
    font_style = pygame.font.SysFont("calibri", 25)                         # Ввод шрифтадля письма
    txt = font_style.render(tex, True, color)
    screen.blit(txt, [10, 50])


def gameLoop():                 # игра
    global screen
    if diff == 'легко':
        width = 720  # Размеры окна
        height = 500
        snake_block = 10
        snake_speed = 15
    elif diff == 'средне':
        width = 540  # Размеры окна
        height = 360
        snake_block = 10
        snake_speed = 23
    elif diff == 'сложно':
        width = 400  # Размеры окна
        height = 240
        snake_block = 10
        snake_speed = 30
    elif diff == 'невозможно':
        width = 240  # Размеры окна
        height = 100
        snake_block = 10
        snake_speed = 35

    closing_with_X = False
    menu = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Генерация еды и бомб
    food_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
    food_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
    while food_x < 35 or food_y < 20:
        food_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
        food_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

    bomb_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
    bomb_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
    while bomb_x < 35 or bomb_y < 20:
        bomb_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
        bomb_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

    bomb_x2 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
    bomb_y2 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
    while bomb_x2 < 35 or bomb_y2 < 20:
        bomb_x2 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
        bomb_y2 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

    bomb_x3 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
    bomb_y3 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
    while bomb_x3 < 35 or bomb_y3 < 20:
        bomb_x3 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
        bomb_y3 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

    while not closing_with_X:
        # Логика окончания игры
        while menu:
            screen.fill((255, 255, 255))
            screen = pygame.display.set_mode((720, 200))
            screen.fill((255, 255, 255))
            pr("The game is over. You may push ESC to leave or R to restart the game.", (0, 0, 0))
            your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        closing_with_X = True
                        menu = False
                    if event.key == pygame.K_r:
                        gameLoop()

        # Обработка ввода с клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing_with_X = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_SPACE:
                    time.sleep(5)

        # Создание спрайтов
        all_sprites = pygame.sprite.Group()
        bomb = pygame.sprite.Sprite(all_sprites)
        bomb.image = pygame.transform.scale(load_image("bomb.png"), (20, 20))
        bomb2 = pygame.sprite.Sprite(all_sprites)
        bomb2.image = pygame.transform.scale(load_image("bomb.png"), (20, 20))
        bomb3 = pygame.sprite.Sprite(all_sprites)
        bomb3.image = pygame.transform.scale(load_image("bomb.png"), (20, 20))
        food = pygame.sprite.Sprite(all_sprites)
        food.image = pygame.transform.scale(load_image("Apple.png"), (20, 20))
        bomb.rect = bomb.image.get_rect()
        bomb2.rect = bomb2.image.get_rect()
        bomb3.rect = bomb3.image.get_rect()
        food.rect = food.image.get_rect()

        # Пересечение с краями
        screen = pygame.display.set_mode((width, height))
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            menu = True
        x1 += x1_change
        y1 += y1_change
        screen.fill((255, 255, 255))

        # Координаты еды и бомб
        bomb.rect.x = bomb_x
        bomb.rect.y = bomb_y

        bomb2.rect.x = bomb_x2
        bomb2.rect.y = bomb_y2

        bomb3.rect.x = bomb_x3
        bomb3.rect.y = bomb_y3

        food.rect.x = food_x
        food.rect.y = food_y

        all_sprites.draw(screen)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                menu = True
        drawing_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        # Логика сбора еды + генерация новой еды и бомб
        if (x1 == food_x and y1 == food_y) or (x1 == food_x and y1 == food_y + 10) or\
                (x1 == food_x + 10 and y1 == food_y) or (x1 == food_x + 10 and y1 == food_y + 10):
            food_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
            food_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
            while food_x < 50 or food_y < 20:
                food_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
                food_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

            bomb_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
            bomb_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
            while bomb_x < 50 or bomb_y < 20:
                bomb_x = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
                bomb_y = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

            bomb_x2 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
            bomb_y2 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
            while bomb_x2 < 50 or bomb_y2 < 20:
                bomb_x2 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
                bomb_y2 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0

            bomb_x3 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
            bomb_y3 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
            while bomb_x3 < 50 or bomb_y3 < 20:
                bomb_x3 = round(random.randrange(snake_block, width - snake_block - 10) / 10.0) * 10.0
                bomb_y3 = round(random.randrange(snake_block, height - snake_block - 10) / 10.0) * 10.0
            Length_of_snake += 1
        # Логика пересечения с бомбами
        if (x1 == bomb_x and y1 == bomb_y) or (x1 == bomb_x and y1 == bomb_y + 10) or\
                (x1 == bomb_x + 10 and y1 == bomb_y) or (x1 == bomb_x + 10 and y1 == bomb_y + 10):
            menu = True
        elif (x1 == bomb_x2 and y1 == bomb_y2) or (x1 == bomb_x2 and y1 == bomb_y2 + 10) or\
                (x1 == bomb_x2 + 10 and y1 == bomb_y2) or (x1 == bomb_x2 + 10 and y1 == bomb_y2 + 10):
            menu = True
        elif (x1 == bomb_x3 and y1 == bomb_y3) or (x1 == bomb_x3 and y1 == bomb_y3 + 10) or\
                (x1 == bomb_x3 + 10 and y1 == bomb_y3) or (x1 == bomb_x3 + 10 and y1 == bomb_y3 + 10):
            menu = True
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()