############################################
# Name: Jonathan Ge                        #
# Course: ICS3UI                           #
# Assignment: Array Animation Assignment   #
# Title: No, I am your father              #
# Description: A recreation of the fight   #
# between Luke Skywalker and Darth Vader   #
# from Star Wars.                          #
# Note: There may be some minor            #
# discrepancies between this animation and #
# scene from the movie.                    #
############################################

from tkinter import *

from time import *

from math import *

from random import *

root = Tk()

s = Canvas(root, width=1200, height=800, background="white")

s.pack()

#importing images

image = PhotoImage(file = "luke.gif")

image2 = PhotoImage(file = "vader.gif")

image3 = PhotoImage(file = "armlessluke.gif")

luke = image.subsample(4,4)

vader = image2.subsample(4,4)

luke_no_arm = image3.subsample(4,4)

#defining s.create functions as single variables for easier and neater code

p = s.create_polygon

r = s.create_rectangle

l = s.create_line

o = s.create_oval

t = s.create_text

a = s.create_arc

im = s.create_image

############################################
#                                          #
#                                          #
#               Background                 # 
#                                          #
############################################

#gradient background loop

grey = []

for i in range(27):

    grey.append("grey"+str(i+2))

space = 30

x = 0

x2 = x + 1200

y = 0

y2 = y + space

for colour in grey:

    r(x,y,x2,y2,fill = colour,outline = colour)

    y = y + space

    y2 = y2 + space

for n in range(500):

    x = randint(0,1200)

    y = randint(0,26)

    r(x,(y*30),x+5,(y*30+5),fill = "yellow")

#Bridge and Antennas

r(0,575,425,650,fill = "#9e9e9d")

p(425,575,650,575,650,650,600,675,475,675,425,650,fill = "#9e9e9d")

r(475,675,600,805,fill = "#6F767D")

p(650,575,750,575,800,550,800,600,650,600,fill = "#9e9e9d")

a(800,625,850,675,start = 180,extent = 180,fill = "#9e9e9d")

r(812.5,575,850,300,fill = "#6F767D")

a(812.5,281.75,850,318.75,start = 0,extent = 180,fill = "#6F767D")

r(800,650,850,550,fill = "#9e9e9d")

r(800,550,825,375,fill = "#9e9e9d")

a(800,362.5,825,387.5,start = 0,extent = 180,fill = "#9e9e9d",outline = "#9e9e9d")

r(750,625,900,633,fill = "#9e9e9d")

l(825,675,825,805,fill = "#9e9e9d",width = 5)

r(850,425,925,450,fill = "#5A5E61")

r(850,525,925,550,fill = "#5A5E61")

r(925,550,975,275,fill = "grey50")

r(937.5,550,962.5,600,fill = "grey43")

p(937.5,600,925,650,975,650,962.5,600,fill = "grey50")

a(925,250,975,300,start = 0,extent = 180,fill = "grey50",outline = "grey50")

r(925,650,975,668,fill = "grey40")

r(655,475,667.5,650,fill = "grey50")

#Shading and Shadows

#Shading for Horizontal Section

shading1 = []

for i in range(50):

    shading1.append("grey"+str(i+12))

space2 = 1

x = 0

x2 = x + 425

y = 650

y2 = y + space2

for color in shading1:

    r(x,y,x2,y2,fill = color,outline = color)

    y = y - space2

    y2 = y2 - space2

#Shading for Column

shading2 = []

for i in range(25):

    shading2.append("grey"+str(i+20))

space3 = 5

x = 475

x2 = x + space3

y = 675

y2 = y + 125

for color2 in shading2:

    r(x,y,x2,y2,fill = color2,outline = color2)

    x = x + space3

    x2 = x2 + space3

#Shading for Middle Section

shading3 = []

for i in range(25):

    shading3.append("grey"+str(i+35))

space4 = 9

x = 425

x2 = x + space4

y = 575

y2 = y + 100

for color3 in shading3:

    r(x,y,x2,y2,fill = color3,outline = color3)

    x = x + space4

    x2 = x2 + space4

