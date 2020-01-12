import random
def setup():
    global cornerpointx, cornerpointy, canvasx, canvasy, back
    global bix, mode, boxx, boxy, boxw, boxh, boxxchange, boxychange
    global food, foodx, foody, foodsizex, foodsizey, musicbackground, hardcore
    global pointcounter, pointincrease, pointtotal, numberofpoints, killergoomba
    global multiplier, killer, killerx, killery, killerx2, killery2, killer2
    global boxx2, boxy2, bix2, boxx2change, boxy2change, minim, coinsound, player1, player2
    add_library("minim") #for sound
    minim=Minim(this)
    coinsound=minim.loadFile("coin.mp3")
    musicbackground=minim.loadFile("balloontrip.mp3")
    musicbackground.loop()
    hardcore = "back.jpg"
    multiplier = 1
    numberofpoints = 0
    points = 100
    pointincrease = 0
    pointtotal = pointincrease * numberofpoints
    pointcounter = 0
    boxw = 30
    boxh = 30
    boxx = 297
    boxy = 369
    boxx2 = 697
    boxy2 = 369
    cornerpointx = 0
    cornerpointy = 0
    canvasx = 1024
    canvasy = 768
    boxxchange = 0
    boxychange = 0
    boxx2change = 0
    boxy2change = 0
    foodsizey = 30
    foodsizex = 30
    size(1024, 768)
    foodx = random.randint(50, 974)
    foody = random.randint(50, 718)
    killerx = random.randint(50, 512)
    killery = random.randint(50, 384)
    killerx2 = random.randint(512, 974)
    killery2 = random.randint(384, 718)
    killergoomba = loadImage("killergoomba.png")
    food = loadImage("coin.png")
    back = loadImage("blackpattern.jpg")
    player1 = loadImage("player1.png")
    player2 = loadImage("player2.png")
    background = image(back, cornerpointx, cornerpointy, canvasx, canvasy)
    
def draw():
    global cornerpointx, cornerpointy, canvasx, canvasy, back
    global bix, boxx, boxy, boxw, boxh, boxxchange, boxychange
    global food, foodx, foody, foodsizex, foodsizey
    global pointcounter, pointincrease, pointtotal, numberofpoints
    global multiplier, killer, killerx, killery, killerx2, killery2, killergoomba
    global boxx2, boxy2, bix2, boxx2change, boxy2change, coinsound, player1, player2

    background = image(back, cornerpointx, cornerpointy, canvasx, canvasy)
    fill(255,0,0)
    killer2 = image(killergoomba, killerx2, killery2, foodsizex, foodsizey)
    killer = image(killergoomba, killerx, killery, foodsizex, foodsizey)
    fill(255,255,255)
    foodpoint = image(food, foodx, foody, foodsizex, foodsizey)
    bix = image(player1, boxx, boxy, boxw, boxh)
    bix2 = image(player2, boxx2, boxy2, boxw, boxh)
    textSize(15)
    fill(255,255,255)
    text("Press h to go hardcore, click screen for easy", 350, 700)
    
    if boxxchange == 0 and boxychange == 0 and boxx2change == 0 and boxy2change == 0:
        textSize(50)
        fill(169, 20, 90)
        text("How to Play:", 375, 100)
        textSize(30)
        fill(255,255,255)
        text("P1 use arrow keys, P2 use wasd", 275, 150)
        text("Press any arrow key/wasd to start", 275, 200)
        text("Click anywhere to reset", 275, 250)
        text("P1 = Red mushroom, P2 = green mushroom", 275, 300)
        text("Avoid brown mushroom, coin = point", 275, 350)
    
    if boxx >= 1 and boxy >= 1 and boxx <= 993 and boxy <= 737 and boxx2 >= 1 and boxy2 >= 1 and boxx2 <= 993 and boxy2 <= 737:
        boxx += boxxchange
        boxy += boxychange
        boxx2 += boxx2change
        boxy2 += boxy2change
        textSize(30)
        fill(255, 0, 0)
        text("Your score:", 724, 30)
        text(pointcounter, 924, 30)
    else:
        textSize(50)
        fill(255, 255, 255)
        text("GAME OVER!", 360, 400)
        text ("Your Score is ", 350, 500)
        text (pointcounter, 685, 500)
        if key == "h":
            back = loadImage(hardcore)
            multiplier = 8
            foodx = random.randint(50, 974)
            foody = random.randint(50, 718)
            killerx = random.randint(50, 512)
            killery = random.randint(50, 384)
            killerx2 = random.randint(512, 974)
            boxx = 297
            boxy = 369
            boxx2 = 697
            boxy2 = 369
            pointcounter = 0
    if boxx >= foodx - foodsizex and boxx <= foodx + foodsizex and boxy >= foody - foodsizey and boxy <= foody +foodsizey:
        pointcounter = pointcounter + 100
        foodx = random.randint(50, 974)
        foody = random.randint(50, 718)
        killerx = random.randint(50, 512)
        killery = random.randint(50, 384)
        killerx2 = random.randint(512, 974)
        multiplier = multiplier + 0.3
        coinsound.loop(0)
    if boxx2 >= foodx - foodsizex and boxx2 <= foodx + foodsizex and boxy2 >= foody - foodsizey and boxy2 <= foody +foodsizey:
        pointcounter = pointcounter + 100
        foodx = random.randint(50, 974)
        foody = random.randint(50, 718)
        killerx = random.randint(50, 512)
        killery = random.randint(50, 384)
        killerx2 = random.randint(512, 974)
        multiplier = multiplier + 0.3
        coinsound.loop(0)
    elif boxx >= killerx - foodsizex and boxx <= killerx + foodsizex and boxy >= killery - foodsizey and boxy <= killery + foodsizey:
        textSize(50)
        fill(255, 255, 255)
        text("GAME OVER!", 360, 400)
        text ("Your Score is ", 350, 500)
        text (pointcounter, 685, 500)
        boxxchange = 0
        boxychange = 0
        boxx2change = 0
        boxy2change = 0
        multiplier = 0

        if key == "h":
            back = loadImage(hardcore)
            multiplier = 8
            foodx = random.randint(50, 974)
            foody = random.randint(50, 718)
            killerx = random.randint(50, 512)
            killery = random.randint(50, 384)
            killerx2 = random.randint(512, 974)
            pointcounter = 0
            killerx2 = random.randint(512, 974)
    elif boxx2 >= killerx - foodsizex and boxx2 <= killerx + foodsizex and boxy2 >= killery - foodsizey and boxy2 <= killery + foodsizey:
        textSize(50)
        fill(255, 255, 255)
        text("GAME OVER!", 360, 400)
        text ("Your Score is ", 350, 500)
        text (pointcounter, 685, 500)
        boxx2change = 0
        boxy2change = 0
        boxxchange = 0
        boxychange = 0
        multiplier = 0
        if key == "h":
            back = loadImage(hardcore)
            multiplier = 8
            foodx = random.randint(50, 974)
            foody = random.randint(50, 718)
            killerx = random.randint(50, 512)
            killery = random.randint(50, 384)
            killerx2 = random.randint(512, 974)
            pointcounter = 0

    elif boxx >= killerx2 - foodsizex and boxx <= killerx2 + foodsizex and boxy >= killery2 - foodsizey and boxy <= killery2 + foodsizey:
        textSize(50)
        fill(255, 255, 255)
        text("GAME OVER!", 360, 400)
        text ("Your Score is ", 350, 500)
        text (pointcounter, 685, 500)
        boxxchange = 0
        boxychange = 0
        boxx2change = 0
        boxy2change = 0
        multiplier = 0
        if key == "h":
            back = loadImage(hardcore)
            multiplier = 8
            foodx = random.randint(50, 974)
            foody = random.randint(50, 718)
            killerx = random.randint(50, 512)
            killery = random.randint(50, 384)
            killerx2 = random.randint(512, 974)
            pointcounter = 0

    elif boxx2 >= killerx2 - foodsizex and boxx2 <= killerx2 + foodsizex and boxy2 >= killery2 - foodsizey and boxy2 <= killery2 + foodsizey:
        textSize(50)
        fill(255, 255, 255)
        text("GAME OVER!", 360, 400)
        text ("Your Score is ", 350, 500)
        text (pointcounter, 685, 500)
        boxxchange = 0
        boxychange = 0
        boxx2change = 0
        boxy2change = 0
        multiplier = 0
        if key == "h":
            back = loadImage(hardcore)
            multiplier = 8
            foodx = random.randint(50, 974)
            foody = random.randint(50, 718)
            killerx = random.randint(50, 512)
            killery = random.randint(50, 384)
            killerx2 = random.randint(512, 974)
            pointcounter = 0

    else:
        pointcounter = pointcounter

    
