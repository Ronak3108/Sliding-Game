import turtle
import random
import time
from datetime import datetime
import os
import ast


wn = turtle.Screen()
t = turtle.Turtle()
t1 = turtle.Turtle()
timeTurtle = turtle.Turtle()
t.hideturtle()
t1.hideturtle()
timeTurtle.hideturtle()

t.speed(0)
t1.speed(0)
timeTurtle.speed(0)

width = wn.window_width()
height = wn.window_height()

wn.setworldcoordinates(0, 0, width, height)

wn.bgcolor("#090034")

game_state = "home_screen"

user_name = ""
grid_state = []
solved = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
move_count = 0
start_time = 0
elapsed_time = 0
timestamp = 0
checkpoint_state = None
checkpoint_active = False



#UTILITY FUNCTIONS--------------------------------------------------------------------------------------------------------------------------------------->

#This function jumbles the solved grid to make solvable grids-------> 
def generateGrid(n):
    global solved
    jumbled = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    
    while jumbled == solved:
        for i in range(n):
            valid_moves = giveValidMoves(jumbled)
            selected_move = random.choice(valid_moves)
            x = getElementPos(jumbled, selected_move)[0]
            y = getElementPos(jumbled, selected_move)[1]
            x0 = getElementPos(jumbled, 0)[0]
            y0 = getElementPos(jumbled, 0)[1]
            temp = jumbled[y][x]
            jumbled[y][x] = jumbled[y0][x0]
            jumbled[y0][x0] = temp
    
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



#-----------------------------------------------------------------------------------

def showHeading():
    #writing the heading
    t.penup()
    t.goto(width/2, height*(0.9))
    t.pendown()
    t.pencolor("#ffff00")
    t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))

#FUNCTIONS THAT ARE RELATED TO DIFFERENT GAME SCREENS----------------------------------------------------------------------------------------------------------------->


#function that starts the home screen of the game----------------------->
def home():
    global game_state
    game_state = "home_screen"   #changing the game state to home_screen

    #setting up a space like color as background
    wn.bgcolor("#090034")
    showHeading()

    
    button_names = ["NEW GAME", "LEADERBOARD"]

    t.speed(0)
    t.pencolor("#000000")

    var_height = (height/2)+50
    for i in range(2):
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


#function that starts the game screen of the game----------------------->
def gameScreen():

    global game_state
    game_state = "game_screen"
    
    global start_time
    global move_count
    global elapsed_time
    global timestamp
    move_count = 0
    start_time = 0
    elapsed_time = 0
    
    wn.bgcolor("#090034")
    global grid_state

    global user_name
    user_name = wn.textinput("login", "Enter your name: ")
    if not user_name:
        user_name = "USER"
    
    global difficulty
    difficulty = int(wn.textinput("difficulty level", "Enter difficulty level (1-4): "))

    showHeading()
    drawBackButton()
    var_height = height/2
    
    t.speed(0)
    t.penup()
    t.goto(0, height*(0.75))
    t.pendown()
    t.pencolor("#ff0000")
    t.write(("HELLO "+ user_name.upper() + "!!"), align = "center", font = ("Courier", 40, "bold"))
    
    var_height = (height/2)
    if not checkpoint_active:
        button2_name = "CHECKPOINT"
    else:
        button2_name = "RETURN"

    button_names = ["UNDO", button2_name]

    for i in range(2):
        t.penup()
        t.goto(-200, var_height)
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
        t.goto(0, var_height-67.5)
        t.pencolor("#000000")
        t.pendown()
        t.write(button_names[i], align = "center", font = ("Courier", 30, "bold"))
        var_height = var_height - 150

    
    if difficulty == 1:
        grid_state = generateGrid(10)
    elif difficulty == 2:
        grid_state = generateGrid(30)
    elif difficulty == 3:
        grid_state = generateGrid(80)
    elif difficulty == 4:
        grid_state = generateGrid(150)
    else:
        grid_state = generateGrid(100)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with open(f"{user_name}_{timestamp}.txt", "w") as file:
        file.write(f"{grid_state}\n")


    drawGrid(grid_state)
    game_state = "game_start"
    start_time = time.time()
    wn.ontimer(timer, 100)
    
    

#function that starts the leaderboard screen of the game----------------------->
def leadScreen():
    global game_state
    game_state = "lead_screen"

    wn.bgcolor("#090034")

    showHeading()

    t.penup()
    t.goto(width / 2, height * 0.8)
    t.pendown()
    t.pencolor("#ff0000")
    t.write("LEADERBOARD", align="center", font=("Courier", 40, "bold"))

    drawBackButton()
    loadLeaderboard()
    wn.onclick(playGame)

