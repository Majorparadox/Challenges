import turtle

print("1. \n")
like = ("I like turtle \n")
print(like*1000)

print("2. \n")

print("3. \n")
Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in Month:
    print("One of the month's of the year is:", i)

# Unrelated looping question. Is there any way to return a certain part of a list based on user input?

print("4. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
#tess.left(3645)
print("Tess goes in circles clockwise 10 times and stops at 45 degrees from north")

print("5. \n")
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#a.
for i in xs:
    print(i)
#b.
for i in xs:
    print(i, i*i)
#c.
total = 0
for i in xs:
    total += i
print(total)
#d.
product = 1
for i in xs:
    product = product*i
print(product)


print("6. \n")
tess = turtle.Turtle()
wn = turtle.Screen()

#a.
for i in range(3):
    tess.forward(50)
    tess.right(240)

#b.
for i in range(4):
    tess.forward(50)
    tess.right(90)
#c.
for i in range(6):
    tess.forward(50)
    tess.right(60)
#d.
for i in range(8):
    tess.forward(50)
    tess.right(45)
turtle.done()

print("7. \n")
alex = turtle.Turtle()
wn = turtle.Screen()
pirate = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in pirate:
    alex.forward(100)
    alex.left(i)

print("8. \n")

print("9. \n")
#20 degrees

print("10. \n")
#Done, deleted code for brevity

print("11. \n")
bob = turtle.Turtle()
wn = turtle.Screen()
for i in range(5):
    bob.forward(300)
    bob.right(144)

print("12. \n")
import turtle

jeff = turtle.Turtle()
wn = turtle.Screen()
jeff.shape("turtle")
jeff.color("blue")
jeff.stamp()
turtle.bgcolor("green")
angle = 30
for i in range (12):
    jeff.penup()
    jeff.forward(60)
    jeff.pendown()
    jeff.forward(30)
    jeff.penup()
    jeff.forward(20)
    jeff.stamp()
    jeff.home()
    jeff.right(angle)
    angle = angle+30

print("13. \n")
#The type is turtle.Turtle

print("14. \n")
#A bale of turtles

print("15. \n")
#A slither of pythons. Not a viper, non venomous

