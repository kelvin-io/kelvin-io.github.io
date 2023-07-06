import pygame, random

pygame.init()
screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
pygame.display.set_caption("Game")
FPS = 60
clock = pygame.time.Clock()

player = pygame.image.load("player.jpg")
player_pos = [50,400]
player_speed = 5

icon = player.convert_alpha()
pygame.display.set_icon(icon)

bullets_num = 10
bullets, bullets_pos, bullets_time = [], [], []
for i in range(bullets_num):
    bullets.append(pygame.image.load("bullet.jpg"))
    bullets_pos.append([550,random.randint(50,450)])
    bullets_time.append((i+1)*1000)
bullets_speed = 5

def key_control():
    global player_pos,player_speed
    key_states = pygame.key.get_pressed()
    if key_states[pygame.K_d]:
        player_pos[0] += player_speed
    if key_states[pygame.K_a]:
        player_pos[0] -= player_speed
    if key_states[pygame.K_w]:
        player_pos[1] -= player_speed
    if key_states[pygame.K_s]:
        player_pos[1] += player_speed

def bullet_control(i,time):
    global bullets_pos, bullets_time, bullets_speed, player_pos
    if bullets_time[i] == -1:
        if bullets_pos[i][0] <= 0:
            bullets_pos[i] = [550,random.randint(50,450)]
            if i == 0:
                bullets_pos[i][1] = player_pos[1]
        else:
            bullets_pos[i][0] -= bullets_speed
    else:
        new_time = pygame.time.get_ticks()
        if  new_time-time >= bullets_time[i]:
            bullets_time[i] = -1

def collide_control(time):
    global bullets_pos, player_pos
    for b in bullets_pos:
        if abs(b[0]-player_pos[0]) < 30 and (b[1]-player_pos[1] > -11 and b[1]-player_pos[1] < 40):
            return show_result(time)
    return 0

def show_result(time):
    final_time = (pygame.time.get_ticks()-time)/1000
    fonts = pygame.font.get_fonts()
    font = pygame.font.SysFont(fonts[0], 20)
    text = f'Time: {final_time} seconds'
    text = font.render(text, True, (255, 0, 0))
    return text

def quit_control(forever=False):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
        if not forever:
            break
    return 0

time = pygame.time.get_ticks()
while True:
    clock.tick(FPS)
    screen.fill((0,0,0))
    key_control()
    screen.blit(player, tuple(player_pos))
    for i in range(bullets_num):
        screen.blit(bullets[i], tuple(bullets_pos[i]))
        bullet_control(i,time)
    if quit_control() == -1:
        break
    text = collide_control(time)
    if text:
        screen.blit(text, (100,100))
        pygame.display.update()
        quit_control(forever=True)
        break
    pygame.display.update()

pygame.quit()
