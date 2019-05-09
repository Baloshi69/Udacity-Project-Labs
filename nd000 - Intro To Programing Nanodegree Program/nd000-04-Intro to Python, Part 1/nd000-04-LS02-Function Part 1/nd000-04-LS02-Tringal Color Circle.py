import turtle
tur = turtle.Turtle()
# Write a function here that creates a
# turtle and draws a shape with it.
def shape(distance, sides, color, width, quantity):
    tur.color(color)
    tur.width(width)
    for side in range(quantity):
        for side in range(sides):
            tur.forward(distance)
            tur.right(360/sides)
        tur.left(15)

# Call the function multiple times.
shape(80, 3, "blue", 3, 7)
shape(80, 3, "yellow", 3, 7)
shape(80, 3, "red", 3, 7)
