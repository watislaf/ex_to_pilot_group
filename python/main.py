import pygame
import os
Main_W = 920
Main_H = 1880
clock = pygame.time.Clock()
window = pygame.display.set_mode((Main_H, Main_W))
howe = 0
objects= [ ]
def finnd(a ,b ,c):
    for obj in objects:
        if type(obj) == type(Rebro(0,0)):
            if (obj.l == a) and (obj.r == b):
                if c == 1:
                    return True
                else:
                    return obj
            if (obj.l == b) and (obj.r == a):
                if c == 1:
                    return True
                else:
                    return obj
    if c==1:
        return False

def set_up(s='Project'):
    pygame.init()
    pygame.display.set_caption(s)


def ColorOf(t):
    if t == 0:
        return (205,0,16)
    if t == 1:
        return (222,222,222)
    if t == 2:
        return (159,138,0)
    if t == 3:
        return (22,22,22)
    if t == 4:
        return (1,241,40)
def run():
    done = True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    return done

def bett(a=(0,0), b=(0,0)):
    tem= [0,0]
    xl = a[0]
    xr = b[0]
    yl = a[1]
    yr = b[1]
    if (xl < xr):
        tem[0] = 4
    if (xl > xr):
        tem[0] = -4
    if (yl < yr):
        tem[1] = 4
    if (yl > yr):
        tem[1] = -4
    return tem

class Round:
    def __init__(self,pos_x = 0,pos_y = 0,color = (0,0,0),radius = 19,width =7,name="None",surname="None",id=0 ):
        self.pos_x = pos_x
        self.id=id
        self.pos_y = pos_y
        self.color=color
        self.radius=radius
        self.width=width
        self.name=name
        self.surname=surname
    def move(self,MoveForX,MoveForY):
        self.pos_x = self.pos_x + MoveForX
        self.pos_y = self.pos_y + MoveForY
    def __lt__(self, other):
        return self.radius>other.radius
    def touch(self,x= 0,y=0):
        return ((x - self.pos_x)*(x - self.pos_x) + (y - self.pos_y)*(y - self.pos_y) <= self.radius*self.radius)
    def paint(self,sur):
        for obj in objects:

            if type(obj)==type(Round()) and obj != self:
                dl=(self.pos_x, self.pos_y)
                dr=(obj.pos_x, obj.pos_y)
                if (self.pos_x - obj.pos_x) * (self.pos_x - obj.pos_x) + (self.pos_y - obj.pos_y) * (self.pos_y - obj.pos_y) < 10000:
                    self.move(-bett(dl,dr)[0], -bett(dl,dr)[1])
        pygame.draw.circle(sur, (self.color), (int(self.pos_x), int(self.pos_y)),self.radius,self.width)
        pygame.draw.circle(sur, (ColorOf(3)), (int(self.pos_x), int(self.pos_y)), self.radius,  4)


class Rebro :
    def __init__(self,l,r,color = (0,0,0) ):
        self.l=l
        self.r=r
        self.color=color

    def paint(self,sur):
        dl = (self.l.pos_x, self.l.pos_y)
        dr = (self.r.pos_x, self.r.pos_y)
        if (self.l.pos_x-self.r.pos_x)*(self.l.pos_x-self.r.pos_x)+(self.l.pos_y-self.r.pos_y)*(self.l.pos_y-self.r.pos_y) >20000:
            for obj in objects:
                if obj == self.l:
                    obj.move(bett(dl,dr)[0],bett(dl,dr)[1])
                if obj ==self.r:
                    obj.move(bett(dr,dl)[0], bett(dr,dl)[1])
        if (self.l.pos_x-self.r.pos_x)*(self.l.pos_x-self.r.pos_x)+(self.l.pos_y-self.r.pos_y)*(self.l.pos_y-self.r.pos_y) <10000:
            for obj in objects:
                if obj == self.l:
                    obj.move(-bett(dl, dr)[0],- bett(dl, dr)[1])
                if obj ==self.r:
                    obj.move(-bett(dr, dl)[0],- bett(dr, dl)[1])

        pygame.draw.line(sur, ColorOf(1),(self.l.pos_x,self.l.pos_y),(self.r.pos_x,self.r.pos_y), 3)

