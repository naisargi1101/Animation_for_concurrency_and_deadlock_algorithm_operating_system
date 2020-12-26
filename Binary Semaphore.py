import pygame

pygame.init()
background_colour = (245, 255, 245)
(width, height) = (1010, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Binary Semaphore')
screen.fill(background_colour)
font = pygame.font.SysFont('arial', 24)
font1 = pygame.font.SysFont('arial ', 20, bold=True)
font2 = pygame.font.SysFont('Times ', 18)
shape_color = (0, 0, 0)
s = 1
p = 0
flag = False
count = 0

pImg = []
px = []
py = []
py_change = []
px_change = 0.2
for i in range(2):
    st = "p" + str(i + 1) + ".png"
    pImage = pygame.image.load(st)
    pImg.append(pygame.transform.scale(pImage, (100, 100)))
    py_change.append(0.2)
    if i == 0:
        px.append(150)
    else:
        px.append(px[i - 1] + 280)
    py.append(300)


def signal_text(x, y):
    signal = font.render("SIGNAL() ", True, (0, 100, 0))
    screen.blit(signal, (x, y + 100))


def algo_text():
    x = 770
    y = 180
    l1 = font2.render("WAIT(semaphore s){ ", True, (0, 0, 0))
    l2 = font2.render("   if (s.value == 1) { ", True, (0, 0, 0))
    l3 = font2.render("        s.value = 0;", True, (0, 0, 0))
    l4 = font2.render("    }", True, (0, 0, 0))
    l5 = font2.render("   else {", True, (0, 0, 0))
    l6 = font2.render("        //Block the process", True, (0, 100, 0))
    l7 = font2.render("         Sleep();} ", True, (0, 0, 0))
    l8 = font2.render("} ", True, (0, 0, 0))
    l9 = font2.render("SIGNAL(Semaphore s){ ", True, (0, 0, 0))
    l10 = font2.render("   s = 1; }", True, (0, 0, 0))

    screen.blit(l1, (x, y))
    screen.blit(l2, (x, y + 20))
    screen.blit(l3, (x, y + 40))
    screen.blit(l4, (x, y + 60))
    screen.blit(l5, (x, y + 80))
    screen.blit(l6, (x, y + 100))
    screen.blit(l7, (x, y + 120))
    screen.blit(l8, (x, y + 140))
    screen.blit(l9, (x, y + 180))
    screen.blit(l10, (x, y + 200))


def stand_person(x, y, j):
    screen.blit(pImg[j], (x, y))


def BLOCK_text():
    blck = font1.render("BLOCK QUEUE ", True, (255, 0, 0))
    screen.blit(blck, (560, 390))


def wait_text(x, y):
    wai = font.render("WAIT() ", True, (255, 0, 0))
    screen.blit(wai, (x + 10, y + 110))


def complete_text(x, y):
    complete = font.render("Completed ", True, (255, 0, 0))
    screen.blit(complete, (x - 10, y + 110))


def semaphore_text():
    pygame.draw.ellipse(screen, shape_color, ((260, 50), (170, 70)), 4)
    semaphore = font.render("Semaphore " + str(s), True, (0, 100, 240))
    screen.blit(semaphore, (285, 70))


running = True
while running:
    screen.fill(background_colour)
    semaphore_text()
    algo_text()
    pygame.draw.rect(screen, shape_color, [50, 500, 615, 150], 4)
    bs = font1.render("BINARY SEMAPHORE", True, (255, 255, 255), (0, 130, 120))
    cs = font.render("Critical Section ", True, (0, 130, 120))
    screen.blit(cs, (300, 650))
    screen.blit(bs, (780, 100))
    Start = font.render("Press 's' to Start", True, (190, 14, 76))
    screen.blit(Start, (790, 50))
    pygame.draw.rect(screen, shape_color, [570, 150, 100, 220], 3)
    pygame.draw.rect(screen, shape_color, [760, 170, 250, 330], 2)  # code
    BLOCK_text()
    pygame.draw.line(screen, (0, 0, 0), (760, 350), (1010, 350), 2)
    screen.blit(cs, (290, 790))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        p = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not flag:  # before cs
        if p == 1:
            py[0] = py[0] - py_change[0]
            if py[0] < 100:
                py[0] = 100
                py_change[0] = -0.2
                s = 0
            if py[0] >= 520:
                py[0] = 520
                py_change[1] = 0.2
                p = 2
            if s == 1:
                wait_text(px[0], py[0])

        elif p == 2:
            py[1] = py[1] - py_change[1]
            if count == 0:
                wait_text(px[1], py[1])
            if py[1] < 100:
                py[1] = 100
                py_change[1] = -0.2
                count = 1
            if py[1] > 200 and count == 1:
                py[1] = 200
                py_change[1] = 0
            if count == 1 and py[1] == 200:
                px[1] = px[1] + px_change
                if px[1] >= 570:
                    px[1] = 570
                    py_change[1] = 0.2
                    count = 0
                    p = 1
                    flag = True

    else:  # after cs
        if p == 1:
            py[0] = py[0] + py_change[0]
            signal_text(px[0], py[0])
            if py[0] < 100:
                py[0] = 100
                py_change[0] = 0
                complete_text(px[0], py[0])
                s = 1
                p = 2

        elif p == 2:
            complete_text(px[0], py[0])
            if count == 0:
                px[1] = px[1] - px_change
                if px[1] <= 450:
                    px[1] = 450
                    count = 1
                    s = 0
            else:
                py[1] = py[1] + py_change[1]
            if py[1] < 100 and count > 1:
                py[1] = 100
                py_change[1] = -0.2
                count += 1
            if count == 2:
                signal_text(px[1], py[1])
            if count == 1 and py[1] < 400:
                wait_text(px[1], py[1])
            if py[1] > 520:
                count = 2
                py[1] = 520
                pygame.time.delay(2000)
                py_change[1] = -0.2
            if count == 3:
                complete_text(px[1], py[1])
                s = 1
                p = 3

        elif p == 3:
            complete_text(px[0], py[0])
            complete_text(px[1], py[1])

    for i in range(len(px)):
        stand_person(px[i], py[i], i)
    pygame.display.update()
