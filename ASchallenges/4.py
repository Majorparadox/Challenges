import turtle

print("1. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
tess.color("purple")
tess.pensize(5)

def make_square(t, l):
    for i in range(5):
        for i in range(4):
            t.forward(l)
            t.left(90)
        t.penup()
        t.forward(2*l)
        t.pendown()

length = 20
make_square(tess, length)


print("2. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
tess.color("purple")
tess.pensize(5)

increment = 0


def woah_dude(t, l):
    for i in range(5):
        for i in range(4):
            if increment >= 1:

            else:
                t.forward(l)
                t.left(90)


woah_dude(tess, 20)


print("3. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
tess.color("purple")
tess.pensize(5)

def draw_poly(t, n, sz):
    interior = ((n - 2) * 180) / n
    mysides = 180 - interior
    for i in range(n):
        t.forward(sz)
        t.left(mysides)

draw_poly(tess, 8, 50)

print("4. \n")

print("5. \n")

print("6. \n")

print("7. \n")
def sum_to(n):
    num = []
    for i in range(n,0,-1):
        num.append(i)
    total = sum(num)
    return total
print(sum_to(10))

print("8. \n")
def area_of_circle(r):
    pi = 3.1415
    area = pi*(r**2)
    return area

print(area_of_circle(5))

print("9. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
tess.color("purple")
tess.pensize(5)

def star(t,l):
    for i in range(5):
        t.forward(l)
        t.right(144)

star(tess,100)

print("10. \n")
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
tess.color("purple")
tess.pensize(5)

def star(t,l):
    for i in range(5):
        for i in range(5):
            t.forward(l)
            t.right(144)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
star(tess,100)
