def setup():
    size(600, 600)
    background(180)
    global img
    img = loadImage("janosik.jpg") # doceniam żarcik :)
    strokeWeight(6)
    noFill()
    textSize(16)
 
def draw():
    try:
        image(img, width/300, height/170, 595, 595)    
    except:
        stroke("#FF0000")
        text("brak pliku", 25, 25)
    else:
        stroke("#7FFFD4")
    finally:
        rect(width/300, height/160, 595, 595)
# 1,5pkt
