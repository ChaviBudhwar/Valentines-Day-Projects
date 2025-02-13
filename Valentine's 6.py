import turtle
import time

screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Happy Valentine's Day! ❤️")

love = turtle.Turtle()
love.speed(3)
love.color("red")

def draw_heart():
    love.begin_fill()
    love.left(50)
    love.forward(133)
    love.circle(50, 200)
    love.right(140)
    love.circle(50, 200)
    love.forward(133)
    love.end_fill()

def show_message():
    love.penup()
    love.goto(-180, -150)
    love.color("red")
    love.write("Happy Valentine's Day! ❤️", font=("Arial", 16, "bold"))
    love.goto(-150, -180)
    love.write("You're amazing, [His Name]! 💕", font=("Arial", 14, "italic"))

love.penup()
love.goto(0, -100)
love.pendown()
draw_heart()

time.sleep(1)
show_message()

turtle.done()


#Explanation: Line by line
#
#import turtle-->For drawing graphics;  A Python library used for drawing shapes
#import time--> For adding delays
#
#Setting Up the Screen
#screen = turtle.Screen()--> Creates a window for drawing.
#screen.bgcolor("pink")-->Makes the background pink 
#screen.title("Happy Valentine's Day! ❤️")--> Sets the title of the window.
#
#Creating a Turtle for Drawing
#love = turtle.Turtle()--> Creates a turtle named love that will draw the heart.
#love.speed(3)--> Controls how fast the turtle moves
#love.color("red")--> Sets the drawing color to red
#
# Function to Draw the Heart
#def draw_heart():
#    love.begin_fill()--> Start filling the shape with color
#    love.left(50)--> Turn left by 50 degrees
#    love.forward(133)--> Move forward 133 pixels
#    love.circle(50, 200)--> Draw the left curve of the heart
#    love.right(140)--> Turn right by 140 degrees
#    love.circle(50, 200)--> Draw the right curve of the heart
#    love.forward(133)--> Move forward again to complete the heart
#    love.end_fill()--> Fill the heart with red color
#
#Function to Show a Message
#def show_message():
#    love.penup()--> Lift the pen so it doesn't draw lines
#    love.goto(-80, -50)--> Move to position
#    love.color("white")--> Set text color to white
#    love.write("Happy Valentine's Day! ❤️", font=("Arial", 16, "bold"))--> Writes text
#    love.goto(-50, -80)--> Move to another position
#    love.write("You're amazing, [His Name]! 💕", font=("Arial", 14, "italic"))--> Write another text
#
#
#love.penup()
#love.goto(0, -100)--> Move to starting position
#love.pendown()
#draw_heart(): 
#draw_heart()--> Call the function to draw the heart
#
#
#time.sleep(1)--> Wait 1 second before showing the message
#show_message()--> Call the function to display the message
#
#
#turtle.done()--> Keeps the window open