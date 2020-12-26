import pygame

pygame.init()
s = 3
p = 0
count = 0
flag = False
background_colour = (253, 255, 255)
(width, height) = (1250, 780)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Counting Semaphore')
screen.fill(background_colour)
font = pygame.font.SysFont('arial', 24)
font1 = pygame.font.SysFont('arial', 18, bold=True)
font2 = pygame.font.SysFont('Times', 18)
shape_color = (0, 0, 0)
pImg = []
px = []
py = []
px_change = []
py_change = []

for i in range(5):
    st = "p" + str(i + 1) + ".png"
    standImage = pygame.image.load(st)
    pImg.append(pygame.transform.scale(standImage, (100, 100)))
    py_change.append(0.4)
    px_change.append(0)
    if i == 0:
        px.append(100)
    else:
        px.append(px[i - 1] + 150)
    py.append(300)


def algo_text():
    x = 1030
    y = 280
    l1 = font2.render("WAIT(semaphore s){ ", True, (0, 0, 0))
    l2 = font2.render("      s = s – 1;", True, (0, 0, 0))
    l3 = font2.render("      if (s <= 0){       ", True, (0, 0, 0))
    l4 = font2.render("             //Block the process", True, (0, 0, 0))
    l5 = font2.render("             sleep() }", True, (0, 0, 0))
    l6 = font2.render("}", True, (0, 100, 0))
    l7 = font2.render("SIGNAL (semaphore s){", True, (0, 0, 0))
    l8 = font2.render("      s = s + 1;", True, (0, 0, 0))
    l9 = font2.render("      if (s <= 0){", True, (0, 0, 0))
    l10 = font2.render("            //wake up the process", True, (0, 0, 0))
    l11 = font2.render("             //from block queue}", True, (0, 0, 0))
    l12 = font2.render("             wakeup()}", True, (0, 0, 0))
    l13 = font2.render("}", True, (0, 0, 0))

    screen.blit(l1, (x, y))
    screen.blit(l2, (x, y + 20))
    screen.blit(l3, (x, y + 40))
    screen.blit(l4, (x, y + 60))
    screen.blit(l5, (x, y + 80))
    screen.blit(l6, (x, y + 100))
    screen.blit(l7, (x, y + 140))
    screen.blit(l8, (x, y + 160))
    screen.blit(l9, (x, y + 180))
    screen.blit(l10, (x, y + 200))
    screen.blit(l11, (x, y + 220))
    screen.blit(l12, (x, y + 240))
    screen.blit(l13, (x, y + 260))


def signal_text(x, y):
    signal = font.render("SIGNAL() ", True, (0, 100, 0))
    screen.blit(signal, (x, y + 100))


def BLOCK_text():
    blck = font.render("BLOCK QUEUE ", True, (255, 0, 0))
    screen.blit(blck, (830, 300))


def wait_text(x, y):
    blck = font.render("WAIT() ", True, (255, 0, 0))
    screen.blit(blck, (x + 10, y + 100))


def complete_text(x, y):
    complete = font.render("Completed ", True, (255, 0, 0))
    screen.blit(complete, (x - 10, y + 110))


def semaphore_text():
    pygame.draw.ellipse(screen, shape_color, ((410, 50), (170, 70)), 4)
    semaphore = font.render("Semaphore " + str(s), True, (0, 100, 240))
    screen.blit(semaphore, (435, 70))


