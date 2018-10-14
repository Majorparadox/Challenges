print("1. \n")
Dictionary = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}
Day = int(input("What day is it in number form (Saturday = 0, Sunday = 6): "))
Currentday = Dictionary.get(Day)
print(Currentday)

print("2. \n")
Leave = int(input("What day are you leaving(0-6): "))
Length = int(input("How many days will you be gone: "))

Modulus = Length % 7

print(Modulus)

ComebackNum = Leave + Modulus
print(ComebackNum)
if ComebackNum > 6:
    ComebackNum = ComebackNum-7
Comeback = Dictionary.get(ComebackNum)
print(Comeback)

print("3. \n")
a <= b a < b a < 18 and day != 3 not (3 >= 4)

#4 3 == 3 True 3 != 3 False 3 >= 4 True not (3 < 4) False

#5 True True True True True True False True

print("6. \n")

GradeBoundary = {75-100:"First", 70-75:"Upper Second", 60-70:"Second", 50-60:"Third", 45-50:"F1 Supp", 40-45:"F2", 0-40:"F3"}

E = int(input("Please enter the mark out of 100"))

def Grades(n): print(GradeBoundary[n]) Grades(E)

print("6,8,9. \n")
import turtle def draw_bar(t, height): t.begin_fill() t.left(90) t.forward(height) if height < 0: t.penup() t.forward(-15) t.write(" "+ str(height)) t.forward(15) t.pendown() else: t.write(" "+ str(height)) t.right(90) t.forward(40) t.right(90) t.forward(height) t.left(90) t.end_fill() t.penup() t.forward(10) t.pendown()

wn = turtle.Screen() wn.bgcolor("lightgreen")

tess = turtle.Turtle() tess.color("blue", "red") tess.pensize(3)

xs = [-50,48,117,200,240,160,260,220]

for a in xs: if a>200: tess.color("blue", "red") elif a >= 100: tess.color("blue", "yellow") else: tess.color("blue", "green") draw_bar(tess, a)

wn.mainloop()

print("10. \n") import math

L1 = float(input("Please enter the length of one side of the triangle: ")) L2 = float(input("Please enter the length of the other side of the triangle: "))

def findhypo(a,b): Hypo = L12 + L22 Hypo2 = math.sqrt(Hypo) return (Hypo2) print(findhypo(L1,L2))

print("11. \n") import math

L1 = float(input("Please enter the length of one side of the triangle: ")) L2 = float(input("Please enter the length of the other side of the triangle: ")) L3 = float(input("Please enter the length of the other side of the triangle: "))

def isrightangle(a,b,c): Hypo = L12 + L22 Hypo = math.sqrt(Hypo) if L3 == Hypo: print(True) else: print(False)

print(isrightangle(L1,L2,L3))

print("12. \n")
import math
L = float(input("Please enter the length of one side of the triangle: ")) L = float(input("Please enter the length of the other side of the triangle: ")) L = float(input("Please enter the length of the other side of the triangle: "))

def isrightangle(a,b,c): Hypo = L2 + L2 Hypo = math.sqrt(Hypo) if L == Hypo: print(True) else: print(False)

print(isrightangle(L,L,L))

print("13. \n")
import math a = math.sqrt(2.0) print(a, aa) print(aa == 2.0)
