add_library('pdf')
def setup():
    global img, img1, img2, pressed
    size (492, 633)
    img = loadImage("kobieta.jpg")
    img1 = loadImage("okular.png")
    img2 = loadImage("wasy.png")
    beginRecord(PDF, "pedef.pdf")

def draw():
    global img, img1, img2
    image(img, 0,0, width, height)
    if key == CODED:
        if keyCode == RIGHT:
            image(img1, -140, -100, 1600, 700)
                
        if keyCode == LEFT:
            image(img2, 120, 250, 500, 250)
    
    
def mousePressed():
    endRecord()
    exit()
