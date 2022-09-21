import pygame
import random
import math
from pygame import mixer
import time

pygame.init()

# Window
screen = pygame.display.set_mode((1000, 600))

# Icon and Caption
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("First Hit Redemption")

# Intro Music
mixer.music.load("music/intro_music.wav")
mixer.music.play()

# background
back = pygame.image.load("assets/land.png")

# Intro Icon
intro_icon = pygame.image.load("assets/player.png")
w = intro_icon.get_width()
h = intro_icon.get_height()
intro_icon = pygame.transform.scale(intro_icon, (int(w*2.2), int(h*2.2)))

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
playerimg = pygame.transform.scale(playerimg, (int(w*1.5), int(h*1.5)))
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
p_bulletX_change = 2.4
p_bulletY_change = 0
p_bullet = "load"

# Power-ups
dash_powerimg = pygame.image.load("assets/dash.png")
w = dash_powerimg.get_width()
h = dash_powerimg.get_height()
dash_powerimg = pygame.transform.scale(dash_powerimg, (int(w*1), int(h*1)))
dash_powerX = random.randint(936, 1000)
dash_powerY = random.randint(0, 536)
dash_powerY_change = 0
dash_powerX_change = -0.4

shield_powerimg = pygame.image.load("assets/shield.png")
w = shield_powerimg.get_width()
h = shield_powerimg.get_height()
shield_powerimg = pygame.transform.scale(
    shield_powerimg, (int(w*0.8), int(h*0.8)))
shield_powerX = random.randint(936, 1000)
shield_powerY = random.randint(0, 536)
shield_powerY_change = 0
shield_powerX_change = -0.4


# Enemy1(gunner)
gunnerimg = []
gunnerX = []
gunnerY = []
gunnerX_change = []
gunnerY_change = []
gunners = 3
for g in range(gunners):
    gunnerimg.append(pygame.image.load("assets/gunner.png"))
    gunnerX.append(random.randint(936, 1000))
    gunnerY.append(random.randint(0, 536))
    gunnerX_change.append(70)
    gunnerY_change.append(0.6)

# Enemy Bullet
e_bulletimg = []
# w = e_bulletimg.get_width()
# h = e_bulletimg.get_height()
# e_bulletimg = pygame.transform.scale(e_bulletimg, (int(w*0.8), int(h*0.8)))
e_bulletX = []
e_bulletY = []
e_bulletX_change = []
e_bulletY_change = []
e_bullet = []
bullets = 3

for e in range(bullets):
    e_bulletimg.append(pygame.image.load("assets/e_bullet.png"))
    e_bulletX.append(0)
    e_bulletY.append(0)
    e_bulletX_change.append(-1.8)
    e_bulletY_change.append(0)
    e_bullet.append("load")

# Enemy2(burgler)
burglerimg = []
burglerX = []
burglerY = []
burglerX_change = []
burglerY_change = []
burglers = 5

for b in range(burglers):
    burglerimg.append(pygame.image.load("assets/burgler.png"))
    burglerX.append(random.randint(936, 1000))
    burglerY.append(random.randint(0, 536))
    burglerX_change.append(-0.5)
    burglerY_change.append(0)


def player(x, y):
    screen.blit(playerimg, (x, y))


def gunner(x, y, g):
    screen.blit(gunnerimg[g], (x, y))


def burgler(x, y, b):
    screen.blit(burglerimg[b], (x, y))


def dash_power(x, y):
    screen.blit(dash_powerimg, (x, y))


def shield_power(x, y):
    screen.blit(shield_powerimg, (x, y))


def dash_get(dash_powerX, dash_powerY, playerX, playerY):
    distance = math.sqrt((math.pow(dash_powerX - playerX, 2)) +
                         (math.pow(dash_powerY - playerY, 2)))
    if distance < 50:
        return True
    else:
        return False


def shield_get(shield_powerX, shield_powerY, playerX, playerY):
    distance = math.sqrt((math.pow(shield_powerX - playerX, 2)) +
                         (math.pow(shield_powerY - playerY, 2)))
    if distance < 50:
        return True
    else:
        return False