def hapen(objects):
    mouse_poz = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    for obj in reversed(objects):
        if pygame.mouse.get_pressed()[0]:
            if(type(obj)==type(Round()) and obj.touch(mouse_poz[0],mouse_poz[1])):
                poz = pygame.mouse.get_rel()
                pygame.mouse.get_rel()
                obj.move(poz[0],poz[1])
                break

    pygame.mouse.get_rel()

def display(World, col=(0, 0, 0), h=20):
    keys = pygame.key.get_pressed()
    Fl = True
    if keys[pygame.K_1]:
        Fl = Fl ^ 1
    if Fl :
        window.fill(col)
        for obj in World:
            obj.paint(window)

        pygame.display.update()
        pygame.time.delay(h)

set_up("3D")
answer=True
lr= [Round(id=-1),Round(id=-1)]
siz= 0
cl = (155, 100, 100)
while run():
    hapen(objects)

    doit=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        objects= []
        howe=0
        fl = False
        siz = 0
        lr = [Round(id=-1), Round(id=-1)]
    if keys[pygame.K_2]:
        if answer==True:
            answer=False
            doit=True
    if keys[pygame.K_3]:
        if answer==False:
            answer=True
            doit=True
    mouse_poz = pygame.mouse.get_pos()
    fl = False
    if pygame.mouse.get_pressed()[1]:
        fl = True
        for obj in objects:
            if type(obj)==type(Round()) and obj.touch(mouse_poz[0], mouse_poz[1]):
                if(lr[0].id==-1):
                    lr[0]=obj
                if (lr[0].id != obj.id):
                    lr[1] = obj
                fl=False
    if fl:
        lr = [Round(id=-1), Round(id=-1)]
    if(lr[1].id!=-1):
        if finnd(lr[1],lr[0],1):
            objects.remove(finnd(lr[1],lr[0],2))
        else:
            objects.append(Rebro(lr[0],lr[1]))
        lr = [Round(id=-1), Round(id=-1)]
    if pygame.mouse.get_pressed()[2]:
        fl = True
        for obj in objects:
            if type(obj)==type(Round()) and obj.touch(mouse_poz[0], mouse_poz[1]):
                fl = False

        if fl:
            objects.append(Round(mouse_poz[0], mouse_poz[1], ColorOf(1), 22, 0, "N", "N", howe))
            howe = howe + 1

    if( siz != len(objects) or doit ==True):
        siz=len(objects)
        sf = open("input.txt","w")
        reber = 0
        vers = 0
        for obj in objects:
            if type(obj) == type(Round(0,0)):
                vers+=1
            if type(obj) == type(Rebro(0,0)):
                reber+=1
        param3 = 2
        if answer == True:
            param3 = 3

        sf.write(str(vers)+" "+str(reber)+" "+str(param3)+"\n")
        for obj in objects:
            if type(obj) == type(Rebro(0, 0)):
                sf.write(str(obj.l.id+1)+" "+str(obj.r.id+1)+"\n")
        sf.close()
        os.system("Project1.exe")
        sf= open("output.txt")
        strin = sf.read()

        ver = 1
        if strin =="NO":
            cl = (155, 100, 100)
            for obj in objects:
                if type(obj) == type(Rebro(0, 0)) :
                    obj.color = (200, 200, 100)
        else:
            colorss = strin.split(" ")

            if colorss[0]=="OK":
                cl = (155, 155, 155)
            else:
                cl = (155, 110, 155)
            print(open("output2.txt").read() )
            while ver < len(colorss):
                for obj in objects:
                    if type(obj) == type(Round()) and (obj.id+1) == ver:
                        if colorss[ver ]=="1":
                            obj.color = (10,10,10)
                        else:
                            obj.color = (200, 200, 200)
                ver += 1

    display(objects,cl,0)