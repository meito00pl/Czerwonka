def setup():
    size(600, 600)
    background(180)
    global img
    img = loadImage("janosik.jpg")
    strokeWeight(6)
    textSize(16)
 
def draw():
    rect(width/300, height/160, 595, 595)
    try:
        stroke("#7FFFD4")
        image(img, width/300, height/170, 595, 595)
           
    except:
        stroke("#FF0000")
        text("brak pliku", 25, 25)
