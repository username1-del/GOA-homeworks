# 5) Turtle ბიბლიოთეკის დახმარებით დახატეთ ფასანაურული ხინკალი
from turtle import*
shape("turtle")
speed(10)


penup()
goto(20, -200)
pendown()

# khikali body structure
width(5)
color("grey")
begin_fill()
forward(350)
left(130)
forward(200)
right(40)
forward(45)
left(90)
forward(86)
left(90)
forward(45)
right(42)
forward(200)
end_fill()
# 1ნაოჭის კორდინატები
penup()
goto(140, -120)
pendown()
# 1ნაოჭის ხაზი
color("black")
begin_fill()
forward(40)
penup()
goto(170, -150)
pendown()
left(185)
forward(40)
penup()
goto(220, -150)
pendown()
forward(40)
penup()
goto(270, -150)
pendown()
forward(20)


exitonclick()