#Covers for Shading 3 (since the shape is irregular, I made a gradient rectangle and covered up the parts that shouldn't be shown)

a24 = p(425,650,475,675,425,675,fill = "#3d3d3d",outline = "#3d3d3d")

a25 = p(650,650,600,675,650,675,fill = "#3d3d3d",outline = "#3d3d3d")

#Additional Minor Details; e.g. lines, dots, wires,etc

#Red lines

l(925,475,975,475,fill = "#912234",width = 7)

l(925,500,975,500,fill = "#912234",width = 4)

l(925,507,975,507,fill = "#912234",width = 4)

l(925,514,975,514,fill = "#912234",width = 4)

#Wires

l(937.5,550,925,575,937.5,600,fill = "grey40",width = 5,smooth = True)

l(940,550,945,575,940,600,fill = "grey28",width = 5,smooth = True)

l(950,550,960,575,950,587.5,962.5,600,fill = "grey28",width = 5,smooth = True)

l(962.5,550,975,575,962.5,600,fill = "grey40",width = 5,smooth = True)

#Dots

o(670,582.5,680,592.5,fill = "grey30")

o(720,582.5,730,592.5,fill = "grey30")

o(770,582.5,780,592.5,fill = "grey30")

#Lines on Middle Section

xL = 450

for L in range(8):

    l(xL,600,xL,650,fill = "black",width = 2)

    xL = xL + 25

l(450,600,625,600,fill = "black",width = 2)

############################################
#                                          #
#                                          #
#                  Scene 1                 # 
#                                          #
############################################

#defining starting positions

x_Image = 100

y_Image = 475

x_Image2 = 175

y_Image2 = 475

#animating using for loop

for f in range(183):
    
    scene = im(x_Image,y_Image,image = vader)

    scene2 = im(x_Image2,y_Image2,image = luke)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

#Railings (Put here because they should be in front of the scene)

    x = 0

    y= 500

    for railings in range(14):

        l(x,y,x,y+75,fill = "white",width = 3)

        x = x+50

    l(0,500,650,500,fill = "white",width = 3)

    #Start with Luke moving backwards and Vader moving forward then, both of them clash their lightsabers

    if f < 150:

        x_Image = x_Image + 0.75

        x_Image2 = x_Image2 + 2

    else:

        x_Image = x_Image + 3.2

        x_Image2 = x_Image2 - 3.2

    s.update()

    sleep(0.03)

    s.delete(scene,scene2,leg)

#making sure Vader and Luke don't disappear during the part with sparks

scene = im(x_Image,y_Image,image = vader)

scene2 = im(x_Image2,y_Image2,image = luke)

leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

joinus = t(200,425,text = "Luke, join the Dark Side.",font = "Arial 15",fill = "#ff0000")

#Note: The real quote is much longer than what is said here

#Railings

x = 0

y= 500

for railings in range(14):

    l(x,y,x,y+75,fill = "white",width = 3)

    x = x+50

l(0,500,650,500,fill = "white",width = 3)

#Sparks when the lightsabers hit eachother

sparks = 100

#Empty Arrays

size = []

x = []

y = []

xSpeed = []

ySpeed = []

sparkDrawings = []

direction = []

#Adding values in the arrays

for i in range(sparks):

    direction.append(choice([-1,1,-2,2]))

    size.append(randint(1,5))

    x.append(randint(345,365))

    y.append(randint(435,455))

    xSpeed.append(randint(5,11))

    ySpeed.append(randint(5,11))

    sparkDrawings.append(0)

#Start the animation

for f in range(50):
    
    #Added text for sound effects
    
    SFX = t(350,375,text = "Bzzzzz!",font = "Arial 15",fill = "white")

    #Creation of each individual spark

    for i in range(sparks):

        sparkDrawings[i] = o(x[i],y[i],x[i]+size[i],y[i]+size[i],fill = "yellow",outline = "red")

        x[i] = x[i] + xSpeed[i]*direction[i]

        y[i] = y[i] + ySpeed[i]*direction[i]*-1

    s.update()

    sleep(0.03)

    for i in range(sparks):

        s.delete(sparkDrawings[i],SFX)

