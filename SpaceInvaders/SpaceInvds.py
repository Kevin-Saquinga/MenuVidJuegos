import turtle
import random
import math

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()

#Configurar pantalla
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("bgSpaceGame.gif")

#Definir formas visuales del juego
turtle.register_shape("invasor.gip")
turtle.register_shape("spaceCraft.gip")

#Dibujar bordes en la pantalla
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("Black")
borderPen.penup()
borderPen.setposition(-300, -300)

#Puntaje

#Crear jugador (Nave Espacial) 
player = turtle.Turtle()
player.shape("spacecraft.git")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed = 15

#Creacion de enemigos
numEnemies = 10
enemies = []
for i in range(numEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("invasor.git")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
enemySpeed = 4

#Crear laser de jugador
missiles = []
for i in range(3):
    missile = turtle.Turtle()
    missile.color("red")
    missile.shape("circle")
    missile.penup()
    missile.speed(0)
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)
bulletspeed = 30

#Funciones para mover jugador a la derecha e izquierda
def moveRight():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def moveLeft():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#Disparar misiles
def fireMissile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break

#Colison entre enemigos y misiles
def deathEnemy(missile, enemy):
    distance = math.sqrt(math.pow(missile.xcor() - enemy.xcor(), 2)+math.pow(missile.ycor()-enemy.ycor(),2))
    if distance < 30:
        return True
    else:
        return False

#Enlace con teclado
turtle.listen()
turtle.onkey(moveRight, "Right")
turtle.onkey(moveLeft, "Left")
turtle.onkey(fireMissile, "space")

