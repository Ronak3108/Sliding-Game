import turtle
import random

#creating a turtle screen and pen object
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

#storing the vaue of the width and height og the screen
width = wn.window_width()
height = wn.window_height()

#setting up custom co-ordinates
wn.setworldcoordinates(0, 0, width, height)

#setting up a space like color as background
wn.bgcolor("#090034")

#writing the heading
t.penup()
t.goto(width/2, height*(0.9))
t.pendown()
t.pencolor("#ffff00")
t.write("SLIDE MASTER", align = "center", font = ("Courier", 80, "bold"))

#creating a variable to monitor state
game_state = "NA"

#function that starts the game
def startGame():

    game_state = "home_screen"   #changing the game state to home_screen
    
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







#function that draws the initial grid
def loadGrid(num_list):

    game_state = "game_screen"

    t.speed(0)
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
            t.forward(120)
            t.right(90)
            t.forward(120)
            t.right(90)
            t.forward(120)
            t.right(90)
            t.forward(120)
            t.right(90)
            t.end_fill()
            t.penup()
            t.goto(var_width + 60, var_height - 60)
            t.write(num_list[i][j], align = "center", font = ("Courier", 20, "bold"))
            var_width = var_width + 120

        var_width = (width/2)
        var_height = var_height-120
        


num_list = [[1,3,4,15],[14,13,7,2],[5,10,6,9],[8,11,12,0]]


def generateNewGame(n):
    solved_grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    for i in range(n):
        move_type = random.choice([1,2,3,4])
        #check if the move is valid or not and convert the move to a state in list of lists form








print(width, height)



# startGame()
# loadGrid(num_list)
generateNewGame(3)

turtle.done()
turtle.mainloop()