#Deleting Vader and Luke so that there are no duplicates when scene 2 begins

s.delete(scene,scene2,leg,joinus)

############################################
#                                          #
#                                          #
#                  Scene 2                 # 
#                                          #
############################################

for f in range(20):

    scene = im(x_Image,y_Image,image = vader)

    scene2 = im(x_Image2,y_Image2,image = luke)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

#railings

    x = 0

    y= 500

    for railings in range(14):

        l(x,y,x,y+75,fill = "white",width = 3)

        x = x+50

    l(0,500,650,500,fill = "white",width = 3)

    if f < 10:

        x_Image = x_Image - 2

        x_Image2 = x_Image2 + 2

    else:

        x_Image = x_Image + 2

        x_Image2 = x_Image2 - 2

    s.update()

    sleep(0.03)

    s.delete(scene,scene2,leg)

#once again, recreating the images so that they don't disappear during the sparks phase

scene = im(x_Image,y_Image,image = vader)

scene2 = im(x_Image2,y_Image2,image = luke)

leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

never = t(500,437.5,text = "I'll never join you!",font = "Arial 15",fill = "#1a75ff")

#Railings (Put here because they should be in front of the characters)

x = 0

y= 500

for railings in range(14):

    l(x,y,x,y+75,fill = "white",width = 3)

    x = x+50

l(0,500,650,500,fill = "white",width = 3)

#Sparks but in a different direction

sparks = 100

#Empty Arrays

size = []

x = []

y = []

xSpeed = []

ySpeed = []

sparkDrawings = []

direction = []

#Adding values in the arrays

for i in range(sparks):

    direction.append(choice([-1,1,-2,2]))

    size.append(randint(1,5))

    x.append(randint(345,365))

    y.append(randint(435,455))

    xSpeed.append(randint(5,11))

    ySpeed.append(randint(5,11))

    sparkDrawings.append(0)

#Start the animation

for f in range(50):
    
    #Added text for sound effects
    
    SFX = t(350,375,text = "Whoosh!",font = "Arial 15",fill = "white")

    #Creation of each individual spark

    for i in range(sparks):

        sparkDrawings[i] = o(x[i],y[i],x[i]+size[i],y[i]+size[i],fill = "yellow",outline = "red")

        x[i] = x[i] + xSpeed[i]*direction[i]

        y[i] = y[i] + ySpeed[i]*direction[i]

    s.update()

    sleep(0.03)

    for i in range(sparks):

        s.delete(sparkDrawings[i],SFX)

#Deleting Vader and Luke so that there are no duplicates when scene 3 begins

s.delete(scene,scene2,leg,never)

############################################
#                                          #
#                                          #
#                  Scene 3                 # 
#                                          #
############################################

#Once again, this huge block of code is Vader and Luke approaching eachother
    
for f in range(130):

    scene = im(x_Image,y_Image,image = vader)

    scene2 = im(x_Image2,y_Image2,image = luke)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

#railings

    x = 0

    y= 500

    for railings in range(14):

        l(x,y,x,y+75,fill = "white",width = 3)

        x = x+50

    l(0,500,650,500,fill = "white",width = 3)

#Luke is getting cornered and Vader is approaching while talking to him

    if f < 100:

        x_Image = x_Image + 1.5

        x_Image2 = x_Image2 + 2.5

        truth = t(425,380,text = "If only you knew the power of the Dark Side.",font = "Arial 15",fill = "#ff0000")

        truth2 = t(425,405,text = "Obi-Wan never told you what happened to your father.",font = "Arial 15",fill = "#ff0000")

        s.update()

        sleep(0.03)

        s.delete(scene,scene2,leg,truth,truth2)

#After the first 100 frames, Vader starts rapidly approaching Luke at a whopping 4 units a frame

    else:

        x_Image = x_Image + 4

        s.update()

        sleep(0.03)

        s.delete(scene,scene2,leg)

