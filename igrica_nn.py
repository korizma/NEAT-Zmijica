import pygame
import neat
import time
import zmijica

size = 100
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)

def analiziraj_outpute(out):
    max = 0
    for k in out:
        if k > max:
            max = k
    index = out.index(max)
    return index+1

def play_game(genome, config):
    global size, red, green, white
    pygame.init()
    gw = pygame.display.set_mode((zmijica.H*size, zmijica.H*size))

    igra = zmijica.Igra()
    igra.nova_igra()

    net = neat.nn.RecurrentNetwork.create(genome, config)

    inputs = igra.prebaci_u_niz()
    out =  net.activate(inputs)
    smer = analiziraj_outpute(out)

    while igra.pomeri_zmiju(smer):
        refresh_display(gw, igra)
        time.sleep(0.5)

        inputs = igra.prebaci_u_niz()
        out = net.activate(inputs)
        smer = analiziraj_outpute(out)
        print(len(igra.zmija))

    print("Gotova igra, rezultat je: "+str(len(igra.zmija)))
    print("Broj poteza je: " + str(igra.uk_broj_poteza))


def refresh_display(display, igra):
    global size, red, green, white
    for value in igra.zmija:
        x = value.x
        y = value.y
        pygame.draw.rect(display, green, pygame.Rect(x*size, y*size, size, size))
    for value in igra.ostatak:
        x = value.x
        y = value.y
        pygame.draw.rect(display, white, pygame.Rect(x * size, y * size, size, size))

    pygame.draw.rect(display, red, pygame.Rect(igra.jabuka.x * size, igra.jabuka.y * size, size, size))
    pygame.display.update()

# ovo je samo za igraca bez nn
def uzmi_ulaze():
    smer = 0
    up = False
    down = False
    right = False
    left = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
    if up and smer != 4:
            smer = 1
    elif down and smer != 1:
            smer = 4
    elif right and smer != 2:
            smer = 3
    elif left and smer != 3:
            smer = 2
    return smer

def igraj_singleplayer():
    global white, red, green, size
    pygame.init()
    gw = pygame.display.set_mode((zmijica.H*size, zmijica.H*size))

    igra = zmijica.Igra()
    igra.nova_igra()
    refresh_display(gw, igra)
    smer = uzmi_ulaze()
    if smer == 0:
        smer = igra.smer
    while igra.pomeri_zmiju(smer):
        pygame.display.update()
        print(igra.smer)
        smer = uzmi_ulaze()
        if smer == 0:
            smer = igra.smer
        refresh_display(gw, igra)
        time.sleep(0.5)
        smer = uzmi_ulaze()
        if smer == 0:
            smer = igra.smer

    print(len(igra.zmija))
