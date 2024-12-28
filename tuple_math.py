
class Tuple_math:
    def add(a: tuple, b: tuple) -> tuple:
        return (a[0] + b[0], a[1] + b[1])
    
    def sub(a: tuple, b: tuple) -> tuple:
        return (a[0] - b[0], a[1] - b[1])
    
    def dot(a: tuple, b: tuple) -> float:
        return a[0] * b[0] + a[1] * b[1]
    
    def scale(a: tuple, b: float) -> tuple:
        return (a[0] * b, a[1] * b)
        
    def normalize(a: tuple) -> tuple:
        l = Tuple_math.length(a)
        return (a[0] / l, a[1] / l)
    
    def length(a: tuple) -> float:
        return (a[0] ** 2 + a[1] ** 2) ** 0.5
    
    def distance(a: tuple, b: tuple) -> float:
        return Tuple_math.length(Tuple_math.sub(a, b))
    
    def taxi_length(a: tuple) -> float:
        return abs(a[0]) + abs(a[1])
    
    def taxi_distance(a: tuple, b: tuple) -> float:
        return Tuple_math.taxi_length(Tuple_math.sub(a, b))
    
"""
    def rotate(self, a: tuple, angle: float) -> tuple:
        from math import cos, sin
        return (a[0] * math.cos(angle) - a[1] * math.sin(angle),
                a[0] * math.sin(angle) + a[1] * math.cos(angle))

"""