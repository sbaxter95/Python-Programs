import turtle

def drawSquare(someTurtle):

    for i in range(1,5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("red")
    michelangelo = turtle.Turtle()
    michelangelo.shape ("turtle")
    michelangelo.color ("yellow")
    michelangelo.speed (2)

    for i in range(1,37):
        drawSquare(michelangelo)
        michelangelo.right(10)

    #leonardo = turtle.Turtle()
    #leonardo.shape ("arrow")
    #leonardo.color ("blue")
    #leonardo.circle(100)

    window.exitonclick()

drawArt()