#so they don't disappear durinf spark phase
        
scene = im(x_Image,y_Image,image = vader)

scene2 = im(x_Image2,y_Image2,image = luke)

leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

#More sparks! This time, vertical

sparks = 100

#Empty Arrays

size = []

x = []

y = []

xSpeed = []

ySpeed = []

sparkDrawings = []

direction = []

#Adding values in the arrays

for i in range(sparks):

    direction.append(choice([-1,1,-2,2]))

    size.append(randint(1,5))

    x.append(randint(602,622))

    y.append(randint(440,460))

    xSpeed.append(randint(5,11))

    ySpeed.append(randint(5,11))

    sparkDrawings.append(0)

#Start the animation

for f in range(50):

#Creation of each individual spark

    for i in range(sparks):

        sparkDrawings[i] = o(x[i],y[i],x[i]+size[i],y[i]+size[i],fill = "yellow",outline = "red")

        y[i] = y[i] + ySpeed[i]*direction[i]*-1

    s.update()

    sleep(0.03)

    for i in range(sparks):

        s.delete(sparkDrawings[i])

#deleting characters so there are no duplicates

s.delete(scene,scene2,leg)

#speaking section

for f in range(10):

    scene = im(x_Image,y_Image,image = vader)

    scene2 = im(x_Image2,y_Image2,image = luke)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

    itWasYou = t(650,387.5,text = "He told me enough! It was you who killed him!",font = "Arial 15",fill = "#1a75ff")

    s.update()

    sleep(0.03)

    s.delete(itWasYou,scene,scene2,leg)

#vader approaching
    
for f in range(12):

    scene = im(x_Image,y_Image,image = vader)

    scene2 = im(x_Image2,y_Image2,image = luke)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

    x_Image = x_Image + 5

    s.update()

    sleep(0.03)

    s.delete(scene,scene2,leg)

for f in range(25):

    scene = im(x_Image,y_Image,image = vader)

#Luke now has his arm cut off, ouch
    

    scene2 = im(x_Image2,y_Image2,image = luke_no_arm)

    leg = p(x_Image2+110.5,y_Image2+85,x_Image2+125,y_Image2+100,x_Image2+137.5,y_Image2+100,x_Image2+112.5,y_Image2+65,fill = "grey10")

    scream = t(725,450,text = "AHHHH!",font = "Arial 15",fill = "#1a75ff")

    x_Image = x_Image - 2

    s.update()

    sleep(0.03)

    s.delete(scene,scene2,leg,scream)

############################################
#                                          #
#                                          #
#               Darth Vader                # 
#                                          #
############################################

#Head

p(307,465,630,395,525,300,300,350,fill = "black")


o(239,-10,550,303,fill = "black")

p(250,175,226,200,222,225,220,275,212.5,325,207,367,650,375,662.5,362.5,662.5,350,660,345,657,332,560,175,550,137.5,fill = "black")

a(207,468,389,286,start = 180,extent = 90,fill = "black")

r(207.25,378,350.25,358,fill = "black",outline = "black")

r(298,465,350,375,fill = "black",outline = "black")

#details (parts of the mask)

p(349,162,350,150,375,147,380,160,387.5,200,375,225,360,225,fill = "grey40")

p(360,210,275,262.5,320,335,350,240,fill = "grey40")

l(300,314,350,240,fill = "black",width = 3)

l(305,320,350,240,fill = "black",width = 3)

l(312.5,325,350,240,fill = "black",width = 3)

l(320,325,350,240,fill = "black",width = 3)

p(387.5,200,412.5,207,425,207.5,450,201,488,205,470,305,395,280,381,214,fill = "grey40")

l(475,275,395,228,fill = "black",width = 3)

l(475,287.5,395,228,fill = "black",width = 3)

l(475,300,395,228,fill = "black",width = 3)

l(463,300,395,228,fill = "black",width = 3)

l(387.5,201,381,212.5,400,222,475,223,480,202,fill = "black",width = 2)

#tint

p(325,240,335,230,332,250,335,257,326,268,fill = "white")

