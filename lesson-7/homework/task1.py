import math

class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.components, other.components)]) if isinstance(other, Vector) and len(self.components) == len(other.components) else self._error()
    
    def __sub__(self, other):
        return Vector(*[a - b for a, b in zip(self.components, other.components)]) if isinstance(other, Vector) and len(self.components) == len(other.components) else self._error()
    
    def __mul__(self, other):
        if isinstance(other, (int, float)): return Vector(*[a * other for a in self.components])
        if isinstance(other, Vector) and len(self.components) == len(other.components): return sum(a * b for a, b in zip(self.components, other.components))
        self._error()
    
    def __rmul__(self, scalar): return self * scalar
    
    def magnitude(self): return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self): return self * (1 / self.magnitude()) if self.magnitude() else self._error("Cannot normalize zero vector.")
    
    def __repr__(self): return f"Vector{self.components}"
    
    def _error(self, msg="Invalid operation."): raise ValueError(msg)
   