def fire_p_bullet(x, y):
    global p_bullet
    p_bullet = "shoot"
    screen.blit(p_bulletimg, (x+75, y+38))


def fire_e_bullet(x, y, e):
    global e_bullet
    e_bullet[e] = "shoot"
    screen.blit(e_bulletimg[e], (x, y))


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


def chk_encounter_e(e_bulletX, e_bulletY, playerX, playerY):
    global player_dist
    player_dist = math.sqrt(math.pow(playerX-e_bulletX, 2) +
                            (math.pow(playerY-e_bulletY, 2)))

    if player_dist < 55:
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
intro_txt = pygame.font.Font("freesansbold.ttf", 60)
play_txt = pygame.font.Font("freesansbold.ttf", 30)
exit_txt = pygame.font.Font("freesansbold.ttf", 30)

# control
controls_txt = pygame.font.Font("freesansbold.ttf", 20)

# Game Over
gameover_txt = pygame.font.Font("freesansbold.ttf", 80)
total_txt = pygame.font.Font("freesansbold.ttf", 40)
# restart_txt = pygame.font.Font("freesansbold.ttf", 30)
quit_txt = pygame.font.Font("freesansbold.ttf", 30)

# Score
score = 0
score_txt = pygame.font.Font("freesansbold.ttf", 30)
scoreX = 10
scoreY = 10

play_game = False
playing = True

# Time
time_rem = 5


