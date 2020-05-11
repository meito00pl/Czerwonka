from dajamondo import Dajamondo
from krejzi_dajamondo import KrejziDajamondo

class DajamondoSystem(object):
    
    def __init__(self, num, v):
        self.particles = []
        self.origin = v.get()
        for i in range(num):
            self.particles.append(Dajamondo(self.origin))
            
    def run(self):
        for i in reversed(range(len(self.particles))):
            p = self.particles[i]
            p.run()
            if p.isDead():
                del self.particles[i]
                
    def addParticle(self):
        p = None
        if int(random(0, 7)) == 0:
            p = Dajamondo(self.origin)
        else:
            p = KrejziDajamondo(self.origin)
        self.particles.append(p)
        
    def dead(self):
        return self.particles.isEmpty()
