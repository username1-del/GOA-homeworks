from turtle import*
width(6)
speed(8)

color("red")
#shape walls
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

left(90)
forward(80) #not door cordinate

#door
begin_fill()
color("brown")
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

penup()
goto(200, 200)
pendown()

#roof
color("orange")
begin_fill()
goto(100, 300)
goto(0, 200)
left(90)
forward(200)
end_fill()

#window cordinate set
penup()
goto(130, 115)
pendown()
#window
begin_fill()
color("yellow")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()
#2nd window cordinate set
penup()
goto(70,115)
pendown()
#2nd window
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()