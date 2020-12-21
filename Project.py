#Space Invader Game

from random import randint
from math import sqrt
import turtle

#Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("Space Invader Background.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300 , -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle() 

#Set the score to ZERO
score = 0

#Drawing the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition((-280) , 270)
scorestring = "Your Score : {}".format(score)
score_pen.write(scorestring , False , align = "left" , font = ("Times New Roman" , 20 , "normal" ))
score_pen.hideturtle()

#Fetching the highest score
try :
    file = open("Space Invader.b")
    high_score = file.readline()
except FileNotFoundError :
    high_score = 0

#Printing the Highest Score
high_pen = turtle.Turtle()
high_pen.speed(0)
high_pen.color("White")
high_pen.penup()
high_pen.setposition(280 , 270)
hscore = "Highest Score : {}".format(high_score) 
high_pen.write(hscore , False , align = "right" , font = ("Times New Roman" , 20 , "normal"))
 
#Create the player turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.shapesize(1 , 1)
player.penup()
player.speed(0)
player.setposition(0 , -250)
player.setheading(90)
playerspeed = 15

#Choose a number of enemies
number_of_enemies = 10

#Creating an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies) :

    #Create the enemy
    enemies.append(turtle.Turtle())
    
for enemy in enemies :
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = randint((-200) , 200)
    y = randint(100 , 250)
    enemy.setposition(x , y)
enemyspeed = 10

#Create the player's projectile
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5 , 0.5)
bullet.hideturtle()
bulletspeed = 20

#Defining bulletstate
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player left and right
def move_left() :
    x = player.xcor()
    x -= playerspeed
    if x < (-280) :
        x = (-280)
    player.setx(x)
move_left()

def move_right() :
    x = player.xcor()
    x += playerspeed
    if x >280 :
        x = 280
    player.setx(x)
move_right()

#Move the player forward and backward
def move_forward() :
    y = player.ycor()
    y += playerspeed
    if y > 0 :
        y = 0
    player.sety(y)
move_forward()

def move_backward() :
    y = player.ycor()
    y -= playerspeed
    if y < (-250) :
        y = (-250)
    player.sety(y)
move_backward()

def Collision(t1 , t2) :
    dist = sqrt(pow((t1.xcor() - t2.xcor()) , 2) + pow((t1.ycor() - t2.ycor()) , 2))
    if dist < 15 :
        return True
    else :
        return False

def fire_bullet() :
    #Declaring bulletstate as global if it needs to be changed
    global bulletstate
    if bulletstate == "ready" :
        bulletstate = "fire"
    
        #Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 25
        bullet.setposition(x , y)
        bullet.showturtle()        
        
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left , "Left")
turtle.onkey(move_right , "Right")
turtle.onkey(fire_bullet , "space")
turtle.onkey(move_forward , "Up")
turtle.onkey(move_backward , "Down")

#Main Game Loop
while True:
    
    for enemy in enemies :        
        
        #Move the enemy
        x = enemy.xcor()    
        x += enemyspeed
        enemy.setx(x)    
    
        #Move the enemy to and fro
        if enemy.xcor() > 280 :            
            
            #Move all enemies down
            for e in enemies :
                y = e.ycor()
                y -= 40
                e.sety(y)                
                
            #Changes the enemy direction
            enemyspeed *= (-1)
             
        if enemy.xcor() < (-280) :            
            
            #Move all enemies down
            for e in enemies :
                y = e.ycor()
                y -= 40
                e.sety(y)                
                
            #Changes the enemy direction
            enemyspeed *= (-1)        
        
        #Check if there is a collision between the bullet and enemy
        if Collision(bullet , enemy) :            
            
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0 , (-400))            
            
            #Reset the enemy
            x = randint((-200) , 200)
            y = randint(100 , 250)
            enemy.setposition(x , y)            
            
            #Update the score
            score += 10
            scorestring = "Your Score : {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring , False , align = "left" , font = ("Times New Roman" , 20 , "normal" ))            
            
        #Check if there is a collision between the player and enemy
        if Collision(player , enemy) :
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()            
            
            #Printing Your Score
            score_pen = turtle.Turtle()
            score_pen.speed(0)
            score_pen.color("white")
            score_pen.penup()
            score_pen.setposition(0 , 50)
            scorestring = "Your Score : {}".format(score)
            score_pen.write(scorestring , False , align = "center" , font = ("Times New Roman" , 50 , "normal" ))            
            
            #Saving the Score
            file = open("Space Invader.b" , mode = 'w')
            file.write('{}'.format(score))
            
            #Printing Game Over
            end_pen = turtle.Turtle()
            end_pen.speed(0)
            end_pen.color("white")
            end_pen.penup()
            end_pen.setposition(0 , (-50))
            endstring = "Game Over"
            end_pen.write(endstring , False , align = "center" , font = ("Times New Roman" , 50 , "normal"))
            break        
        
        #Check if the enemy has gone down the border
        if enemy.ycor() < (-280) :
            for e in enemies :
                e.hideturtle()                
                
                #Printing Your Score
                score_pen = turtle.Turtle()
                score_pen.speed(0)
                score_pen.color("white")
                score_pen.penup()
                score_pen.setposition(0 , 50)
                scorestring = "Your Score : {}".format(score)
                score_pen.write(scorestring , False , align = "center" , font = ("Times New Roman" , 50 , "normal" ))                
                
                #Printing Game Over
                end_pen = turtle.Turtle()
                end_pen.speed(0)
                end_pen.color("white")
                end_pen.penup()
                end_pen.setposition(0 , 0)
                endstring = "Game Over"
                end_pen.write(endstring , False , align = "center" , font = ("Times New Roman" , 50 , "normal"))
                break    
    
    #Move the bullet
    if bulletstate == "fire" :
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)    
    
    #Checking whether the bullet has gone to the top
    if bullet.ycor() > 275 :
        bullet.hideturtle()
        bulletstate = "ready"