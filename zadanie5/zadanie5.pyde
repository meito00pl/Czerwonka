from krejzi_dajamondo import KrejziDajamondo
from dajamondo import Dajamondo
from dajamondo_system import DajamondoSystem

systems = None

def setup():
    global systems
    size(750, 750)
    systems = []
    
def draw():
    background(255)
    for ps in systems:
        ps.run()
        ps.addParticle()
        
def mousePressed():
    systems.append(DajamondoSystem(3, PVector(mouseX, mouseY)))
