def setup():
    size(600, 600)
    global x, y, xSpeed, ySpeed
    x = 600
    y = 300
    
    xSpeed = 5
    ySpeed = 5

def draw():
    global x, y, xSpeed, ySpeed
    background(0)
    textSize(25)
    fill(255)
    text("kliknij, aby zakonczyc", 20, 40)
    if mousePressed and (mouseButton == LEFT):
        exit()
    x = x + xSpeed
    if x > width or x < 0:
        xSpeed *= -1

    y = y + ySpeed
    if y > height or y <0:
        ySpeed *= -1
    
    fill(random(255), random(255), random(255))
    ellipse(x, y, 50, 50)

    



    