#function that loads the leaderboard by reading data from the file named "leaderboard.txt"----------------------->
def loadLeaderboard():
    with open("leaderboard.txt", "r") as file:
        lines = file.readlines() #this takes all the lines in the file in this variable named lines

    leaderboard = [] #this list will contain the data to be shown on the leaderboard screen
    for line in lines:
        name, score, timestamp = line.strip().split(",") #it separates the string by commas and stores the substrings on the variables in the order they are written.
        leaderboard.append((name, int(score), timestamp)) #adding the data to leaderboard

    leaderboard.sort(key=lambda x: x[1], reverse=True) #this sorts the list wrt the highest score because 1 is the index of score

    #this displays the leaderboard list on the screen
    var_height = height * 0.5
    t.penup()
    for i, (name, score, timestamp) in enumerate(leaderboard):
        t.goto(width / 2, var_height)
        t.pendown()
        t.pencolor("#FFFFFF")
        t.write(f"{i+1}. {name} - {score} points", align="center", font=("Courier", 25, "bold"))
        var_height -= 40

            

#function that starts the leaderboard screen of the game----------------------->
def replayScreen():
    global game_state, user_name, timestamp
    game_state = "replay_screen" #changing the game_state to replay screen

    wn.bgcolor("#090034")

    showHeading()
    t.penup()
    t.goto(width/2, height*(0.8))
    t.pendown()
    t.pencolor("#ff0000")
    t.write("REPLAY", align = "center", font = ("Courier", 40, "bold"))
    
    drawBackButton()


    filename = f"{user_name}_{timestamp}.txt"
#reading the file in which all the moves we amde are saved.
    with open(filename, "r") as file:
        states = file.readlines()

    for state in states:
        grid = ast.literal_eval(state.strip()) #converting script to python script
        t1.clear()
        drawGrid(grid)
        time.sleep(0.5)

    filename = f"{user_name}_{timestamp}.txt" #deleting the file that stored the game moves are deleted after the replay is watched or if the user chose not to watch it.
    if os.path.exists(filename):
        os.remove(filename)




#Functions that handle navigation between different screens------------------------------------------------------------------------------------>
def navigate(x, y):
    global game_state
    if -200<=int(x)<=-100 and height/2-100<=int(y)<=height/2:
        t.clear()
        t1.clear()
        game_state = "home_screen"
        home()
        wn.onclick(navigate)
        return
    if game_state == "home_screen":
        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-50,int(height/2)+50):
            t.clear()
            gameScreen()
        
        elif int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-200,int(height/2)-100):
            t.clear()
            leadScreen()

            
            
#function that draws the grid everytime a move is made and also in the start of the game----------------------->
def drawGrid(num_list):
    global solved
    wn.tracer(0)
    t.hideturtle()
    t1.hideturtle()
    timeTurtle.hideturtle()
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
    wn.update() # this updates the screen after a time instead of showing us the entire procedure of drawing the grid again.
    
    if grid_state == solved and game_state != "replay_screen": #checking if the user has completed the game or not.
        declareWin()
        
    wn.onclick(playGame) #this function handles the entire click handling except in the homescreen because that is handled by navigate function.

def playGame(x,y):
    global move_count
    move_count = move_count+1
    global grid_state
    global game_state
    global timestamp
    with open(f"{user_name}_{timestamp}.txt", "a") as save_file:
        save_file.write(f"{grid_state}\n") # every move is stored inside this text file in form of grid state
    

    j = int((x - (width/2)) // 120)
    i = int(((height*(0.75)) - y) // 120)
    
    
    
    if 0 <= i < 4 and 0 <= j < 4:
        zero_pos = getElementPos(grid_state, 0)
        zero_i = zero_pos[1]
        zero_j = zero_pos[0]
        
     
        if (abs(i - zero_i) == 1 and j == zero_j) or (abs(j - zero_j) == 1 and i == zero_i):
            grid_state[zero_i][zero_j], grid_state[i][j] = grid_state[i][j], grid_state[zero_i][zero_j]
            t1.clear()
            drawGrid(grid_state) # redraws the grid after every move
        elif game_state == "game_start":
            if int(x) in range(-200, 200) and int(y) in range(int(height/2)-100, int(height/2)):
                undo() # handles the undo functionality
    
    if int(x) in range(-200,-100) and int(y) in range(height-50,height): # handles the back button clicking in every game state
        t.clear()
        t1.clear()
        game_state = "home_screen"
        home()
        filename = f"{user_name}_{timestamp}.txt"
        if os.path.exists(filename):
            os.remove(filename)

        
        wn.onclick(navigate)
    elif game_state == "game_won":
        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-50, int(height/2)+50):
            t.clear()
            t1.clear()
            replayScreen() # calling the replay function

        elif int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-200, int(height/2)-100):
            t.clear()
            t1.clear()
            filename = f"{user_name}_{timestamp}.txt"
            if os.path.exists(filename):
                os.remove(filename)
            home()
            wn.onclick(navigate)
    elif game_state == "game_start":
        if int(x) in range(-200, 200) and int(y) in range(int(height/2)-100, int(height/2)):
            undo()
        elif int(x) in range(-200, 200) and int(y) in range(int(height/2)-250, int(height/2)-150):
            handleCheckpoint() # cslling the checkpoint handling function
            return

            
    


