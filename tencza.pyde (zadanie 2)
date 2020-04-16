def setup():
    size(600, 600)
    textSize(150)
    textAlign(LEFT, TOP)
    global color1, color2, kolor, klatki
    color1 = "#ff0000"
    color2 = "#ffff00"
    noStroke()
    kolor = 0
    klatki = 0
    fill(255)
    text("C", 350, 300)
def draw():
    global klatki, kolor

    jd()

    klatki += 1
    if klatki % 1 == 0:
        kolor += 1
    wzorek(350, 300, kolor); wzorek(150, 300, kolor)

def keyPressed():
    global color1, color2
    if keyCode in [LEFT, RIGHT]:
        color1, color2 = color2, color1
    if key == 'c' or key == 'C':
        fill(color1)
        text("C", 350, 300)

def keyReleased():
    global color1, color2
    if keyCode in [LEFT, RIGHT]:
        color1, color2 = color2, color1
    if key == 'c' or key == 'C':
        fill(255)
        text("C", 350, 300)


def jd():
    podswietlenie = (mouseX >= 150 and mouseX <= 150 + 100  and mouseY >= 300 and mouseY <= 300 + 100)
    if podswietlenie:
        fill(color2)
        text("K", 150, 300)
    else:
        fill(255)
        text("K", 150, 300)

def wzorek(x, y, start):
    rainbow = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000ff", "#4B0082", "#EE82EE"]
    i = x 
    j = y
    k = start
    while(i <= x + 150):
        fill(rainbow[k % 7])
        rect(i, y, 10, 10)
        rect(i, y + 150, 10, 10)
        i += 10
        k += 1
    while(j <= y + 150):
        fill(rainbow[k % 7])
        rect(x, j, 10, 10)
        rect(x + 150, j, 10, 10)
        j += 10
        k += 1
