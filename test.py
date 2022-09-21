import pygame
import random
import math
from pygame import mixer

pygame.init()

# Window
screen = pygame.display.set_mode((1000, 600))

# FPS 
clock = pygame.time.Clock()

# Icon and Caption
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Guns Reloaded")

# Intro Music
mixer.music.load("music/intro_music.wav")
mixer.music.play()

# background
back = pygame.image.load("assets/land.png")

# Intro Font and Icon
intro_font = pygame.image.load("assets/intro.png")
w = intro_font.get_width()
h = intro_font.get_height()
intro_icon = pygame.transform.scale(intro_font, (int(w*2.2), int(h*2.2)))

intro_icon = pygame.image.load("assets/intro_player.png")
w = intro_icon.get_width()
h = intro_icon.get_height()
intro_icon = pygame.transform.scale(intro_icon, (int(w*0.65), int(h*0.65)))

# gameover
endgame = pygame.image.load("assets/endgame.png")

# controls instructions
# W
w_key_img = pygame.image.load("assets/w_key.png")
w = w_key_img.get_width()
h = w_key_img.get_height()
w_key_img = pygame.transform.scale(w_key_img, (int(w*1), int(h*1)))
# S
s_key_img = pygame.image.load("assets/s_key.png")
w = s_key_img.get_width()
h = s_key_img.get_height()
s_key_img = pygame.transform.scale(s_key_img, (int(w*1), int(h*1)))
# space
space_key_img = pygame.image.load("assets/space_key.png")
w = space_key_img.get_width()
h = space_key_img.get_height()
space_key_img = pygame.transform.scale(space_key_img, (int(w*1.7), int(h*1.7)))

# Player
playerimg = pygame.image.load("assets/player_b.png")
w = playerimg.get_width()
h = playerimg.get_height()
playerimg = pygame.transform.scale(playerimg, (int(w*0.95), int(h*0.95)))
playerX = 50
playerY = 280
playerY_change = 0

# player bullet
p_bulletimg = pygame.image.load("assets/p_bullet.png")
w = p_bulletimg.get_width()
h = p_bulletimg.get_height()
p_bulletimg = pygame.transform.scale(p_bulletimg, (int(w*0.8), int(h*0.8)))
p_bulletX = 50
p_bulletY = 0
p_bulletX_change = 2.7
p_bulletY_change = 0
p_bullet = "load"


# Enemy1(gunner)
gunnerimg = pygame.image.load("assets/gunner.png")
gunnerX = random.randint(936, 1000)
gunnerY = random.randint(0, 536)
gunnerX_change = 70
gunnerY_change = 0.75

# Enemy Bullet
e_bulletimg = pygame.image.load("assets/e_bullet.png")
w = e_bulletimg.get_width()
h = e_bulletimg.get_height()
e_bulletimg = pygame.transform.scale(e_bulletimg, (int(w*0.8), int(h*0.8)))
e_bulletX = 0
e_bulletY = 0
e_bulletX_change = -2.2
e_bulletY_change = 0
e_bullet = "load"

# Enemy2(burgler)
burglerimg = []
burglerX = []
burglerY = []
burglerX_change = []
burglerY_change = []
burglers = 6

for b in range(burglers):
    burglerimg.append(pygame.image.load("assets/burgler.png"))
    burglerX.append(random.randint(936, 1000))
    burglerY.append(random.randint(0, 536))
    burglerX_change.append(-0.65)
    burglerY_change.append(0)

# Enemy3(Wagon)
wagonimg = pygame.image.load("assets/wagon.png")
w = wagonimg.get_width()
h = wagonimg.get_height()
wagonimg = pygame.transform.scale(wagonimg, (int(w*0.18), int(h*0.18)))
wagonX = random.randint(936, 1000)
wagonY = random.randint(0, 536)
wagonX_change = 75
wagonY_change = 1.65


def player(x, y):
    screen.blit(playerimg, (x, y))


def gunner(x, y):
    screen.blit(gunnerimg, (x, y))


def burgler(x, y, b):
    screen.blit(burglerimg[b], (x, y))


def wagon(x, y):
    screen.blit(wagonimg, (x, y))


def fire_p_bullet(x, y):
    global p_bullet
    p_bullet = "shoot"
    screen.blit(p_bulletimg, (x+84, y+30))


def fire_e_bullet(x, y):
    global e_bullet
    e_bullet = "shoot"
    screen.blit(e_bulletimg, (x-28, y+28))


def chk_encounter_b(p_bulletX, p_bulletY, burglerX, burglerY):
    global burgler_dist
    burgler_dist = math.sqrt(math.pow(burglerX-p_bulletX, 2) +
                             (math.pow(burglerY-p_bulletY, 2)))

    if burgler_dist < 55:
        return True
    else:
        return False


def chk_encounter_g(p_bulletX, p_bulletY, gunnerX, gunnerY):
    global gunner_dist
    gunner_dist = math.sqrt(math.pow(gunnerX-p_bulletX, 2) +
                            (math.pow(gunnerY-p_bulletY, 2)))

    if gunner_dist < 55:
        return True
    else:
        return False


