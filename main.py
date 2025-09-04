import turtle
import random

#creating a turtle screen and pen object
wn = turtle.Screen()
t = turtle.Turtle()
t1 = turtle.Turtle()
t.speed(0)

#storing the vaue of the width and height og the screen
width = wn.window_width()
height = wn.window_height()

#setting up custom co-ordinates
wn.setworldcoordinates(0, 0, width, height)

#setting up a space like color as background
wn.bgcolor("#090034")



#creating a variable to monitor state
game_state = "home_screen"
user_name = ""
grid_state = []
solved = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

#UTILITY FUNCTIONS--------------------------------------------------------------------------------------------------------------------------------------->

#This function jumbles the solved grid to make solvable grids-------> 
def generateGrid(n):
    global solved
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
    global grid_state
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
    try:
        difficulty = int(wn.textinput("difficulty level", "Enter difficulty level (1-4): "))
    except:
        difficulty = 4
        
    t.speed(0)
    t.penup()
    t.goto(0, height*(0.75))
    t.pendown()
    t.pencolor("#ffff00")
    t.write(("Hello, "+ user_name + "!!"), align = "center", font = ("Courier", 30, "bold"))
    
    if difficulty == 1:
        grid_state = generateGrid(10)
    elif difficulty == 2:
        grid_state = generateGrid(50)
    elif difficulty == 3:
        grid_state = generateGrid(100)
    elif difficulty == 4:
        grid_state = generateGrid(200)
    else:
        grid_state = generateGrid(100)
    
    drawGrid(grid_state)
    
    t.penup()
    t.goto(-450,900)
    t.pendown()
    t.fillcolor("#ff0000")
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()
    


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
    
    t.penup()
    t.goto(-450,900)
    t.pendown()
    t.fillcolor("#ff0000")
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()


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
    
    t.penup()
    t.goto(-450,900)
    t.pendown()
    t.fillcolor("#ff0000")
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()



#Functions that handle navigation between different screens------------------------------------------------------------------------------------>
def navigate(x,y):
    global game_state
    if game_state == "home_screen":
        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-50,int(height/2)+50):
            game_state = "game_screen"
            t.clear()
            gameScreen()

        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-200,int(height/2)-100):
            game_state = "saved_screen"
            t.clear()
            savedScreen()

        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-350,int(height/2)-250):
            game_state = "lead_screen"
            t.clear()
            leadScreen()
    
    if game_state != "game_state":
        if int(x) in range(-450,-400) and int(y) in range(850,900):
            game_state = "home_screen"
            t.clear()
            home()


def drawGrid(num_list):
    global solved
    print(num_list)
    wn.tracer(0)
    var_width = (width/2)
    var_height = height*(0.75)
    t1.penup()
    t1.goto(var_width, var_height)
    t1.pencolor("#000000")
    t1.pensize(5)
    t1.pendown()
    for i in range(4):

        for j in range(4):

            if num_list[i][j] == 0:
                t1.fillcolor("#000000")
            else:
                t1.fillcolor("#FFF8DE")

            t1.penup()
            t1.goto(var_width, var_height)
            t1.pendown()
            t1.begin_fill()
            for n in range(4):
                t1.forward(120)
                t1.right(90)
            t1.end_fill()
            t1.penup()
            t1.goto(var_width + 60, var_height - 65)
            t1.write(num_list[i][j], align = "center", font = ("Courier", 30, "bold"))
            var_width = var_width + 120

        var_width = (width/2)
        var_height = var_height-120
    wn.update()
    
    if grid_state == solved:
        declareWin()
        
    wn.onclick(playGame)

def playGame(x,y):
    
    global grid_state
    j = int((x - (width/2)) // 120)
    i = int(((height*(0.75)) - y) // 120)
    
    
    
    if 0 <= i < 4 and 0 <= j < 4:
        zero_pos = getElementPos(grid_state, 0)
        zero_i = zero_pos[1]
        zero_j = zero_pos[0]
        
     
        if (abs(i - zero_i) == 1 and j == zero_j) or (abs(j - zero_j) == 1 and i == zero_i):
            grid_state[zero_i][zero_j], grid_state[i][j] = grid_state[i][j], grid_state[zero_i][zero_j]
            t1.clear()
            drawGrid(grid_state)

def declareWin():
    t1.clear()
    t1.goto(width/2, height/2)
    wn.bgpic("image.gif")

            
# leadScreen()
# showGrid(generateGrid(4))

#back button while playing game is not working
#Add leaderboard
#Add saved games using the grid_state variable
#Figure out a way to make the other elements in the game screen to not dissapear.
#add an undo button while playing game.
#add a save game button in the game
#add a quick checkpoint button
#add time counter to count the time taken in solving the game
home()
wn.onclick(navigate)

turtle.done()
wn.mainloop()