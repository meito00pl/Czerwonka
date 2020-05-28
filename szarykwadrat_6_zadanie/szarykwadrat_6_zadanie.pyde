class Kwadrat(object):
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)

        
class SzaryKwadrat(Kwadrat):
    def sketchSzary(self, x, y):
        rectMode(RADIUS)
        fill(255)
        super(SzaryKwadrat, self).sketch(x, y)
        rectMode(CENTER)
        fill(100)
        super(SzaryKwadrat, self).sketch(x, y)

def setup():
    size(500, 500)
    malySzaryKwadrat = SzaryKwadrat(30.0)
    malySzaryKwadrat.sketchSzary(400, 400)
    malySzaryKwadrat.sketchSzary(325,300)
    duzySzaryKwadrat = SzaryKwadrat(120.0)
    duzySzaryKwadrat.sketchSzary(150, 150)