while playing:

    # main menu
    if play_game == False:

        screen.blit(back, (0, 0))

        intro_font = intro_txt.render(
            "FIRST HIT REDEMPTION", True, (102, 51, 0))
        screen.blit(intro_font, (150, 50))

        screen.blit(intro_icon, (440, 130))

        play_font = play_txt.render(
            "Press SPACE to Play", True, (0, 0, 0))
        screen.blit(play_font, (360, 370))

        quit_font = quit_txt.render(
            "Press ESC to QUIT", True, (0, 0, 0))
        screen.blit(quit_font, (370, 410))

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

        # Powers

        dash_powerX += dash_powerX_change
        if dash_powerX <= 0:
            dash_powerX = random.randint(936, 1000)
            dash_powerY = random.randint(0, 536)
            dash_powerX_change = -0.5
        dash_power(dash_powerX, dash_powerY)

        check_dash = dash_get(dash_powerX, dash_powerY, playerX, playerY)
        if check_dash:
            print("Dash Power Up")
            dash_powerX = random.randint(936, 1000)
            dash_powerY = random.randint(0, 536)

        shield_powerX += shield_powerX_change
        if shield_powerX <= 0:
            shield_powerX = random.randint(936, 1000)
            shield_powerY = random.randint(0, 536)
            shield_powerX_change = -0.5
        shield_power(shield_powerX, shield_powerY)

        for g in range(gunners):
            player_dist_g = math.sqrt(math.pow(gunnerX[g]-playerX, 2) +
                                      (math.pow(gunnerY[g]-playerY, 2)))
            if player_dist_g < 70:
                for j in range(gunners):
                    gunnerX[j] = 2000
                    gameover()

            check_difficulty_med = chk_score_med(score)
            check_difficulty_hard = chk_score_hard(score)
            if check_difficulty_med:
                gunnerY[g] += gunnerY_change[g]
                if gunnerY[g] >= 536:
                    gunnerY_change[g] = - 0.8
                    gunnerX[g] -= gunnerX_change[g]
                elif gunnerY[g] <= 0:
                    gunnerY_change[g] = 0.8
                    gunnerX[g] -= gunnerX_change[g]

            elif check_difficulty_hard:
                gunnerY[g] += gunnerY_change[g]
                if gunnerY[g] >= 536:
                    gunnerY_change[g] = - 1.2
                    gunnerX[g] -= gunnerX_change[g]
                elif gunnerY[g] <= 0:
                    gunnerY_change[g] = 1.2
                    gunnerX[g] -= gunnerX_change[g]

            else:
                gunnerY[g] += gunnerY_change[g]
                if gunnerY[g] >= 536:
                    gunnerY_change[g] = - 0.6
                    gunnerX[g] -= gunnerX_change[g]
                elif gunnerY[g] <= 0:
                    gunnerY_change[g] = 0.6
                    gunnerX[g] -= gunnerX_change[g]

            encounter_g = chk_encounter_g(
                p_bulletX, p_bulletY, gunnerX[g], gunnerY[g])
            if encounter_g:
                enemy_down = mixer.Sound("music/enemy_down.wav")
                enemy_down.play()
                p_bulletX = 50
                p_bullet = "load"
                gunnerX[g] = random.randint(936, 1000)
                gunnerY[g] = random.randint(0, 536)
                score += 2
            gunner(gunnerX[g], gunnerY[g], g)

            # if(player_dist_g > 70):
            #     if(gunnerY[g] == playerY):
            #         for e in range(bullets):
            #             e_bulletY[e] = gunnerY[g]
            #             e_bulletX[e] = gunnerX[g]
            #             fire_e_bullet(e_bulletX[e], e_bulletY[e], e)

        for b in range(burglers):
            player_dist_b = math.sqrt(math.pow(burglerX[b]-playerX, 2) +
                                      (math.pow(burglerY[b]-playerY, 2)))
            if player_dist_b < 70:
                for j in range(burglers):
                    burglerX[j] = 2000
                    gameover()

            check_difficulty_med = chk_score_med(score)
            check_difficulty_hard = chk_score_hard(score)
            if check_difficulty_med:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -0.8

            elif check_difficulty_hard:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -1.2

            else:
                burglerX[b] += burglerX_change[b]
                if burglerX[b] <= 0:
                    burglerX[b] = random.randint(936, 1000)
                    burglerY[b] = random.randint(0, 536)
                    burglerX_change[b] = -0.5

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

        if p_bulletX >= 1000:
            p_bulletX = 50
            p_bullet = "load"

        #  player bullet movement
        if p_bullet is "shoot":
            fire_p_bullet(p_bulletX, p_bulletY)
            p_bulletX += p_bulletX_change


        if e_bulletX[e] <= 0:
            e_bulletX[e] = gunnerX[g]
            e_bulletY[e] = gunnerY[g]
            e_bullet[e] = "load"

        #  Enemy bullet movement
        if e_bullet[e] is "shoot":
            fire_e_bullet(e_bulletX[e], e_bulletY[e],e)
            e_bulletX[e] += e_bulletX_change[e]

        show_score(scoreX, scoreY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # dash_power = dash_get(dash_powerX, dash_powerY, playerX, playerY)
        # if dash_power:
        #     while(dash_count < 10):
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_w:
        #                 playerY_change = -1.1
        #             if event.key == pygame.K_s:
        #                 playerY_change = 1.1
        #             if event.key == pygame.K_SPACE:
        #                 if p_bullet is "load":
        #                     dash_count +=1
        #                     gunshot = mixer.Sound("music/bullet.mp3")
        #                     gunshot.play()
        #                     p_bulletY = playerY
        #                     fire_p_bullet(p_bulletX, p_bulletY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -0.7
            if event.key == pygame.K_s:
                playerY_change = 0.7
            if event.key == pygame.K_SPACE:
                if p_bullet is "load":
                    gunshot = mixer.Sound("music/bullet.mp3")
                    gunshot.play()
                    p_bulletY = playerY
                    fire_p_bullet(p_bulletX, p_bulletY)
                for g in range(gunners):
                    for e in range(bullets):
                        if e_bullet[e] is "load":
                            e_bulletX[e] = gunnerX[g]
                            e_bulletY[e] = gunnerY[g]
                            fire_e_bullet(e_bulletX[e], e_bulletY[e],e)

        if event.type == pygame.KEYUP:
            playerY_change = 0

    pygame.display.update()

pygame.quit()
