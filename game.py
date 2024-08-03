import pygame as py
import levels as lvl

py.mixer.pre_init(44100, -16, 1, 512)
py.init()

py.mixer.music.load("audio/main2.mp3")
py.mixer.music.play(-1, 0.0, 100)
mainMusicPaused = False
mainMusicVolume = 0.5
py.mixer.music.set_volume(mainMusicVolume)

jump_snd = py.mixer.Sound("audio/jump.wav")
click_snd = py.mixer.Sound("audio/click2.wav")
win_snd = py.mixer.Sound("audio/win.wav")
lose_snd = py.mixer.Sound("audio/lose.wav")
pick_snd = py.mixer.Sound("audio/pick.ogg")

clock = py.time.Clock()
fps = 60

screen_width = 1000
screen_height = 700

screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption('REDEMPTION')
icon = py.image.load('images/logo.png')
py.display.set_icon(icon)

font_score = py.font.SysFont('Bauhaus 93', 20)
color_soul = (190, 230, 246) #color for font

tile_size = 50
game_over = 0
score = 0
rules = False
main_menu = True

bg_img = py.image.load('images/hell5.png')
bg_img = py.transform.scale(bg_img, (screen_width, screen_height))
heaven_img = py.image.load('images/heaven.png')
heaven_img = py.transform.scale(heaven_img, (screen_width, screen_height))
restart1_img = py.image.load('images/переиграть1.png')
restart1_img = py.transform.scale(restart1_img, (restart1_img.get_width() * 1.5, restart1_img.get_height() * 1.5))
restart2_img = py.image.load('images/переиграть2.png')
restart2_img = py.transform.scale(restart2_img, (restart2_img.get_width() * 1.5, restart2_img.get_height() * 1.5))
start1_img = py.image.load('images/играть1.png')
start1_img = py.transform.scale(start1_img, (start1_img.get_width() * 1.5, start1_img.get_height() * 1.5))
start2_img = py.image.load('images/играть2.png')
start2_img = py.transform.scale(start2_img, (start2_img.get_width() * 1.5, start2_img.get_height() * 1.5))
exit1_img = py.image.load('images/выйти1.png')
exit1_img = py.transform.scale(exit1_img, (exit1_img.get_width() * 1.5, exit1_img.get_height() * 1.5))
exit2_img = py.image.load('images/выйти2.png')
exit2_img = py.transform.scale(exit2_img, (exit2_img.get_width() * 1.5, exit2_img.get_height() * 1.5))
rules1_img = py.image.load('images/правила1.png')
rules1_img = py.transform.scale(rules1_img, (rules1_img.get_width() * 1.5, rules1_img.get_height() * 1.5))
rules2_img = py.image.load('images/правила2.png')
rules2_img = py.transform.scale(rules2_img, (rules2_img.get_width() * 1.5, rules2_img.get_height() * 1.5))
soul_img = py.image.load('images/soul4.png')
soul_img = py.transform.scale(soul_img, (tile_size // 2, tile_size // 2))
menu_img = py.image.load('images/menu.png')
menu_img = py.transform.scale(menu_img, (550, 450))
name_img = py.image.load('images/name.png')
game_over_img = py.image.load('images/game over.png')
rules_img = py.image.load('images/rules.png')
rules_img = py.transform.scale(rules_img, (750, 550))
cross_img = py.image.load('images/cross.png')
cross_img = py.transform.scale(cross_img, (tile_size * 2, tile_size * 1.5))
win_img = py.image.load('images/you win.png')
win_img = py.transform.scale(win_img, (700, 200))
congrats_img = py.image.load('images/congr.png')
final_words_img = py.image.load('images/final.png')
final_words_img = py.transform.scale(final_words_img, (950, 70))


bat_img = py.image.load('images/bat1.png')
bat_img = py.transform.scale(bat_img, (25, 21))
bat_left = []
bat_right = []
for i in range(2, 4):
    img = py.image.load(f'images/bat{i}.png')
    img_left = py.transform.scale(img, (25, 21))
    img_right = py.transform.flip(img_left, True, False)
    bat_left.append(img_left)
    bat_right.append(img_right)

lava_img = []
for i in range(1, 4):
    img = py.image.load(f'images/lava_{i}.png')
    img = py.transform.scale(img, (tile_size, tile_size // 2))
    lava_img.append(img)

fire_img = []
for i in range(1, 5):
    img = py.image.load(f'images/fire{i}.png')
    img = py.transform.scale(img, (tile_size, tile_size))
    fire_img.append(img)

snake_img = []
for i in range(1, 4):
    img = py.image.load(f'images/snake{i}.png')
    img = py.transform.scale(img, (tile_size * 0.7, tile_size * 0.7))
    snake_img.append(img)

dog_right = []
dog_left = []
for i in range(1, 4):
    img = py.image.load(f'images/dog_{i}.png')
    img_left = py.transform.scale(img, (tile_size + 20, tile_size + 10))
    img_right = py.transform.flip(img_left, True, False)
    dog_left.append(img_left)
    dog_right.append(img_right)

demon_right = []
demon_left = []
for i in range(1, 5):
    img = py.image.load(f'images/demon{i}.png')
    img_left = py.transform.scale(img, (tile_size * 0.7, tile_size * 0.7 + 20))
    img_right = py.transform.flip(img_left, True, False)
    demon_left.append(img_left)
    demon_right.append(img_right)

health_bar = []
for i in range(1, 6):
    img = py.image.load(f'images/health{i}.png')
    img = py.transform.scale(img, (tile_size*2, tile_size//3))
    health_bar.append(img)

bat_group = py.sprite.Group()
lava_group = py.sprite.Group()
spikes_group = py.sprite.Group()
exit_group = py.sprite.Group()
soul_group = py.sprite.Group()
heal_group = py.sprite.Group()
fire_group = py.sprite.Group()
snake_group = py.sprite.Group()
enemy_group11 = py.sprite.Group()
enemy_group12 = py.sprite.Group()
enemy_group13 = py.sprite.Group()
enemy_group14 = py.sprite.Group()
enemy_group21 = py.sprite.Group()
enemy_group22 = py.sprite.Group()
enemy_group23 = py.sprite.Group()
enemy_group24 = py.sprite.Group()


levels_list = [lvl.level1, lvl.level2, lvl.level3, lvl.level4, lvl.level5]
lvl_indx = 0
max_lvl = 5

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def reset_level(lvl):
    player.reset(100, screen_height - 130)
    bat_group.empty()
    lava_group.empty()
    spikes_group.empty()
    exit_group.empty()
    heal_group.empty()
    fire_group.empty()
    snake_group.empty()
    soul_group.empty()
    enemy_group11.empty()
    enemy_group12.empty()
    enemy_group13.empty()
    enemy_group14.empty()
    enemy_group21.empty()
    enemy_group22.empty()
    enemy_group23.empty()
    enemy_group24.empty()

    world_map = levels_list[lvl_indx]

    world = World(world_map)

    return world

class Button():
    def __init__(self, image1, image2, x, y):
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x     #self.width // 2
        self.rect.y = y    #self.height // 2
        self.clicked = False

    def draw(self):
        action = False

        mouse_pos = py.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.image = self.image2
            if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                click_snd.play()
        else:
           self.image = self.image1
        self.clicked = False

        screen.blit(self.image, self.rect)

        return action


class World():
    def __init__(self, map):
        self.tile_list = []

        hellTile_img = py.image.load('images/hell_tile.jpg')
        lavaTile_img = py.image.load('images/lava_tile.png')

        row_count = 0
        for row in map:
            column_count = 0
            for tile in row:
                if tile == 1: #brick
                    img = py.transform.scale(hellTile_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2: #spikes
                    spikes = Spikes(column_count * tile_size, row_count * tile_size + tile_size * 0.4)
                    spikes_group.add(spikes)
                if tile == 3: #lava tile
                    img = py.transform.scale(lavaTile_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    lava_tile = (img, img_rect)
                    self.tile_list.append(lava_tile)
                if tile == 4: #bat
                    bat = Enemy_bat(column_count * tile_size, row_count * tile_size + 10)
                    bat_group.add(bat)
                if tile == 5: #lava
                    lava = Lava(column_count * tile_size, row_count * tile_size + tile_size // 2)
                    lava_group.add(lava)
                if tile == 6: #exit
                    exit = Exit(column_count * tile_size, row_count * tile_size - tile_size // 2)
                    exit_group.add(exit)
                if tile == 7: #soul
                    soul = Soul(column_count * tile_size + tile_size // 2, row_count * tile_size + tile_size // 2)
                    soul_group.add(soul)
                if tile == 81: #dog1
                    dog = Enemy(column_count * tile_size, row_count * tile_size - 5, dog_left, dog_right)
                    enemy_group11.add(dog)
                if tile == 82: #dog2
                    dog = Enemy(column_count * tile_size, row_count * tile_size - 5, dog_left, dog_right)
                    enemy_group12.add(dog)
                if tile == 83: #dog3
                    dog = Enemy(column_count * tile_size, row_count * tile_size - 5, dog_left, dog_right)
                    enemy_group13.add(dog)
                if tile == 84: #dog4
                    dog = Enemy(column_count * tile_size, row_count * tile_size - 5, dog_left, dog_right)
                    enemy_group14.add(dog)
                if tile == 9: #heal
                    heal = Heal(column_count * tile_size + tile_size // 2, row_count * tile_size + tile_size // 2)
                    heal_group.add(heal)
                if tile == 10: #fire
                    fire = Fire(column_count * tile_size, row_count * tile_size)
                    fire_group.add(fire)
                if tile == 11: #snake
                    snake = Snake(column_count * tile_size, row_count * tile_size + tile_size * 0.3)
                    snake_group.add(snake)
                if tile == 121: #demon1
                    demon = Enemy(column_count * tile_size, row_count * tile_size - 5, demon_right, demon_left)
                    enemy_group21.add(demon)
                if tile == 122: #demon2
                    demon = Enemy(column_count * tile_size, row_count * tile_size - 5, demon_right, demon_left)
                    enemy_group22.add(demon)
                if tile == 123: #demon3
                    demon = Enemy(column_count * tile_size, row_count * tile_size - 5, demon_right, demon_left)
                    enemy_group23.add(demon)
                if tile == 124: #demon4
                    demon = Enemy(column_count * tile_size, row_count * tile_size - 5, demon_right, demon_left)
                    enemy_group24.add(demon)
                column_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_animation_slower = 10
        hit_right_img = py.image.load('images/skeleton_hit1.png')
        hit_right_img = py.transform.scale(hit_right_img, (40, 50))
        hit_left_img = py.transform.flip(hit_right_img, True, False)

        if game_over == 0:
            global fight
            key = py.key.get_pressed()
            if key[py.K_UP] and self.jumped == False and self.in_air == False:
                self.velocity_y = -20
                self.jumped = True
                jump_snd.play()
            if key[py.K_UP] == False:
                self.jumped = False
            if key[py.K_LEFT] and self.rect.x > 3:
                dx -= 3
                self.counter += 1
                self.direction = -1
            if key[py.K_RIGHT] and self.rect.x + self.width + 3 < screen_width:
                dx += 3
                self.counter += 1
                self.direction = 1
            if key[py.K_RIGHT] == False and key[py.K_LEFT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.skeleton_right[self.index]
                if self.direction == -1:
                    self.image = self.skeleton_left[self.index]
            if key[py.K_SPACE] == True:
                if self.direction == 1:
                    self.image = hit_right_img
                if self.direction == -1:
                    self.image = hit_left_img
                fight = True
            if key[py.K_SPACE] == False:
                fight = False


            if self.counter > walk_animation_slower:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.skeleton_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.skeleton_right[self.index]
                if self.direction == -1:
                    self.image = self.skeleton_left[self.index]

            self.velocity_y += 1.5 # gravity
            if self.velocity_y > 8:
                self.velocity_y = 8
            dy += self.velocity_y

            self.in_air = True
            for tile in world.tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.velocity_y < 0:  # jumping
                        dy = tile[1].bottom - self.rect.top
                        self.velocity_y = 0
                    elif self.velocity_y >= 0:  # falling
                        dy = tile[1].top - self.rect.bottom
                        self.velocity_y = 0
                        self.in_air = False


            if py.sprite.spritecollide(self, bat_group, False):
                self.health -= 1

            if py.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            if py.sprite.spritecollide(self, spikes_group, False):
                game_over = -1

            if py.sprite.spritecollide(self, enemy_group11, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group12, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group13, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group14, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group21, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group22, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group23, False):
                self.health -= 1

            if py.sprite.spritecollide(self, enemy_group24, False):
                self.health -= 1

            if py.sprite.spritecollide(self, fire_group, False):
                self.health -= 1

            if py.sprite.spritecollide(self, snake_group, False):
                self.health -= 1

            if self.health <= 0:
                game_over = -1

            if py.sprite.spritecollide(self, exit_group, False) and score >= 5:
                game_over = 1
                win_snd.play()


            self.rect.x += dx
            self.rect.y += dy


        elif game_over == -1: #death
            lose_snd.play()
            self.image = self.dead_image


        screen.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y):
        self.skeleton_right = []
        self.skeleton_left = []
        self.index = 0  # to get picture from skeleton_right list
        self.counter = 0  # speed of animation?
        for i in range(0, 6):
            img = py.image.load(f'images/skeleton_walk{i}.png')
            img_right = py.transform.scale(img, (40, 50))
            img_left = py.transform.flip(img_right, True, False)
            self.skeleton_right.append(img_right)
            self.skeleton_left.append(img_left)

        self.dead_img = py.image.load('images/death.png')
        self.dead_image = py.transform.scale(self.dead_img, (40, 50))
        self.image = self.skeleton_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        self.health = 500


class Enemy_bat(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = bat_img #py.transform.scale(bat_img, (25, 21))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.index = 0
        self.counter = 0 #animation

    def update(self):
        walk_animation_slower = 10

        self.rect.x += self.move_direction
        self.move_counter += 1
        self.counter += 1

        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        if self.counter > walk_animation_slower:
            self.counter = 0
            self.index += 1
            if self.index >= len(bat_right):
                self.index = 0
            if self.move_direction == 1:
                self.image = bat_right[self.index]
            if self.move_direction == -1:
                self.image = bat_left[self.index]


class Lava(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = lava_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 #animation
        self.index = 0

    def update(self):
        animation_slower = 10

        self.counter += 1
        if self.counter > animation_slower:
            self.counter = 0
            self.index += 1
            if self.index >= len(lava_img):
                self.index = 0
        self.image = lava_img[self.index]

class Fire(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = fire_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 #animation
        self.index = 0

    def update(self):
        animation_slower = 5

        self.counter += 1
        if self.counter > animation_slower:
            self.counter = 0
            self.index += 1
            if self.index >= len(fire_img):
                self.index = 0
        self.image = fire_img[self.index]


class Snake(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = snake_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 #animation
        self.index = 0

    def update(self):
        animation_slower = 5

        self.counter += 1
        if self.counter > animation_slower:
            self.counter = 0
            self.index += 1
            if self.index >= len(snake_img):
                self.index = 0
        self.image = snake_img[self.index]


class Soul(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        soul_img = py.image.load('images/soul4.png')
        self.image = py.transform.scale(soul_img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Heal(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        heal_img = py.image.load('images/heal.png')
        self.image = py.transform.scale(heal_img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Spikes(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        spikes_img = py.image.load('images/spikes.png')
        self.image = py.transform.scale(spikes_img, (tile_size * 0.5, tile_size * 0.6))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Exit(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        exit_img = py.image.load('images/Gates.png')
        self.image = py.transform.scale(exit_img, (tile_size, tile_size * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(py.sprite.Sprite):
    def __init__(self, x, y, left, right):
        py.sprite.Sprite.__init__(self)
        self.left = left
        self.right = right
        self.image = left[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.health11 = 200
        self.health12 = 200
        self.health13 = 200
        self.health14 = 200
        self.health21 = 200
        self.health22 = 200
        self.health23 = 200
        self.health24 = 200
        self.index = 0
        self.counter = 0  # animation

    def update(self):
        walk_animation_slower = 10

        key = py.key.get_pressed()
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.counter += 1

        global score

        if py.sprite.spritecollide(player, enemy_group11, False):
            if key[py.K_SPACE]:
                self.health11 -= 2
            if self.health11 == 0:
                py.sprite.spritecollide(player, enemy_group11, True)
                score += 1
            if self.health11 <= 200 and self.health11 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health11 <= 160 and self.health11 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health11 <= 120 and self.health11 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health11 <= 80 and self.health11 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health11 <= 40 and self.health11 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group12, False):
            if key[py.K_SPACE]:
                self.health12 -= 2
            if self.health12 == 0:
                py.sprite.spritecollide(player, enemy_group12, True)
                score += 1

            if self.health12 <= 200 and self.health12 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health12 <= 160 and self.health12 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health12 <= 120 and self.health12 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health12 <= 80 and self.health12 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health12 <= 40 and self.health12 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group13, False):
            if key[py.K_SPACE]:
                self.health13 -= 2
            if self.health13 == 0:
                py.sprite.spritecollide(player, enemy_group13, True)
                score += 1

            if self.health13 <= 200 and self.health13 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health13 <= 160 and self.health13 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health13 <= 120 and self.health13 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health13 <= 80 and self.health13 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health13 <= 40 and self.health13 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group14, False):
            if key[py.K_SPACE]:
                self.health14 -= 2
            if self.health14 == 0:
                py.sprite.spritecollide(player, enemy_group14, True)
                score += 1

            if self.health14 <= 200 and self.health14 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health14 <= 160 and self.health14 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health14 <= 120 and self.health14 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health14 <= 80 and self.health14 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health14 <= 40 and self.health14 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group21, False):
            if key[py.K_SPACE]:
                self.health21 -= 2
            if self.health21 == 0:
                py.sprite.spritecollide(player, enemy_group21, True)
                score += 1

            if self.health21 <= 200 and self.health21 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health21 <= 160 and self.health21 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health21 <= 120 and self.health21 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health21 <= 80 and self.health21 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health21 <= 40 and self.health21 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group22, False):
            if key[py.K_SPACE]:
                self.health22 -= 2
            if self.health22 == 0:
                py.sprite.spritecollide(player, enemy_group22, True)
                score += 1

            if self.health22 <= 200 and self.health22 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health22 <= 160 and self.health22 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health22 <= 120 and self.health22 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health22 <= 80 and self.health22 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health22 <= 40 and self.health22 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group23, False):
            if key[py.K_SPACE]:
                self.health23 -= 2
            if self.health23 == 0:
                py.sprite.spritecollide(player, enemy_group23, True)
                score += 1

            if self.health23 <= 200 and self.health23 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health23 <= 160 and self.health23 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health23 <= 120 and self.health23 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health23 <= 80 and self.health23 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health23 <= 40 and self.health23 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))

        if py.sprite.spritecollide(player, enemy_group24, False):
            if key[py.K_SPACE]:
                self.health24 -= 2
            if self.health24 == 0:
                py.sprite.spritecollide(player, enemy_group24, True)
                score += 1

            if self.health24 <= 200 and self.health24 > 160:
                screen.blit(health_bar[0], (screen_width - 105, 70))
            if self.health24 <= 160 and self.health24 > 120:
                screen.blit(health_bar[1], (screen_width - 105, 70))
            if self.health24 <= 120 and self.health24 > 80:
                screen.blit(health_bar[2], (screen_width - 105, 70))
            if self.health24 <= 80 and self.health24 > 40:
                screen.blit(health_bar[3], (screen_width - 105, 70))
            if self.health24 <= 40 and self.health24 >= 0:
                screen.blit(health_bar[4], (screen_width - 105, 70))


        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        if self.counter > walk_animation_slower:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.right):
                self.index = 0
            if self.move_direction == 1:
                self.image = self.right[self.index]
            if self.move_direction == -1:
                self.image = self.left[self.index]


world_map = levels_list[lvl_indx]

world = World(world_map)
player = Player(100, screen_height - 130)

restart_button = Button(restart1_img, restart2_img, 345, 310)
exit_button = Button(exit1_img, exit2_img, 345, 500)
exit_button2 = Button(exit1_img, exit2_img, 345, 450)
start_button = Button(start1_img, start2_img, 345, 220)
rules_button = Button(rules1_img, rules2_img, 345, 360)
exit_rules_button = Button(cross_img, cross_img, 760, 105)

run = True

while run:

    clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    if main_menu:
        screen.blit(menu_img, (225, 200))
        screen.blit(name_img, (220, 100))
        if exit_button.draw():
           run = False
        if start_button.draw():
            main_menu = False
        if rules_button.draw() or rules == True:
            rules = True
            screen.blit(rules_img, (100, 100))
            if exit_rules_button.draw() == True:
                rules = False
                main_menu = True

    else:
        world.draw()
        screen.blit(soul_img, (21, 10))
        draw_text('  ' + str(score) + ' / 5', font_score, color_soul, tile_size - 10, 10)

        player.update(game_over)

        if player.health <= 500 and player.health > 400:
            screen.blit(health_bar[0], (25, 45))
        if player.health <= 400 and player.health > 300:
            screen.blit(health_bar[1], (25, 45))
        if player.health <= 300 and player.health > 200:
            screen.blit(health_bar[2], (25, 45))
        if player.health <= 200 and player.health > 100:
            screen.blit(health_bar[3], (25, 45))
        if player.health <= 100 and player.health >= 0:
            screen.blit(health_bar[4], (25, 45))

        if game_over == 0:
            bat_group.update()
            lava_group.update()
            fire_group.update()
            snake_group.update()
            enemy_group11.update()
            enemy_group12.update()
            enemy_group13.update()
            enemy_group14.update()
            enemy_group21.update()
            enemy_group22.update()
            enemy_group23.update()
            enemy_group24.update()


            if py.sprite.spritecollide(player, soul_group, True):
                score += 1
                pick_snd.play()

            if py.sprite.spritecollide(player, heal_group, True):
                player.health = 500

        bat_group.draw(screen)
        lava_group.draw(screen)
        spikes_group.draw(screen)
        exit_group.draw(screen)
        soul_group.draw(screen)
        heal_group.draw(screen)
        fire_group.draw(screen)
        snake_group.draw(screen)
        enemy_group11.draw(screen)
        enemy_group12.draw(screen)
        enemy_group13.draw(screen)
        enemy_group14.draw(screen)
        enemy_group21.draw(screen)
        enemy_group22.draw(screen)
        enemy_group23.draw(screen)
        enemy_group24.draw(screen)

        game_over = player.update(game_over)

        if game_over == -1:
            screen.blit(menu_img, (225, 150))
            screen.blit(game_over_img, (250, 200))
            if restart_button.draw():
                world_data = []
                world = reset_level(lvl_indx)
                game_over = 0
                score = 0
            if exit_button2.draw():
                run = False

        if game_over == 1:
            lvl_indx += 1
            if lvl_indx < max_lvl:
                world_map = []
                world = reset_level(lvl_indx)
                game_over = 0
                score = 0
            else:
                screen.blit(heaven_img, (0, 0))
                screen.blit(win_img, (screen_width // 2 - 330, screen_height // 2 - 200))
                screen.blit(congrats_img, (screen_width // 2 - 300, 500))
                screen.blit(final_words_img, (115, 580))


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_F10:
                mainMusicPaused = not mainMusicPaused
                if mainMusicPaused:
                    py.mixer.music.pause()
                else:
                    py.mixer.music.unpause()
            if event.key == py.K_F11:
                mainMusicVolume -= 0.1
                py.mixer.music.set_volume(mainMusicVolume)
            if event.key == py.K_F12:
                mainMusicVolume += 0.1
                py.mixer.music.set_volume(mainMusicVolume)


    py.display.update()


py.quit()