running = True
while running:
    screen.fill(background_colour)
    semaphore_text()
    algo_text()
    pygame.draw.rect(screen, shape_color, [55, 500, 900, 200], 4)
    pygame.draw.rect(screen, shape_color, [850, 80, 100, 220], 3)
    pygame.draw.rect(screen, shape_color, [1020, 260, 230, 310], 2)
    pygame.draw.line(screen, (0, 0, 0), (1020, 410), (1250, 410), 2)
    BLOCK_text()
    Start = font.render("Press 's' to Start", True, (190, 14, 76))
    screen.blit(Start, (1030, 150))
    bs = font1.render("COUNTING SEMAPHORE", True, (255, 255, 255), (0, 130, 120))
    cs = font.render("CRITICAL SECTION ", True, (0, 100, 240))
    screen.blit(cs, (450, 700))
    screen.blit(bs, (1030, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        p = 1
    if not flag:  # before cs
        if p == 1:  # up
            py[0] = py[0] - py_change[0]
            if py[0] <= 74.8:
                py[0] = 75
                py_change[0] = -0.4
                s = s - 1
            if py[0] >= 550:
                py[0] = 550
                p = 2
            if s == 3:
                wait_text(px[0], py[0])

        elif p == 2:
            py[1] = py[1] - py_change[1]
            if py[1] <= 74.8:
                py[1] = 75
                py_change[1] = -0.4
                s = s - 1
            if py[1] >= 550:
                py[1] = 550
                p = 3
            if s == 2:
                wait_text(px[1], py[1])
        elif p == 3:
            py[2] = py[2] - py_change[2]
            if py[2] <= 110:
                py[2] = 110
                py_change[2] = -0.4
                s = s - 1
            if py[2] >= 550:
                py[2] = 550
                p = 4
            if s == 1:
                wait_text(px[2], py[2])
        elif p == 4:
            py[3] = py[3] - py_change[3]
            px[3] = px[3] - px_change[3]
            if py[3] < 80:
                py[3] = 80
                py_change[3] = 0
                px_change[3] = -0.3
                s = s - 1
            if px[3] >= 850:
                px_change[3] = 0.4
                p = 5
            if s == 0:
                wait_text(px[3], py[3])
        elif p == 5:
            py[4] = py[4] - py_change[4]
            px[4] = px[4] - px_change[4]
            if s == -1:
                wait_text(px[4], py[4])
            if py[4] < 100:
                py[4] = 100
                py_change[4] = -0.4
                count = 1
                s = s - 1
            if py[4] >= 200 and count == 1:
                py_change[4] = 0
                px_change[4] = -0.4
            if px[4] > 850:
                px[4] = 850
                px_change[4] = 0.4
                py_change[4] = 0
                p = 1
                flag = True

    else:
        if p == 1:
            if s == -2:
                py[0] = py[0] + py_change[0]
                signal_text(px[0], py[0])
                if py[0] <= 110:
                    py[0] = 110
                    py_change[0] = 0.4
                    s = s + 1
                    complete_text(px[0], py[0])

            if s == -1:
                complete_text(px[0], py[0])
                px[3] = px[3] - px_change[3]
                py[3] = py[3] - py_change[3]
                if px[3] < 550:
                    px[3] = 550
                    py_change[3] = -0.4
                    px_change[3] = 0
                if py[3] > 550:
                    py[3] = 550
                    p = 2

        elif p == 2:
            complete_text(px[0], py[0])
            if s == -1:
                py[1] = py[1] + py_change[1]
                signal_text(px[1], py[1])
                if py[1] <= 110:
                    py[1] = 110
                    py_change[1] = 0.4
                    s = s + 1
                    complete_text(px[1], py[1])
            if s == 0:
                complete_text(px[1], py[1])
                px[4] = px[4] - px_change[4]
                py[4] = py[4] - py_change[4]
                if px[4] < 700:
                    px[4] = 700
                    py_change[4] = -0.4
                    px_change[4] = 0
                if py[4] > 550:
                    py[4] = 550
                    p = 3
        elif p == 3:
            complete_text(px[0], py[0])
            complete_text(px[1], py[1])
            py[2] = py[2] + py_change[2]
            signal_text(px[2], py[2])
            if py[2] <= 110:
                py[2] = 110
                py_change[2] = 0.4
                s = s + 1
                complete_text(px[2], py[2])
                p = 4
        elif p == 4:
            for i in range(3):
                complete_text(px[i], py[i])
            py[3] = py[3] + py_change[3]
            signal_text(px[3], py[3])
            if py[3] <= 110:
                py[3] = 110
                py_change[3] = 0.4
                s = s + 1
                complete_text(px[3], py[3])
                p = 5
        elif p == 5:
            for i in range(4):
                complete_text(px[i], py[i])
            py[4] = py[4] + py_change[4]
            signal_text(px[4], py[4])
            if py[4] <= 110:
                py[4] = 110
                py_change[4] = 0.4
                p = 6
                s = 3
                complete_text(px[4], py[4])
        else:
            for i in range(5):
                complete_text(px[i], py[i])
            # running = False

    for i in range(len(px)):
        screen.blit(pImg[i], (px[i], py[i]))
    pygame.display.update()
