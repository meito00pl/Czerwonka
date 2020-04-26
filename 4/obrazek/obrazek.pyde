add_library('pdf')
def setup():
    global img, img1, img2, pressed
    size (492, 633)
    img = loadImage("dowod.jpg")
    img1 = loadImage("okular.png")
    img2 = loadImage("wasy.png") # nie załączyłeś tego pliku do repozytorium
    beginRecord(PDF, "pedef.pdf")

def draw():
    global img, img1, img2
    image(img, 0,0, width, height)
    if key == CODED:
        if keyCode == RIGHT:
            image(img1, -140, -100, 1600, 700)
                
        if keyCode == LEFT:
            image(img2, 120, 250, 500, 250) # nie działą, bo nie ma pliku i psuje też zapis pdfa
    
    
def mousePressed():
    endRecord() # podając dopiero w tej funkcji zapisujesz dużo klatek tego samego i pdf będzie tym icęższy im dłużej minie od odpalenia programu do kliknięcia
    exit()
    
# 1,25p
