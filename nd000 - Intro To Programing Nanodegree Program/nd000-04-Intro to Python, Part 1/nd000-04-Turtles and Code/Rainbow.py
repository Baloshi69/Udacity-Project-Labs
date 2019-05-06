import turtle

rainbow_color = ["red", "orange", "yellow", "green", "blue", "purple"]

# After Learning range() function i used it in line 6. to save all Typing i done in line 7
rang = range(19)
# rainbow_iteration = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19,]

# Write whatever code you want here!
# Import and Variable of RAINBOW
rainbow = turtle.Turtle()
rainbow.width(5)
rainbow.penup()
rainbow.back(160)
rainbow.pendown()
rainbow.left(70)

# Rainbow CODE
for color in rainbow_color:
    for iteration in rang:
        rainbow.right(7)
        rainbow.forward(20)
    rainbow.penup()
    rainbow.right(118)
    rainbow.forward(290)
    rainbow.right(117)
    rainbow.color(color)
    rainbow.pendown()

rainbow.penup()
rainbow.right(153)
rainbow.forward(40)
rainbow.left(90)
rainbow.forward(130)
rainbow.pendown()

for color in rainbow_color:
    for i in [1, 2, 3, 4, 5]:
        rainbow.forward(50)
        rainbow.left(70)
    rainbow.left(153)
    rainbow.color(color)
