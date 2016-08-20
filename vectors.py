import math
import numbers

class Vector:
    ''' Handling R2 vectors for basic operations '''
    magnitude = None
    angle = None
    units = 'radians'
    x = None
    y = None

    def __init__(self, x=None, y=None, magnitude=None, angle=None, units='radians'):
        self.magnitude = magnitude
        self.angle = angle
        self.units = units
        self.x = x
        self.y = y

    @staticmethod
    def from_components(x=None, y=None, units='radians'):
        if x and y:
            magnitude, angle = Vector.polarFromComponents(x, y, units)
            v = Vector(x, y, magnitude, angle, units)
            return v
        else:
            print 'You need to specify the (x,y) components of the vector'

    @staticmethod
    def from_polar(magnitude=None, angle=None, units='radians'):
        if magnitude and angle:
            x, y = Vector.componentsFromPolar(magnitude, angle, units)
            v = Vector(x, y, magnitude, angle, units)
            return v
        else:
            'You need to specify the magnitude and angle of the vector (units="radians" by default)'

    @staticmethod
    def componentsFromPolar(magnitude=None, angle=None, units='radians'):
        if not magnitude and not angle:
            print 'You need to specify the magnitude and angle of the vector (units="radians" by default)'
            x = None
            y = None
        else:
            if units == 'radians':
                theta = angle
            elif units == 'degrees':
                theta = math.radians(angle)
            x = magnitude * math.cos(theta)
            y = magnitude * math.sin(theta)
        return x,y

    @staticmethod
    def polarFromComponents(x=None, y=None, units='radians'):
        if not x and not y:
            print 'You need to specify the (x,y) components of the vector'
            magnitude = None
            angle = None
        else:
            quadrantOffset = math.pi
            magnitude = math.sqrt(x*x + y*y)
            angle = math.atan(1.0*y/x)
            if units == 'degrees':
                angle = math.degrees(angle)
                quadrantOffset = 180.0
            if x < 0 and y >= 0 or x < 0 and y < 0:
                angle = angle + quadrantOffset
        return magnitude, angle

    def _add(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            magnitude, angle = Vector.polarFromComponents(x, y, self.units)
            return x,y,magnitude,angle

    def add(self, other):
            x, y, magnitude, angle = self._add(other)
            self.x = x
            self.y = y
            self.magnitude = magnitude
            self.angle = angle

    def plus(self, other):
            x, y, magnitude, angle = self._add(other)   
            return Vector(x, y, magnitude, angle, self.units)

    def _substract(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            magnitude, angle = Vector.polarFromComponents(x, y, self.units)
            return x, y, magnitude, angle
    
    def substract(self, other):
            x, y, magnitude, angle = self._substract(other)
            self.x = x
            self.y = y
            self.magnitude = magnitude
            self.angle = angle

    def minus(self, other):
        x, y, magnitude, angle = self._substract(other)
        return Vector(x, y, magnitude, angle, self.units)

    def times(self, escalar=None):
        if isinstance(escalar, numbers.Number):
            x = self.x * escalar
            y = self.y * escalar
            magnitude, angle = Vector.polarFromComponents(x, y, self.units)
            self.x = x
            self.y = y
            self.magnitude = magnitude
            self.angle = angle

    def __str__(self):
        s = 'Polar form:\n\tMagnitude: {}\n\tAngle: {} ({})\nComponents:\n\tX:{}, Y:{}\n'.format(self.magnitude, self.angle, self.units, self.x, self.y)
        return s


u = Vector.from_polar(4,310,'degrees')
w = Vector.from_polar(7,50,'degrees')

print u
print w

print u.plus(w)