def keyPressed():
    global cornerpointx, cornerpointy, canvasx, canvasy, back
    global bix, mode, boxx, boxy, boxw, boxh, boxxchange, boxychange
    global food, foodx, foody, foodsizex, foodsizey
    global pointcounter, pointincrease, pointtotal, numberofpoints
    global multiplier, killer, killerx, killery, killerx2, killery2, killer2
    global boxx2, boxy2, bix2, boxx2change, boxy2change
    if keyCode == DOWN:
        boxychange = 3 * multiplier
        boxxchange = 0
    elif keyCode == UP:
        boxychange = -3 * multiplier
        boxxchange = 0
    if keyCode == RIGHT:
        boxxchange = 3 * multiplier
        boxychange = 0
    elif keyCode == LEFT:
        boxxchange = -3 * multiplier
        boxychange = 0
    if key == "s":
        boxy2change = 3 * multiplier
        boxx2change = 0
    elif key == "w":
        boxy2change = -3 * multiplier
        boxx2change = 0
    if key == "d":
        boxx2change = 3 * multiplier
        boxy2change = 0
    elif key == "a":
        boxx2change = -3 * multiplier
        boxy2change = 0
def mousePressed():
    global cornerpointx, cornerpointy, canvasx, canvasy, back
    global bix, mode, boxx, boxy, boxw, boxh, boxxchange, boxychange
    global food, foodx, foody, foodsizex, foodsizey
    global pointcounter, pointincrease, pointtotal, numberofpoints
    global multiplier, killer, killerx, killery, killerx2, killery2, killer2
    global boxx2, boxy2, bix2, boxx2change, boxy2change
    if mousePressed:
        multiplier = 1
        numberofpoints = 0
        points = 100
        pointincrease = 0
        pointtotal = pointincrease * numberofpoints
        pointcounter = 0
        boxw = 30
        boxh = 30
        boxx = 297
        boxy = 369
        boxx2 = 697
        boxy2 = 369
        cornerpointx = 0
        cornerpointy = 0
        canvasx = 1024
        canvasy = 768
        boxxchange = 0
        boxychange = 0
        boxx2change = 0
        boxy2change = 0
        foodsizey = 30
        foodsizex = 30
        size(1024, 768)
        foodx = random.randint(50, 950)
        foody = random.randint(50, 300)
        killerx = random.randint(50, 475)
        killery = random.randint(50, 150)
        killerx2 = random.randint(475, 950)
        killery2 = random.randint(150, 300)
        back = loadImage("blackpattern.jpg")
        
    