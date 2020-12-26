import pygame

pygame.init()
background_colour = (245, 255, 245)
(width, height) = (1300, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dining philosopher')
screen.fill(background_colour)
font = pygame.font.SysFont('arial', 24)
font1 = pygame.font.SysFont('arial ', 30, bold=True)
font2 = pygame.font.SysFont('Times ', 24)
shape_color = (0, 0, 0)

s = [1, 1, 1, 1, 1]
f = []
fx = [730, 770, 490, 280, 410]
fy = [150, 450, 590, 360, 100]
px = [540, 770, 640, 300, 260]
py = [30, 250, 540, 490, 170]
pImg = []
occupied_by = [5, 5, 5, 5, 5]
eating_process = [0, 0, 0, 0, 0]
block_process = [0, 0, 0, 0, 0]
want_stick_number = [5, 5, 5, 5, 5]
f.append(font1.render("F0", True, (0, 0, 0)))
f.append(font1.render("F1", True, (0, 0, 0)))
f.append(font1.render("F2", True, (0, 0, 0)))
f.append(font1.render("F3", True, (0, 0, 0)))
f.append(font1.render("F4", True, (0, 0, 0)))

block = font.render("BLOCK", True, (255, 0, 0))
think = font.render("THINKING", True, (255, 0, 0))
svalue = font2.render("SEMAPHORES", True, (0, 0, 0))
eating = font.render("EATING", True, (0, 158, 0))
algo = font1.render("ALGORITHM", True, (0, 158, 158))
avoid = font.render("For last process :-", True, (0, 158, 158))

instruction = pygame.image.load("DP.png")
instruction = pygame.transform.scale(instruction, (250, 450))

table = pygame.image.load("table.png")
table = pygame.transform.scale(table, (650, 650))

for i in range(5):
    st = "p" + str(i) + ".png"
    Image = pygame.image.load(st)
    pImg.append(pygame.transform.scale(Image, (100, 100)))

y = 30
n = 0
flag4 = False


def semaphore_text(i, s, sx, sy):
    semaphore = font2.render("S" + str(i) + " = " + str(s), True, (0, 0, 0))
    screen.blit(semaphore, (sx, sy))


def algorithm_text():
    image1 = pygame.image.load("DP1.jpeg")
    image1 = pygame.transform.scale(image1, (250, 300))
    image2 = pygame.image.load("DP2.jpeg")
    image2 = pygame.transform.scale(image2, (250, 300))
    screen.blit(image1, (1050, 50))
    screen.blit(image2, (1050, 400))


running = True
while running:
    screen.fill(background_colour)
    pygame.draw.circle(screen, (0, 0, 0), (550, 350), 220, 3)
    pygame.draw.rect(screen, shape_color, [900, 150, 100, 220], 3)  # block
    screen.blit(think, (905, 110))
    screen.blit(table, (225, 25))
    screen.blit(instruction, (5, 250))
    screen.blit(svalue, (5, 30))
    screen.blit(algo, (1100, 10))
    screen.blit(avoid, (1050, 365))
    algorithm_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_0] and keys[pygame.K_LEFT]:
        if s[0] == 1 and occupied_by[0] == 5:
            fx[0] = 640
            fy[0] = 90
            s[0] = 0
            occupied_by[0] = 0
            n = n + 1
        if s[0] == 0 and fx[0] != 640:
            block_process[0] = 1
            want_stick_number[0] = 0

    if keys[pygame.K_1] and keys[pygame.K_LEFT]:
        if s[1] == 1 and occupied_by[1] == 5:
            fx[1] = 790
            fy[1] = 350
            s[1] = 0
            occupied_by[1] = 1
            n = n + 1
            if n == 4:
                flag4 = True
        if s[1] == 0 and fx[1] != 790:
            block_process[1] = 1
            want_stick_number[1] = 1

    if keys[pygame.K_2] and keys[pygame.K_LEFT]:
        if s[2] == 1 and occupied_by[2] == 5:
            fx[2] = 610
            fy[2] = 580
            s[2] = 0
            occupied_by[2] = 2
            n = n + 1
            if n == 4:
                flag4 = True
        if s[2] == 0 and fx[2] != 610:
            block_process[2] = 1
            want_stick_number[2] = 2

    if keys[pygame.K_3] and keys[pygame.K_LEFT]:
        if s[3] == 1 and occupied_by[3] == 5:
            fx[3] = 310
            fy[3] = 460
            s[3] = 0
            occupied_by[3] = 3
            n = n + 1
            if n == 4:
                flag4 = True
        if s[3] == 0 and fx[3] != 310:
            block_process[3] = 1
            want_stick_number[3] = 3

    if keys[pygame.K_4] and keys[pygame.K_LEFT]:
        if s[4] == 1 and occupied_by[4] == 5:
            fx[4] = 345
            fy[4] = 155
            s[4] = 0
            occupied_by[4] = 4
            n = n + 1
            if n == 4:
                flag4 = True
        if s[4] == 0 and fx[4] != 345:
            block_process[4] = 1
            want_stick_number[4] = 4

    if keys[pygame.K_0] and keys[pygame.K_RIGHT]:
        if s[4] == 1 and occupied_by[4] == 5:
            if not flag4 and occupied_by[0] == 0:
                fx[4] = 500
                fy[4] = 80
                s[4] = 0
                occupied_by[4] = 0
                eating_process[0] = 1

        if (s[4] == 0 and fx[4] != 500 and occupied_by[0] == 0) or flag4:
            block_process[0] = 1
            want_stick_number[0] = 4
            if flag4:
                flag4 = False

    if keys[pygame.K_1] and keys[pygame.K_RIGHT]:
        if s[0] == 1 and occupied_by[0] == 5 and s[1] == 0:
            if not flag4 and occupied_by[1] == 1:
                fx[0] = 780
                fy[0] = 220
                s[0] = 0
                occupied_by[0] = 1
                eating_process[1] = 1
        if (s[0] == 0 and fx[0] != 780 and occupied_by[1] == 1) or flag4:
            block_process[1] = 1
            want_stick_number[1] = 0
            if flag4:
                flag4 = False

    if keys[pygame.K_2] and keys[pygame.K_RIGHT]:
        if s[1] == 1 and occupied_by[1] == 5 and s[2] == 0:
            if not flag4 and occupied_by[2] == 2:
                fx[1] = 710
                fy[1] = 520
                s[1] = 0
                occupied_by[1] = 2
                eating_process[2] = 1
        if (s[1] == 0 and fx[1] != 710 and occupied_by[2] == 2) or flag4:
            block_process[2] = 1
            want_stick_number[2] = 1
            if flag4:
                flag4 = False

    if keys[pygame.K_3] and keys[pygame.K_RIGHT]:
        if s[2] == 1 and occupied_by[2] == 5 and s[3] == 0:
            if not flag4 and occupied_by[3] == 3:
                fx[2] = 400
                fy[2] = 555
                s[2] = 0
                occupied_by[2] = 3
                eating_process[3] = 1
        if (s[2] == 0 and fx[2] != 400 and occupied_by[3] == 3) or flag4:
            block_process[3] = 1
            want_stick_number[3] = 2
            if flag4:
                flag4 = False

    if keys[pygame.K_4] and keys[pygame.K_RIGHT]:
        if s[3] == 1 and occupied_by[3] == 5 and s[4] == 0:
            if not flag4 and occupied_by[4] == 4:
                fx[3] = 290
                fy[3] = 270
                s[3] = 0
                occupied_by[3] = 4
                eating_process[4] = 1
        if (s[3] == 0 and fx[3] != 290 and occupied_by[4] == 4) or flag4:
            block_process[4] = 1
            want_stick_number[4] = 3
            if flag4:
                flag4 = False

    if block_process[0] == 1:  # p0 block
        screen.blit(block, (560, 10))

    if block_process[1] == 1:  # p1 block
        screen.blit(block, (790, 230))

    if block_process[2] == 1:  # p2 block
        screen.blit(block, (655, 630))

    if block_process[3] == 1:  # p3 block
        screen.blit(block, (315, 580))

    if block_process[4] == 1:  # p4 block
        screen.blit(block, (270, 150))

    if eating_process[0] == 1:
        screen.blit(eating, (px[0] + 10, py[0] - 20))
    else:
        p0 = font.render("P0", True, (0, 0, 0))
        screen.blit(p0, (940, 200))
    if eating_process[1] == 1:
        screen.blit(eating, (px[1] + 10, py[1] - 20))
    else:
        p1 = font.render("P1", True, (0, 0, 0))
        screen.blit(p1, (940, 230))
    if eating_process[2] == 1:
        screen.blit(eating, (px[2] + 15, py[2] + 100))
    else:
        p2 = font.render("P2", True, (0, 0, 0))
        screen.blit(p2, (940, 260))
    if eating_process[3] == 1:
        screen.blit(eating, (px[3] + 10, py[3] + 100))
    else:
        p3 = font.render("P3", True, (0, 0, 0))
        screen.blit(p3, (940, 290))
    if eating_process[4] == 1:
        screen.blit(eating, (px[4] + 10, py[4] - 20))
    else:
        p4 = font.render("P4", True, (0, 0, 0))
        screen.blit(p4, (940, 320))

    if keys[pygame.K_0] and keys[pygame.K_r]:
        eating_process[0] = 0
        block_process[0] = 0
        for i in range(5):
            if occupied_by[i] == 0:
                if i == 0:
                    fx[0] = 730
                    fy[0] = 150
                    s[0] = 1
                    occupied_by[0] = 5
                    if want_stick_number[1] == 0:
                        block_process[1] = 0
                if i == 4:
                    fx[4] = 410
                    fy[4] = 100
                    s[4] = 1
                    occupied_by[4] = 5
                    if want_stick_number[4] == 4:
                        block_process[4] = 0
        if n > 0:
            n = n - 1

    if keys[pygame.K_1] and keys[pygame.K_r]:
        eating_process[1] = 0
        block_process[1] = 0
        for i in range(5):
            if occupied_by[i] == 1:
                if i == 0:
                    fx[0] = 730
                    fy[0] = 150
                    s[0] = 1
                    occupied_by[0] = 5
                    if want_stick_number[0] == 0:
                        block_process[0] = 0
                if i == 1:
                    fx[1] = 770
                    fy[1] = 450
                    s[1] = 1
                    occupied_by[1] = 5
                    if want_stick_number[2] == 1:
                        block_process[2] = 0
        if n > 0:
            n = n - 1

    if keys[pygame.K_2] and keys[pygame.K_r]:
        eating_process[2] = 0
        block_process[2] = 0
        for i in range(5):
            if occupied_by[i] == 2:
                if i == 2:
                    fx[2] = 490
                    fy[2] = 590
                    s[2] = 1
                    occupied_by[2] = 5
                    if want_stick_number[3] == 2:
                        block_process[3] = 0
                if i == 1:
                    fx[1] = 770
                    fy[1] = 450
                    s[1] = 1
                    occupied_by[1] = 5
                    if want_stick_number[1] == 1:
                        block_process[1] = 0
        if n > 0:
            n = n - 1

    if keys[pygame.K_3] and keys[pygame.K_r]:
        eating_process[3] = 0
        block_process[3] = 0
        for i in range(5):
            if occupied_by[i] == 3:
                if i == 2:
                    fx[2] = 490
                    fy[2] = 590
                    s[2] = 1
                    occupied_by[2] = 5
                    if want_stick_number[2] == 2:
                        block_process[2] = 0
                if i == 3:
                    fx[3] = 280
                    fy[3] = 360
                    s[3] = 1
                    occupied_by[3] = 5
                    if want_stick_number[4] == 3:
                        block_process[4] = 0
        if n > 0:
            n = n - 1

    if keys[pygame.K_4] and keys[pygame.K_r]:
        eating_process[4] = 0
        block_process[4] = 0
        for i in range(5):
            if occupied_by[i] == 4:
                if i == 4:
                    fx[4] = 410
                    fy[4] = 100
                    s[4] = 1
                    occupied_by[4] = 5
                    if want_stick_number[0] == 4:
                        block_process[0] = 0
                if i == 3:
                    fx[3] = 280
                    fy[3] = 360
                    s[3] = 1
                    occupied_by[3] = 5
                    if want_stick_number[3] == 3:
                        block_process[3] = 0
        if n > 0:
            n = n - 1

    for i in range(5):
        y = y + 30
        screen.blit(pImg[i], (px[i], py[i]))
        screen.blit(f[i], (fx[i], fy[i]))
        semaphore_text(i, s[i], 10, y)
    y = 30
    pygame.display.update()
