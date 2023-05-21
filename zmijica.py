import random
import random as rand

def remove_item(arr, item):
    for obj in arr:
        if item == obj:
            arr.remove(obj)
    return



W = 8
H = 8

class tacka:
    def __init__(self, a, b):
        self.x = int(a)
        self.y = int(b)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Igra:
    ostatak = []
    zmija = []
    jabuka = tacka(-1, -1)
    smer = 4
    broj_poteza = 0
    prosli_skor = 2

    def pravi_jabuku(self):
        jab = self.jabuka_seed % len(self.ostatak)
        self.jabuka.x = self.ostatak[jab].x
        self.jabuka.y = self.ostatak[jab].y
        self.ostatak.pop(jab)
        return

    def proveri_glavu(self, x, y):
        global H, W
        if x < 0 or x >= W or y < 0 or y >= H:
            return True
        if tacka(x, y) in self.zmija:
            return True
        return False

    def nova_igra(self):
        global H, W
        self.ostatak = []
        self.zmija = []
        self.jabuka = tacka(-1, -1)
        self.smer = 4
        self.broj_poteza = 0
        self.prosli_skor = 2
        self.uk_broj_poteza = 0
        self.jabuka_seed = 91
        for i in range(H):
            for j in range(W):
                self.ostatak.append(tacka(j,i))

        pomX = 1
        pomY = 1
        self.zmija.append(tacka(pomX, pomY))
        remove_item(self.ostatak, tacka(pomX, pomY))

        pomX = 0
        pomY = 1
        self.zmija.append(tacka(pomX, pomY))
        remove_item(self.ostatak, tacka(pomX, pomY))

        self.pravi_jabuku()
        return

    def kraj_igre(self):
        return False

    def update_tablu(self):
        self.uk_broj_poteza += 1
        global W, H
        noviX = -1
        noviY = -1
        glavaX = self.zmija[0].x
        glavaY = self.zmija[0].y

        if self.smer == 1:
            noviX = glavaX
            noviY = glavaY-1

            if self.proveri_glavu(noviX, noviY):
                return self.kraj_igre()
            else:
                self.zmija.insert(0, tacka(noviX, noviY))
        elif self.smer == 2:
            noviX = glavaX-1
            noviY = glavaY

            if self.proveri_glavu(noviX, noviY):
                return self.kraj_igre()
            else:
                self.zmija.insert(0, tacka(noviX, noviY))
        elif self.smer == 3:
            noviX = glavaX+1
            noviY = glavaY

            if self.proveri_glavu(noviX, noviY):
                return self.kraj_igre()
            else:
                self.zmija.insert(0, tacka(noviX, noviY))
        elif self.smer == 4:
            noviX = glavaX
            noviY = glavaY+1

            if self.proveri_glavu(noviX, noviY):
                return self.kraj_igre()
            else:
                self.zmija.insert(0, tacka(noviX, noviY))

        if noviX == self.jabuka.x and noviY == self.jabuka.y:
            self.pravi_jabuku()
        else:
            remove_item(self.ostatak, tacka(noviX, noviY))
            #ostatak.remove(tacka(noviX, noviY))
            self.ostatak.append(self.zmija[-1])
            self.zmija.pop()
        return True

    def pomeri_zmiju(self, sl_smer):
        if not(sl_smer == self.smer or (sl_smer == 1 and self.smer == 4) or  (sl_smer == 4 and self.smer == 1) or (sl_smer == 2 and self.smer == 3) or (sl_smer == 3 and self.smer == 2)):
            self.smer = sl_smer
            self.broj_poteza += 1
        nastavi = self.update_tablu()
        if len(self.zmija) != self.prosli_skor:
            self.broj_poteza = 0
        return nastavi

    def prebaci_u_niz(self):
        global H, W
        niz = [-1 for i in range(H*W)]
        for t in self.zmija:
            index = t.x + t.y * H
            niz[index] = ((len(self.zmija)-self.zmija.index(t))/len(self.zmija))/10*9
        for t in self.ostatak:
            index = t.x + t.y * H
            niz[index] = 0
        index = self.jabuka.x + self.jabuka.y * H
        niz[index] = 1
        return niz



# pg.init()
# pg.display.set_caption("bannnnn")
# game_window = pg.display.set_mode((wX, wY))
#
# nova_igra()
# override_smer = 0
# while True:
#     time.sleep(1)
#     up = False
#     down = False
#     right = False
#     left = False
#     for event in pg.event.get():
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_UP:
#                 up = True
#             if event.key == pg.K_DOWN:
#                 down = True
#             if event.key == pg.K_LEFT:
#                 left = True
#             if event.key == pg.K_RIGHT:
#                 right = True
#     if up and smer != 4:
#         smer = 1
#     elif down and smer != 1:
#         smer = 4
#     elif right and smer != 2:
#         smer = 3
#     elif left and smer != 3:
#         smer = 2
#     pg.draw.rect(game_window, red, pg.Rect(jabuka.x * 80, jabuka.y * 80, 80, 80))
#
#     for point in zmija:
#         pg.draw.rect(game_window, green, pg.Rect(point.x*80, point.y*80, 80, 80))
#
#     for point in ostatak:
#         pg.draw.rect(game_window, black, pg.Rect(point.x*80, point.y*80, 80, 80))
#
#     pg.display.update()
#     update_tablu()