# this function is called when the user has completed the game-------------------->
def declareWin():
    global move_count
    global game_state
    global difficulty
    global user_name
    global timestamp

    # score is given on the basis of difficulty
    if difficulty == 1:
        score = 200
    elif difficulty == 2:
        score = 300
    elif difficulty == 3:
        score = 400
    elif difficulty == 4:
        score = 500
    
    # thwe score is saved in the leaderboard file
    saveScore(user_name, score)
    
    game_state = "game_won" #changing the game state to game_won
    elapsed_time = time.time() - start_time # calcularing total time taken to complete the game
    mins = int(elapsed_time // 60)
    secs = int(elapsed_time % 60)
    t.clear()
    t1.clear()
    t.penup()
    t.goto(width/2, height/2+150)
    t.pendown()
    t.pencolor("yellow")
    t.write(f"CONGRATULATIONS ON FINISHING THE GAME IN {mins:02}:{secs:02},", align = "center", font = ("Courier", 30, "bold"))
    t.penup()
    t.goto(width/2, height/2+100)
    t.pendown()
    t.write(user_name.upper(), align = "center", font = ("Courier", 35, "bold"))
    
    
    button_names = ["REPLAY", "HOME"]

    t.speed(0)
    t.pencolor("#000000")

    var_height = (height/2)+50
    for i in range(2):
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
        
    wn.onclick(navigate)
    
    
    
# this function writes in a text file storing the 
def saveScore(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{score},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    
# draws the back buttonon every screen
def drawBackButton():
    t.penup()
    t.goto(-200, height)
    t.pendown()
    t.fillcolor("#ff0000")
    t.pencolor("#ffffff")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()
    t.penup()
    t.goto(-150, height-37.5)
    t.pendown()
    t.write("BACK", align = "center", font = ("Courier", 15, "bold"))


# this function shows the timer and updates it while the game is being played. It uses a separate turtle to draw it.
def timer():
    global elapsed_time
    global start_time
    global game_state


    if game_state == "game_start":
        elapsed_time = time.time() - start_time
        mins = int(elapsed_time // 60)
        secs = int(elapsed_time % 60)
        timeTurtle.clear()
        timeTurtle.penup()
        timeTurtle.goto(width - 100, height*(0.75) + 25)
        timeTurtle.pendown()
        timeTurtle.pencolor("yellow")
        timeTurtle.write(f"Time: {mins:02}:{secs:02}", align="center", font=("Courier", 20, "bold"))
        wn.update()
        wn.ontimer(timer, 100)
    else:
        timeTurtle.clear()
        wn.update()

#this function handles the undo functionality
def undo():
    global grid_state, user_name, timestamp, move_count

    filename = f"{user_name}_{timestamp}.txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        return


    lines.pop()  #last element of the list is removed using pop to delete the last move from the file


    last_state = lines[-1].strip() # removes the white spaces in the string


    grid_state = ast.literal_eval(last_state)  # string is converted to python script


    with open(filename, "w") as file:
        file.writelines(lines)

    move_count = max(0, move_count - 1)
    t1.clear()
    drawGrid(grid_state)


def handleCheckpoint():
    global checkpoint_state
    global checkpoint_active
    global grid_state

    t.clear()
    showHeading()
    drawBackButton()

    if not checkpoint_active:
        checkpoint_state = [row[:] for row in grid_state]
        checkpoint_active = True
    else:
        if checkpoint_state:
            grid_state = [row[:] for row in checkpoint_state]
            t1.clear()
            drawGrid(grid_state)

    var_height = height/2

    if not checkpoint_active:
        button2_name = "CHECKPOINT"
    else:
        button2_name = "RETURN"
        
        button_names = ["UNDO", button2_name]
    for i in range(2):
        t.penup()
        t.goto(-200, var_height)
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
        t.goto(0, var_height-67.5)
        t.pencolor("#000000")
        t.pendown()
        t.write(button_names[i], align = "center", font = ("Courier", 30, "bold"))
        var_height = var_height - 150

home()
wn.onclick(navigate)

turtle.done()
wn.mainloop()

