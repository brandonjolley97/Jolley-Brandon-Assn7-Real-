import turtle

circle1 = turtle.Turtle()
circle2 = turtle.Turtle()

circle1.speed(15)
circle2.speed(15)

circle1X, circle1Y, circle1Radius = eval(input("Please enter circle1's center x-, and y-coordinates, and radius: "))
circle2X, circle2Y, circle2Radius = eval(input("Please enter circle2's center x-, and y-coordinates, and radius: "))

circle1Center = circle1Y - circle1Radius
circle2Center = circle2Y - circle2Radius


circle1.penup()
circle1.goto(circle1X,circle1Center)
circle1.pendown()
circle1.circle(circle1Radius)
circle2.penup()
circle2.goto(circle2X,circle2Center)
circle2.pendown()
circle2.circle(circle2Radius)

distanceBetweenCenters = (((max(circle1X, circle2X) - min(circle1X, circle2X)) * (max(circle1X, circle2X) - min(circle1X, circle2X))) +
                          ((max(circle1Y, circle2Y) - min(circle1Y, circle2Y)) * (max(circle1Y, circle2Y) - min(circle1Y, circle2Y)))) ** 0.5

if distanceBetweenCenters > circle1Radius + circle2Radius:
    print("The circles do not overlap")
elif distanceBetweenCenters <= circle1Radius + circle2Radius:
    if max(circle1Radius, circle2Radius) - min(circle1Radius, circle2Radius) >= distanceBetweenCenters:
        if max(circle1Radius,circle2Radius) == circle1Radius:
            print("Circle 2 is inside circle 1.")
        elif max(circle1Radius,circle2Radius) == circle2Radius:
            print("Circle 1 is inside circle 2.")
        else:
            print("You broke me!  How'd that happen?")
    else:
        print("The circles overlap.")
else:
    print("You broke me!  How'd that happen?")

print(distanceBetweenCenters)


turtle.done()