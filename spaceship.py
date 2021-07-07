from jupylet.sprite import Sprite
from jupylet.label import Label
from jupylet.app import App


app = App()


# The x and y components of the spaceship's velocity.
vx = 0
vy = 0


# The objects.
ship    = Sprite('images/ship1.png', x=app.width/2,  y=app.height/2,  scale=0.5, angle = -45)
stars   = Sprite('images/stars.png', scale=2.5)
alien   = Sprite('images/alien.png', scale=0.5)
moon    = Sprite('images/moon.png',  x=app.width-70, y=app.height-70, scale=0.5)
mars    = Sprite('images/mars.png', x=app.width-70, y=app.height-70, scale=0.1)
jupiter = Sprite('images/jupiter2.png', x=app.width-70, y=app.height-70, scale=0.3)
saturn  = Sprite('images/saturn.png', x=app.width-70, y=app.height-70, scale=0.4)
uranus  = Sprite('images/uranus.png', x=app.width-70, y=app.height-70, scale=0.2)
earth   = Sprite('images/earth.jpg', scale=0.8, x=app.width/2,  y=app.height/2)
wur     = Sprite('images/WUR.jpg', scale=0.3, x=app.width/2, y=app.height/2)
#allofus= Sprite('images/allofus.png', scale=0.15, x=app.height/2, y=app.height/2, angle = -45)
allofus = Sprite('images/allofus2.png', scale=0.15, x=app.height/2, y=app.height/2, angle = -45)

draw_alien = False
draw_stars = False
draw_moon = False
draw_mars = False
draw_jupiter = False
draw_saturn = False
draw_uranus = False
draw_earth = False
draw_campus = False


# The x and y components of the spaceship's velocity.
vx = 0
vy = 0

# Current pressed state of the arrow keys.
up    = False
left  = True
right = True


@app.run_me_every(1/60)
def update_ship(ct, dt):
    global vx, vy

    if left:
        ship.angle += 150 * dt
        
    if right:
        ship.angle -= 120 * dt
        
    if up:
        vx += 3 * math.cos(math.radians(90 + ship.angle))
        vy += 3 * math.sin(math.radians(90 + ship.angle))

    #
    # Update ship position according to its velocity.
    #
    ship.x += vx * dt
    ship.y += vy * dt

    ship.wrap_position(app.width, app.height)
    

@app.run_me_every(1/60)
def rotate(ct, dt):
    
    alien.angle += 64 * dt


@app.event
def mouse_position_event(x, y, dx, dy):
    
    alien.x = x
    alien.y = y
    

@app.event
def render(ct, dt):
    
    app.window.clear()

    if draw_stars:
        stars.draw()
    if draw_earth:
        earth.draw()

    ship.draw()

    if draw_alien:
        alien.draw()
    if draw_moon:
        moon.draw()
    if draw_mars:
        mars.draw()
    if draw_jupiter:
        jupiter.draw()
    if draw_saturn:
        saturn.draw()
    if draw_uranus:
        uranus.draw()
    if draw_campus:
        wur.draw()
        allofus.draw()

        
def set_adventure():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_earth, left, right, up

    left = True
    right = True
    draw_stars = True
    draw_moon = False
    draw_alien = False
    draw_mars = False
    draw_jupiter = False
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45


def set_fromearthtomoon():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = True
    draw_alien = True
    draw_mars = False
    draw_jupiter = False
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45
    moon.x, moon.y = app.width-70, app.height-70


def set_frommoontomars():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = True
    draw_alien = True
    draw_mars = True
    draw_jupiter = False
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45
    moon.x, moon.y = app.width-420, app.height-420
    mars.x, mars.y = app.width-70, app.height-70


def set_frommarstojupiter():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = True
    draw_jupiter = True
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45
    mars.x, mars.y = app.width-430, app.height-430
    jupiter.x, jupiter.y = app.width-70, app.height-70


