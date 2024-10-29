# Recursion. Homework 3. Task 2.
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=400, animation=True):
    window = turtle.Screen()
    window.bgcolor('black')

    t = turtle.Turtle(visible=False)
    t.color('white')
    t.pencolor('skyblue')
    t.speed('fastest')
    t.penup()
    t.goto(-size / 2, -size / 3)
    t.left(60)
    t.pendown()

    if not animation:
        window.tracer(False)

    t.begin_fill()
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    t.end_fill()

    if not animation:
        window.tracer(True)
    window.mainloop()


def main():
    draw_koch_snowflake(6, animation=False)

if __name__ == '__main__':
    main()