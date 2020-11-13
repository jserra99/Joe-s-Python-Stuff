import turtle as trtl

#Create a spider body
spdr = trtl.Turtle()
spdr.pensize(40)
spdr.circle(20)

#Configuring spider legs
legs = 6
leg_len = 70
degree = 380 / legs
spdr.pensize(5)
counter = 0

#Draw Legs
while (counter < legs):
  spdr.goto(0,0)
  spdr.setheading(degree*counter)
  spdr.forward(leg_len)
  counter = counter + 1
spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()