def chk_encounter_w(p_bulletX, p_bulletY, wagonX, wagonY):
    global wagon_dist
    wagon_dist = math.sqrt(math.pow(wagonX-p_bulletX, 2) +
                           (math.pow(wagonY-p_bulletY, 2)))

    if wagon_dist < 55:
        return True
    else:
        return False


def chk_encounter_e(e_bulletX, e_bulletY, playerX, playerY):
    global player_dist
    player_dist = math.sqrt(math.pow(playerX-e_bulletX, 2) +
                            (math.pow(playerY-e_bulletY, 2)))

    if player_dist < 55:
        return True
    else:
        return False


def chk_collision(p_bulletX, p_bulletY, e_bulletX, e_bulletY):
    global collision_dist
    collision_dist = math.sqrt(math.pow(p_bulletX-e_bulletX, 2) +
                               (math.pow(p_bulletY-e_bulletY, 2)))

    if collision_dist < 55:
        return True
    else:
        return False


def chk_score_med(score):
    if score > 30:
        return True
    else:
        return False


def chk_score_hard(score):
    if score > 60:
        return True
    else:
        return False


def gameover():
    screen.blit(endgame, (0, 0))
    end_sound = mixer.Sound("music/game_over.wav")
    end_sound.play()
    gameover_font = gameover_txt.render(
        "GAME OVER :(", True, ((255, 255, 255)))
    screen.blit(gameover_font, (240, 150))
    gameover_font = total_txt.render(
        "Total Score : " + str(score), True, ((0, 0, 0)))
    screen.blit(gameover_font, (390, 250))
    quit_font = quit_txt.render(
        "Press ESC to QUIT", True, (255, 255, 255))
    screen.blit(quit_font, (395, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


def show_score(x, y):
    score_font = score_txt.render(
        "Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_font, (x, y))


# Texts

# Intro
play_txt = pygame.font.Font("freesansbold.ttf", 30)
exit_txt = pygame.font.Font("freesansbold.ttf", 30)

# control
controls_txt = pygame.font.Font("freesansbold.ttf", 20)

# Game Over
gameover_txt = pygame.font.Font("freesansbold.ttf", 80)
total_txt = pygame.font.Font("freesansbold.ttf", 40)
quit_txt = pygame.font.Font("freesansbold.ttf", 30)

# Score
score = 0
score_txt = pygame.font.Font("freesansbold.ttf", 30)
scoreX = 10
scoreY = 10

play_game = False
playing = True


while playing:

    # main menu
    if play_game == False:

        screen.blit(back, (0, 0))

        screen.blit(intro_font, (160, 10))

        screen.blit(intro_icon, (395, 130))

        play_font = play_txt.render(
            "Press SPACE to Play", True, (0, 0, 0))
        screen.blit(play_font, (360, 390))

        quit_font = quit_txt.render(
            "Press ESC to QUIT", True, (0, 0, 0))
        screen.blit(quit_font, (370, 430))

        screen.blit(w_key_img, (780, 430))
        w_font = controls_txt.render("Move Up", True, (0, 0, 0))
        screen.blit(w_font, (840, 440))

        screen.blit(s_key_img, (780, 480))
        s_font = controls_txt.render("Move Down", True, (0, 0, 0))
        screen.blit(s_font, (840, 490))

        screen.blit(space_key_img, (765, 510))
        space_font = controls_txt.render("Shoot", True, (0, 0, 0))
        screen.blit(space_font, (870, 540))

        for play in pygame.event.get():
            if play.type == pygame.QUIT:
                playing = False
            if play.type == pygame.KEYDOWN:
                if play.key == pygame.K_SPACE:
                    play_game = True
                elif play.key == pygame.K_ESCAPE:
                    playing = False

    elif play_game == True:
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        mixer.music.stop()

        playerY += playerY_change
        if playerY <= 0:
            playerY = 0
        elif playerY >= 536:
            playerY = 536

        player(playerX, playerY)


        # Gunner All Functions

        player_dist_g = math.sqrt(math.pow(gunnerX-playerX, 2) +
                                  (math.pow(gunnerY-playerY, 2)))
        if player_dist_g < 70:
            gunnerX = 2000
            print("------------- X_X Killed by Gunner X_X -------------")
            gameover()

        else:
            encounter_e = chk_encounter_e(
                e_bulletX, e_bulletY, playerX, playerY)
            if encounter_e:
                print("------------- X_X Killed by Bullet X_X -------------")
                gameover()

        check_difficulty_med = chk_score_med(score)
        check_difficulty_hard = chk_score_hard(score)
        if check_difficulty_med:
            gunnerY += gunnerY_change
            if gunnerY >= 536:
                gunnerY_change = - 1.05
                gunnerX -= gunnerX_change
            elif gunnerY <= 0:
                gunnerY_change = 1.05
                gunnerX -= gunnerX_change

        elif check_difficulty_hard:
            gunnerY += gunnerY_change
            if gunnerY >= 536:
                gunnerY_change = - 1.65
                gunnerX -= gunnerX_change
            elif gunnerY <= 0:
                gunnerY_change = 1.65
                gunnerX -= gunnerX_change

        else:
            gunnerY += gunnerY_change
            if gunnerY >= 536:
                gunnerY_change = - 0.75
                gunnerX -= gunnerX_change
            elif gunnerY <= 0:
                gunnerY_change = 0.75
                gunnerX -= gunnerX_change

        encounter_g = chk_encounter_g(
            p_bulletX, p_bulletY, gunnerX, gunnerY)
        if encounter_g:
            enemy_down = mixer.Sound("music/enemy_down.wav")
            enemy_down.play()
            p_bulletX = 50
            p_bullet = "load"
            gunnerX = random.randint(936, 1000)
            gunnerY = random.randint(0, 536)
            score += 3
        gunner(gunnerX, gunnerY)

        # Burglers All Functions
        for b in range(burglers):
            player_dist_b = math.sqrt(math.pow(burglerX[b]-playerX, 2) +
                                      (math.pow(burglerY[b]-playerY, 2)))
            if player_dist_b < 70:
                for j in range(burglers):
                    burglerX[j] = 2000
                    print("------------- X_X Killed by Burgler X_X -------------")
                    gameover()

            check_difficulty_med = chk_score_med(score)
            check_difficulty_hard = chk_score_hard(score)
            if check_difficulty_med:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -1.0

            elif check_difficulty_hard:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -1.4

            else:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -0.7

            encounter_b = chk_encounter_b(
                p_bulletX, p_bulletY, burglerX[b], burglerY[b])
            if encounter_b:
                enemy_down = mixer.Sound("music/enemy_down.wav")
                enemy_down.play()
                p_bulletX = 50
                p_bullet = "load"
                burglerX[b] = random.randint(936, 1000)
                burglerY[b] = random.randint(0, 536)
                score += 1

            burgler(burglerX[b], burglerY[b], b)

        # Wagon All Functions
        player_dist_w = math.sqrt(math.pow(wagonX-playerX, 2) +
                                  (math.pow(wagonY-playerY, 2)))
        if player_dist_w < 70:
            wagonX = 2000
            print("------------- X_X Killed by Wagon X_X -------------")
            gameover()

        check_difficulty_med = chk_score_med(score)
        check_difficulty_hard = chk_score_hard(score)
        if check_difficulty_med:
            wagonY += wagonY_change
            if wagonY >= 536:
                wagonY_change = - 1.65
                wagonX -= wagonX_change
            elif wagonY <= 0:
                wagonY_change = 1.65
                wagonX -= wagonX_change

        elif check_difficulty_hard:
            wagonY += wagonY_change
            if wagonY >= 536:
                wagonY_change = - 2.05
                wagonX -= wagonX_change
            elif wagonY <= 0:
                wagonY_change = 2.05
                wagonX -= wagonX_change
        else:
            wagonY += wagonY_change
            if wagonY >= 536:
                wagonY_change = - 1.35
                wagonX -= wagonX_change
            elif wagonY <= 0:
                wagonY_change = 1.35
                wagonX -= wagonX_change

        encounter_w = chk_encounter_w(
            p_bulletX, p_bulletY, wagonX, wagonY)
        if encounter_w:
            enemy_down = mixer.Sound("music/enemy_down.wav")
            enemy_down.play()
            p_bulletX = 50
            p_bullet = "load"
            wagonX = random.randint(936, 1000)
            wagonY = random.randint(0, 536)
            score += 6
        wagon(wagonX, wagonY)

        if p_bulletX >= 1000:
            p_bulletX = 50
            p_bullet = "load"

        #  player bullet movement
        if p_bullet is "shoot":
            fire_p_bullet(p_bulletX, p_bulletY)
            p_bulletX += p_bulletX_change

        if e_bulletX <= 0:
            e_bulletX = gunnerX
            e_bulletY = gunnerY
            e_bullet = "load"

        #  Enemy bullet movement
        if e_bullet is "shoot":
            fire_e_bullet(e_bulletX, e_bulletY)
            e_bulletX += e_bulletX_change

        collision = chk_collision(e_bulletX, e_bulletY, playerX, playerY)
        if collision:
            e_bullet = "load"
            p_bullet = "load"

        show_score(scoreX, scoreY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -1.2
            if event.key == pygame.K_s:
                playerY_change = 1.2
            if event.key == pygame.K_SPACE:
                if p_bullet is "load":
                    gunshot = mixer.Sound("music/bullet.mp3")
                    gunshot.play()
                    p_bulletY = playerY
                    fire_p_bullet(p_bulletX, p_bulletY)

                if e_bullet is "load":
                    e_bulletX = gunnerX
                    e_bulletY = gunnerY
                    fire_e_bullet(e_bulletX, e_bulletY)

        if event.type == pygame.KEYUP:
            playerY_change = 0
        
        clock.tick(90)

    pygame.display.update()

pygame.quit()