def set_fromjupitertosaturn():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = True
    draw_saturn = True
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45
    jupiter.x, jupiter.y = app.width-430, app.height-430
    saturn.x, saturn.y = app.width-70, app.height-70


def set_fromsaturntouranus():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = False
    draw_saturn = True
    draw_uranus = True
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, -45
    saturn.x, saturn.y = app.width-390, app.height-390
    uranus.x, uranus.y = app.width-70, app.height-70


def set_fromuranustosaturn():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = False
    draw_saturn = True
    draw_uranus = True
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, 135
    saturn.x, saturn.y = app.width-390, app.height-390
    uranus.x, uranus.y = app.width-70, app.height-70


def set_fromsaturntojupiter():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = True
    draw_saturn = True
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, 135
    saturn.x, saturn.y = app.width-70, app.height-70
    jupiter.x, jupiter.y = app.width-430, app.height-430


def set_fromjupitertomars():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = True
    draw_moon = False
    draw_alien = True
    draw_mars = True
    draw_jupiter = True
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, 135
    jupiter.x, jupiter.y = app.width-70, app.height-70
    mars.x, mars.y = app.width-430, app.height-430


def set_frommarstoearth():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_campus, draw_earth, left, right, up

    left = False
    right = False
    draw_stars = False
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = False
    draw_saturn = False
    draw_uranus = False
    draw_earth = True
    draw_campus = False

    ship.x, ship.y, ship.angle = app.width/2, app.height/2, 135
    mars.x, mars.y = app.width-430, app.height-430
    earth.x, earth.y = app.width/2, app.height/2


def set_oncampus():
    global draw_stars, draw_moon, draw_alien, draw_mars, draw_jupiter, draw_saturn, draw_uranus, draw_earth, draw_campus, left, right, up

    left = False
    right = False
    draw_stars = False
    draw_moon = False
    draw_alien = True
    draw_mars = False
    draw_jupiter = False
    draw_saturn = False
    draw_uranus = False
    draw_earth = False
    draw_campus = True


def check_my_answer_adventure(x, y):
    if x == 'Vredepeel' and 20 <= y <= 22:
        print('Hoera! Your answer is correct! Let us take you on an adventure!')
        set_adventure()
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'Vredepeel'         : print('x is incorrect')
        if y < 20 or y > 22         : print('y is incorrect')
           
        return False


def check_my_answer_fromearthtomoon(x):
    if x == ('a', 'b', 'c'):
        print('Hoera! Your answer is correct! Your alien is taking you to Moon!')
        set_fromearthtomoon
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if 'a' in x                 : print('a is correct')
        if 'b' in x                 : print('b is correct')
        if 'c' in x                 : print('c is correct')
        return False

