def setup():
    size(600,600)
    point(40,20)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    rectMode(CENTER)
    rect(300,300,300,300)
    fill(100,100,100,100)
    if mousePressed:
        rect(mouseX, mouseY,mouseX,mouseY)
    # brakuje else by coś się zadziało gdy nie klikamy
#1,5pkt
