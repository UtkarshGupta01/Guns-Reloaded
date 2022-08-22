import pygame
import random
import math
from pygame import mixer

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
e_bulletimg = pygame.image.load("assets/e_bullet.png")
w = e_bulletimg.get_width()
h = e_bulletimg.get_height()
e_bulletimg = pygame.transform.scale(e_bulletimg, (int(w*0.8), int(h*0.8)))
e_bulletX = 0
e_bulletY = 0
e_bulletX_change = -1.8
e_bulletY_change = 0

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


def fire_p_bullet(x, y):
    global p_bullet
    p_bullet = "shoot"
    screen.blit(p_bulletimg, (x+75, y+38))


def fire_e_bullet(x, y):
    global e_bullet
    screen.blit(e_bulletimg, (x, y+10))


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

        for g in range(gunners):
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

        for b in range(burglers):
            player_dist_b = math.sqrt(math.pow(burglerX[b]-playerX, 2) +
                                      (math.pow(burglerY[b]-playerY, 2)))
            if player_dist_b < 70:
                for j in range(burglers):
                    burglerX[j] = 2000
                    # gunnerX[j] = 2000
                # screen.fill((0,0,0))
                # screen.blit(endgame, (0, 0))
                # game_sound.stop()
                gameover()
                # for play_again in pygame.event.get():
                #     if play_again.type == pygame.QUIT:
                #         playing = False
                #     if play_again.type == pygame.KEYDOWN:
                #         if play_again.key == pygame.K_r:
                #             play_game = True
                #         if play_again.key == pygame.K_ESCAPE:
                #             playing = False

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

        show_score(scoreX, scoreY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

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

        if event.type == pygame.KEYUP:
            playerY_change = 0

    pygame.display.update()

pygame.quit()