def check_my_answer_frommoontomars(x, y, z):
    dy = 10
    if x == 'Vredepeel' and 70-dy <= y <= 70+dy and z == ('b','c'):
        print('Hoera! Your answer is correct! You have past the Moon and heading towards Mars!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'Vredepeel'         :      print('x is incorrect')
        if y<70-dy or y>70+dy       :      print('y is incorrect')
        if 'a' in z                 :      print('a is incorrect')
        if 'b' in z                 :      print('b is correct')
        if 'c' in z                 :      print('c is correct')
        return False  

def check_my_answer_frommarstojupiter(x, y, z1, z2):
    if x == 'Vredepeel' and y == 2 and  12<=z1<=16 and 30<=z2<=40:
        print('Hoera! Your answer is correct! You have past Mars and heading towards Jupiter!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'Vredepeel'         :      print('x  is  incorrect')
        if y != 2                   :      print('y  is  incorrect')    
        if z1 < 12 or z1 > 16       :      print('z1 is incorrect')
        if z2 < 30 or z2 > 40       :      print('z2 is incorrect')
        return False 
    
def check_my_answer_fromjupitertosaturn(x, y, z):
    if x == 'decreases' and y == 'night' and z == 'weaker':
        print('Hoera! Your answer is correct! You are on your way to Saturn!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'decreases'         :      print('x is incorrect')
        if y != 'night'             :      print('y is incorrect')
        if z != 'weaker'            :      print('z is incorrect')
        return False 
    
def check_my_answer_fromsaturntouranus(x, y, z, u1, u2):
    if x == 'does not' and y == 'lower' and z == 'inversely proportional' and u1 == 'open up' and u2 == 'lower':
        print('Hoera! Your answer is correct! Bye bye Saturn! Hello Uranus!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'does not'         :    print('x  is incorrect')
        if y  != 'lower'            :    print('y  is incorrect')
        if z  != 'inversely proportional': print('z  is incorrect')
        if u1 != 'open up'          :    print('u1 is incorrect')
        if u2 != 'lower'            :    print('u2 is incorrect')
        return False
    
def check_my_answer_fromuranustosaturn(aerodynamic_res, canopy_res, x, y1, y2, z1, z2):
    if aerodynamic_res == 20 and canopy_res >= 30 and x == 'negligible' and y1 == 'canopy' and y2 == 'radiation' and z1 == 'night' and z2 == 'high':
        print('Hoera! Your answer is correct! You have made a circle around Uranus!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if aerodynamic_res != 20    :    print('aerodynamic_res is incorrect') 
        if canopy_res      != 30    :    print('canopy_res      is incorrect')
        if x  != 'negligible'       :    print('x  is incorrect')
        if y1 != 'canopy'           :    print('y1 is incorrect')
        if y2 != 'radiation'        :    print('y2 is incorrect')
        if z1 != 'night'            :    print('z1 is incorrect')
        if z2 != 'high'             :    print('z2 is incorrect')
        return False
    
def check_my_answer_fromsaturntojupiter(x, y1, y2):
    if x == 'Wekerom' and y1 == 'higher' and y2 == 'lower': 
        print('Hoera! Your answer is correct! You are on your way to Jupiter!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'Wekerom'          :    print('x  is incorrect')
        if y1 != 'higher'           :    print('y1 is incorrect')
        if y2 != 'lower'            :    print('y2 is incorrect')
        return False
    
def check_my_answer_fromjupitertomars(x, y1, y2):
    if x == 'summer' and y1 == 'high' and y2 == 'open':
        print('Hoera! Your answer is correct! You are passing Jupiter again!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'summer'           :    print('x  is incorrect')
        if y1 != 'high'             :    print('y1 is incorrect')
        if y2 != 'open'             :    print('y2 is incorrect')
        return False  
    
def check_my_answer_frommarstoearth(x, y, z1, z2):
    if x == 'higher' and y == 'night' and z1 == 'night' and z2 == 'canopy resistance':
        print('Hoera! Your answer is correct! You are almost back on Earth!')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'higher'           :    print('x  is incorrect')
        if y  != 'night'            :    print('y  is incorrect')
        if z1 != 'night'            :    print('z1 is incorrect')
        if z2 != 'canopy resistance':    print('z2 is incorrect')
        return False 
    
def check_my_answer_oncampus(Wekerom, Vredepeel, Zegveld, x):
    margin = 500
    if  (2111-margin <=Wekerom<= 2111+margin) and (3136-margin <=Vredepeel<= 3136+margin) and (1311-margin <=Zegveld<= 1311+margin) and x == 'comparable':
        print('Hoera! Your answer is correct! Where would you like to go next? Hey, you brought some friends :)')
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if (Wekerom   < 2111-margin or Wekerom   > 2111+margin): print('F_NH3_2018_Wekerom   is incorrect')
        if (Vredepeel < 3136-margin or Vredepeel > 3136+margin): print('F_NH3_2018_Vredepeel is incorrect')
        if (Zegveld   < 1311-margin or Zegveld   > 1311+margin): print('F_NH3_2018_Zegveld   is incorrect')
        if x != 'comparable': print('x is incorrect')
        return False    