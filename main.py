import turtle
import random

#creating a turtle screen and pen object
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

#storing the vaue of the width and height og the screen
width = wn.window_width()
height = wn.window_height()
print(width, height)

#setting up custom co-ordinates
wn.setworldcoordinates(0, 0, width, height)

#setting up a space like color as background
wn.bgcolor("#090034")



#creating a variable to monitor state
game_state = "home_screen"
user_name = ""

#UTILITY FUNCTIONS--------------------------------------------------------------------------------------------------------------------------------------->

#This function jumbles the solved grid to make solvable grids-------> 
def generateGrid(n):
    solved = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    jumbled = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    
    while jumbled == solved:
        for i in range(n):
            valid_moves = giveValidMoves(jumbled)
            selected_move = random.choice(valid_moves)
            move_posX = getElementPos(jumbled, selected_move)[0]
            move_posY = getElementPos(jumbled, selected_move)[1]
            zero_posX = getElementPos(jumbled, 0)[0]
            zero_posY = getElementPos(jumbled, 0)[1]
            temp = jumbled[move_posY][move_posX]
            jumbled[move_posY][move_posX] = jumbled[zero_posY][zero_posX]
            jumbled[zero_posY][zero_posX] = temp
    
    return jumbled

#This function gives the position of any element in the 2d list-------> 
def getElementPos(num_list, element):
    for i in num_list:
        for j in i:
            if j == element:
                pos_x = i.index(j)
                pos_y = num_list.index(i)
                return [pos_x, pos_y]
                
#This function gives the list of all the valid moves that can be done in any state-------> 
def giveValidMoves(num_list):
    x = getElementPos(num_list,0)[0]
    y = getElementPos(num_list,0)[1]
    valid_moves = []
    
    try:
        valid_moves.append(num_list[y+1][x])
    except:
        pass
    try:
        valid_moves.append(num_list[y-1][x])
    except:
        pass
    try:
        valid_moves.append(num_list[y][x+1])
    except:
        pass
    try:
        valid_moves.append(num_list[y][x-1])
    except:
        pass

    return valid_moves











#FUNCTIONS THAT ARE RELATED TO DIFFERENT GAME SCREENS----------------------------------------------------------------------------------------------------------------->


#function that starts the home screen of the game----------------------->
def home():
    global game_state
    game_state = "home_screen"   #changing the game state to home_screen

    #setting up a space like color as background
    wn.bgcolor("#090034")

    #writing the heading
    t.penup()
    t.goto(width/2, height*(0.9))
    t.pendown()
    t.pencolor("#ffff00")
    t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))
    
    button_names = ["NEW GAME", "SAVED GAMES", "LEADERBOARD"]

    t.speed(0)
    t.pencolor("#000000")

    var_height = (height/2)+50
    for i in range(3):
        t.penup()
        t.goto((width/2)-200, var_height)
        t.pendown()
        t.fillcolor("#FFF8DE")
        t.begin_fill()
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()
        t.begin_fill()
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()
        t.penup()
        t.goto(width/2, var_height-67.5)
        t.pendown()
        t.write(button_names[i], align = "center", font = ("Courier", 30, "bold"))
        var_height = var_height - 150



#function that draws the game screen and the initial grid-------------------->
def gameScreen():

    #setting up a space like color as background
    wn.bgcolor("#090034")

    #writing the heading
    t.penup()
    t.goto(width/2, height*(0.9))
    t.pendown()
    t.pencolor("#ffff00")
    t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))

    global user_name
    user_name = wn.textinput("login", "Enter your name: ")
    if not user_name:
        user_name = "User"
    global game_state
    game_state = "game_screen"    #changing the game state to game_screen
    
    global difficulty
    difficulty = int(wn.textinput("difficulty level", "Enter difficulty level (1-4): "))
    
    t.speed(0)
    t.penup()
    t.goto(0, height*(0.75))
    t.pendown()
    t.pencolor("#ffff00")
    t.write(("Hello, "+ user_name + "!!"), align = "center", font = ("Courier", 30, "bold"))
    
    if difficulty == 1:
        drawGrid(generateGrid(10))
    elif difficulty == 2:
        drawGrid(generateGrid(30))
    elif difficulty == 3:
        drawGrid(generateGrid(60))
    elif difficulty == 4:
        drawGrid(generateGrid(100))
    else:
        drawGrid(generateGrid(200))


def leadScreen():

    game_state = "lead_screen"

    #setting up a space like color as background
    wn.bgcolor("#090034")

    #writing the heading
    t.penup()
    t.goto(width/2, height*(0.9))
    t.pendown()
    t.pencolor("#ffff00")
    t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))

    t.penup()
    t.goto(width/2, height*(0.8))
    t.pendown()
    t.pencolor("#ff0000")
    t.write("LEADERBOARD", align = "center", font = ("Courier", 40, "bold"))

def savedScreen():

    game_state = "saved_screen"

    #setting up a space like color as background
    wn.bgcolor("#090034")

    #writing the heading
    t.penup()
    t.goto(width/2, height*(0.9))
    t.pendown()
    t.pencolor("#ffff00")
    t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))

    t.penup()
    t.goto(width/2, height*(0.8))
    t.pendown()
    t.pencolor("#ff0000")
    t.write("SAVED GAMES", align = "center", font = ("Courier", 40, "bold"))



#Functions that handle navigation between different screens------------------------------------------------------------------------------------>
def navigate(x,y):
     global game_state
     if game_state == "home_screen":
         if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-50,int(height/2)+50):
             game_state = "game_screen"
             wn.clearscreen()
             gameScreen()

         if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-200,int(height/2)-100):
             game_state = "saved_screen"
             wn.clearscreen()
             savedScreen()

         if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-350,int(height/2)-250):
             game_state = "lead_screen"
             wn.clearscreen()
             leadScreen()


def drawGrid(num_list):
    var_width = (width/2)
    var_height = height*(0.75)
    t.penup()
    t.goto(var_width, var_height)
    t.pencolor("#000000")
    t.pensize(5)
    t.pendown()
    for i in range(4):

        for j in range(4):

            if num_list[i][j] == 0:
                t.fillcolor("#000000")
            else:
                t.fillcolor("#FFF8DE")

            t.penup()
            t.goto(var_width, var_height)
            t.pendown()
            t.begin_fill()
            for n in range(4):
                t.forward(120)
                t.right(90)
            t.end_fill()
            t.penup()
            t.goto(var_width + 60, var_height - 65)
            t.write(num_list[i][j], align = "center", font = ("Courier", 30, "bold"))
            var_width = var_width + 120

        var_width = (width/2)
        var_height = var_height-120











            
# leadScreen()
# showGrid(generateGrid(4))
home()
wn.onclick(navigate)

turtle.done()


wn.mainloop()