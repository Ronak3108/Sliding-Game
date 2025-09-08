import turtle
import random
import time
from datetime import datetime
import os
import ast

#creating a turtle screen and pen object
wn = turtle.Screen()
t = turtle.Turtle()
t1 = turtle.Turtle()
timeTurtle = turtle.Turtle()
t.speed(0)
t1.speed(0)
timeTurtle.speed(0)

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
move_count = 0
start_time = 0
elapsed_time = 0
timestamp = 0
checkpoint_state = None
checkpoint_moves = 0
checkpoint_time = 0
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



#function that draws the game screen and the initial grid-------------------->
def gameScreen():

    global game_state
    game_state = "game_screen"    #changing the game state to game_screen
    
    global start_time
    global move_count
    global elapsed_time
    global timestamp
    move_count = 0
    start_time = 0
    elapsed_time = 0
    
    #setting up a space like color as background
    wn.bgcolor("#090034")
    global grid_state

    global user_name
    user_name = wn.textinput("login", "Enter your name: ")
    if not user_name:
        user_name = "USER"
    
    global difficulty
    try:
        difficulty = int(wn.textinput("difficulty level", "Enter difficulty level (1-4): "))
    except:
        difficulty = 4

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

    try:
        with open(f"{user_name}_{timestamp}.txt", "w") as save_file:
            save_file.write(f"{grid_state}\n")
    except IOError as e:
        print(f"Error saving game: {e}")


    drawGrid(grid_state)
    game_state = "game_start"
    start_time = time.time()
    wn.ontimer(timer, 100)
    
    


def leadScreen():
    global game_state
    game_state = "lead_screen"

    # Setting up a space-like color as background
    wn.bgcolor("#090034")

    showHeading()

    t.penup()
    t.goto(width / 2, height * 0.8)
    t.pendown()
    t.pencolor("#ff0000")
    t.write("LEADERBOARD", align="center", font=("Courier", 40, "bold"))

    # Load leaderboard and display it
    drawBackButton()
    loadLeaderboard()
    wn.onclick(playGame)


def loadLeaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()

        leaderboard = []
        for line in lines:
            name, score, timestamp = line.strip().split(",")
            leaderboard.append((name, int(score), timestamp))

        # Sort the leaderboard by score in descending order
        leaderboard.sort(key=lambda x: x[1], reverse=True)

        # Display the leaderboard
        var_height = height * 0.5
        t.penup()
        for i, (name, score, timestamp) in enumerate(leaderboard[:10]):  # Show top 10 players
            t.goto(width / 2, var_height)
            t.pendown()
            t.pencolor("#FFFFFF")
            t.write(f"{i+1}. {name} - {score} points", align="center", font=("Courier", 25, "bold"))
            var_height -= 40  # Adjust vertical space between names

    except IOError as e:
        print(f"Error reading leaderboard: {e}")

            


def replayScreen():
    global game_state, user_name, timestamp
    game_state = "replay_screen"

    #setting up a space like color as background
    wn.bgcolor("#090034")

    showHeading()

    t.penup()
    t.goto(width/2, height*(0.8))
    t.pendown()
    t.pencolor("#ff0000")
    t.write("REPLAY", align = "center", font = ("Courier", 40, "bold"))
    
    drawBackButton()


    filename = f"{user_name}_{timestamp}.txt"
    try:
        with open(filename, "r") as file:
            states = file.readlines()  # Each line is a string of grid_state

        for state in states:
            grid = ast.literal_eval(state.strip())  # Convert string back to list
            t1.clear()
            drawGrid(grid)
            time.sleep(0.5)  # Delay between steps

    except FileNotFoundError:
        print("Replay file not found!")
    filename = f"{user_name}_{timestamp}.txt"
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

            
            

def drawGrid(num_list):
    global solved
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
    
    if grid_state == solved and game_state != "replay_screen":
        declareWin()
        
    wn.onclick(playGame)

def playGame(x,y):
    global move_count
    move_count = move_count+1
    global grid_state
    global game_state
    global timestamp
    try:
        with open(f"{user_name}_{timestamp}.txt", "a") as save_file:
            save_file.write(f"{grid_state}\n")
    except:
        print("Error saving game")
        
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
        elif game_state == "game_start":
            if int(x) in range(-200, 200) and int(y) in range(int(height/2)-100, int(height/2)):
                undo()
    
    if int(x) in range(-200,-100) and int(y) in range(height-50,height):
        t.clear()
        t1.clear()
        game_state = "home_screen"
        home()
        try:
            filename = f"{user_name}_{timestamp}.txt"
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass
        
        wn.onclick(navigate)
    elif game_state == "game_won":
        if int(x) in range(int(width/2)-200, int(width/2)+200) and int(y) in range(int(height/2)-50, int(height/2)+50):
            t.clear()
            t1.clear()
            replayScreen()

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
            handleCheckpoint()
            return
            
    



def declareWin():
    global move_count
    global game_state
    global difficulty
    global user_name
    global timestamp
    
    difficulty_points = {
        1: 200,
        2: 300,
        3: 400,
        4: 500
    }
    
    score = difficulty_points.get(difficulty, 200) 
    
    saveScore(user_name, score)
    
    game_state = "game_won"
    elapsed_time = time.time() - start_time
    mins = int(elapsed_time // 60)
    secs = int(elapsed_time % 60)
    t.clear()
    t1.clear()
    t.penup()
    t.goto(width/2, height/2+150)
    t.pendown()
    t.pencolor("yellow")
    t.write("CONGRATULATIONS ON FINISHING THE GAME,", align = "center", font = ("Courier", 30, "bold"))
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
    
    
    

def saveScore(player_name, score):
    try:
        with open("leaderboard.txt", "a") as file:
            file.write(f"{player_name},{score},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    except IOError as e:
        print(f"Error saving score: {e}")
    
    
    
    
    
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



def timer():
    global elapsed_time
    global start_time
    global game_state

    try:
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
    except:
        return

def undo():
    global grid_state, user_name, timestamp, move_count

    filename = f"{user_name}_{timestamp}.txt"

    if not os.path.exists(filename):
        print("No moves to undo.")
        return

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("No moves to undo.")
            return


        lines.pop()


        last_state = lines[-1].strip()


        grid_state = ast.literal_eval(last_state)


        with open(filename, "w") as file:
            file.writelines(lines)

        move_count = max(0, move_count - 1)
        t1.clear()
        drawGrid(grid_state)

    except Exception as e:
        print(f"Undo failed: {e}")


def handleCheckpoint():
    global checkpoint_state
    global checkpoint_state
    global checkpoint_moves
    global checkpoint_time
    global checkpoint_active
    global grid_state
    global move_count
    global elapsed_time
    global start_time

    if not checkpoint_active:
        checkpoint_state = [row[:] for row in grid_state]
        checkpoint_moves = move_count
        checkpoint_time = elapsed_time
        checkpoint_active = True
    else:
        if checkpoint_state:
            grid_state = [row[:] for row in checkpoint_state]
            move_count = checkpoint_moves
            start_time = time.time() - checkpoint_time
            t1.clear()
            drawGrid(grid_state)
    t.clear()
    showHeading()
    drawBackButton()
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

