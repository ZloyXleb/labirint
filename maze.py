from pygame import *
mixer.init()
font.init()
font = font.SysFont('Arial', 70)

my_win = display.set_mode((700, 500))
display.set_caption('Лабиринт')

fon = transform.scale(image.load('fon.jpeg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, w, h, speed):
        super().__init__()
        self.speed = speed
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(p_image), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        my_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
    
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'

        if self.rect.x >= 650:
            self.direction = 'left'  

        if self.direction == 'left':
            self.rect.x -= self.speed
        
        else:
            self.rect.x += self.speed

class Wall(GameSprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_w, wall_h):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_w = wall_w
        self.wall_h = wall_h
        self.image = Surface((self.wall_w, self.wall_h))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        my_win.blit(self.image, (self.rect.x, self.rect.y))


st1 = Wall(154, 255, 255, 100, 20, 410, 10)
st2 = Wall(154, 255, 255, 100, 20, 10, 360)
st3 = Wall(154, 255, 255, 180, 95, 10, 360)
st4 = Wall(154, 255, 255, 260, 20, 10, 360)
st5 = Wall(154, 255, 255, 340, 95, 10, 360)
st6 = Wall(154, 255, 255, 420, 20, 10, 360)
st7 = Wall(154, 255, 255, 500, 95, 10, 360)
win = font.render('You win!', True, (100, 255, 100))
lose = font.render('You lose!', True, (255, 100, 100))
mause = Player('hero.png', 0, 50, 45, 45, 7)
cat = Enemy('cyborg.png', 50, 100, 65, 65, 5)
chesse = GameSprite('treasure.png', 600, 400, 65, 65, 0)
finich = False

'''mixer.music.load('jungles.ogg')
mixer.music.play()'''
money = mixer.Sound('money.ogg')
kikk = mixer.Sound('kick.ogg')

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finich != True:
        my_win.blit(fon, (0, 0))
        cat.update()
        mause.update()
        mause.reset()
        st1.draw_wall()
        st2.draw_wall()
        st3.draw_wall()
        st4.draw_wall()
        st5.draw_wall()
        st6.draw_wall()
        st7.draw_wall()
        cat.reset()
        chesse.reset()
        if sprite.collide_rect(mause, chesse):
            finich = True
            money.play()
            my_win.blit(win, (200, 200))
        if sprite.collide_rect(mause, cat) or sprite.collide_rect(mause, st1) or sprite.collide_rect(mause, st2) or sprite.collide_rect(mause, st3) or sprite.collide_rect(mause, st4) or sprite.collide_rect(mause, st5) or sprite.collide_rect(mause, st6) or sprite.collide_rect(mause, st7):
            finich = True
            kikk.play()
            my_win.blit(lose, (200, 200))
        
        


    clock.tick(60)
    display.update()