p(407,220,414,220,424,241,409,234,fill = "white")

p(460,201,473,201,462.5,214,fill = "white")

#mouth section

p(370,220,322,335,465,309,fill = "black")

l(385,250,400,320,fill = "grey30",width = 10)

l(362,250,376,325,fill = "grey30",width = 10)

l(347,275,355,325,fill = "grey30",width = 10)

l(410,252,423,320,fill = "grey30",width = 10)

o(355,220,390,260,fill = "white")

l(322,335,351,250,353,225,362.5,215,378,215,390,222,395,237.5,403,248,465,309,fill = "white",width = 5,smooth = True)

l(465,309,322,335,fill = "white",width = 5)

o(300,325,325,345,fill = "white")

o(462.5,297,485,314,fill = "white")

#left eye

p(350,162.5,352,207,340,220,325,237.5,280,260,262.5,223,274,175,300,158,fill = "black",smooth = True)

p(325,203,347,200,350,207,328,210,fill = "white")

p(300,225,299,220,300,206,294,212.5,288,230,290,240,fill = "white")

p(300,237.5,325,234,312.5,240,300,247,fill = "white")

#right eye

p(380,157,400,145,425,130,450,135,472,150,487.5,175,492,200,480,201,462.5,202,437.5,203,415,204,386,200,fill = "black",smooth = True)

p(400,187.5,423,183,423,192,400,199,fill = "white")

p(466,205,464,193,462,187,450,176,455,187.5,452,198,fill = "white")

#helmet highlights

l(238,175,276,150,350,145,375,137.5,425,120,475,115,500,125,525,150,550,175,628,300,fill = "white",width = 2)

l(262.5,225,262.5,212.5,275,175,287.5,160,300,155,325,157,349,162.5,fill = "white",smooth = True)

l(380,156,400,140,425,130,450,137,475,150,498,200,fill = "white",smooth = True)

#Body

p(307,465,295,495,225,530,187.5,550,162,600,150,650,151,675,162.5,737.5,150,810,925,810,925,475,630,395,fill = "black")

#hand / thumb

p(750,805,650,725,577,625,510,550,500,537.5,498,500,500,487.5,512.5,476,525,475,550,476,700,551,750,550,775,525,787.5,487.5,925,500,925,810,fill = "grey7",outline = "white")

p(500,487.5,512.5,476,525,475,550,476,700,551,750,550,775,525,775,563,762.5,575,712.5,587.5,587.5,525,fill = "white")

r(925,675,975,725,fill = "grey7",outline = "grey7")

r(970,550,925,575,fill = "grey7",outline = "grey7")

#index finger

p(805,425,787.5,400,762.5,375,750,362.5,737.5,350,735,337.5,737.5,325,762.5,310,775,308,800,312.5,825,325,850,350,874,376,900,425,fill = "grey7",smooth = True,outline = "white")

#middle finger

p(775,475,776,450,785,435,875,396,900,398,925,405,982,437,990,450,1000,470,1000,485,970,550,825,575,849,512.5,800,505,fill = "grey7",outline = "white")

l(787.5,487.5,800,505,825,510,850,513,950,517,fill = "white",width = 2,smooth = True)

#ring finger

p(970,550,980,560,992,587.5,995,625,990,650,975,675,900,675,825,630,800,600,800,575,799,550,805,535,812.5,535,875,539,951,560,fill = "grey7",outline = "white")

#pinky finger

p(950,700,937.5,720,875,724,850,725,825,730,812.5,737.5,807,750,812.5,775,850,805,988,805,1001,775,1000,750,987.5,687.5,975,676,950,687.5,fill = "grey7",outline = "white")

r(625,390,310,475,fill = "black",outline = "black")

#final text section

for f in range(50):

    no = t(875,75,text = "No",font = "Arial 50",fill = "#ff0000")

    s.update()

    sleep(0.03)

for f in range(50):

    father = t(875,150,text = "I am your father.",font = "Arial 50",fill = "#ff0000")

    s.update()

    sleep(0.03)

#The End!








