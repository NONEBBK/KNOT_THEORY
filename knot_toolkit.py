# knot_toolkit.py

import snappy

class Knot:
    """
    A robust class to represent a knot using its canonical census name.
    """
    def __init__(self, name: str):
        self.name = name
        self.invariants = {}
        self._snappy_manifold = None
    
    def __repr__(self):
        return f"Knot(name='{self.name}')"
    
    def get_snappy_manifold(self):
        if self.name == '0_1': return None
        if self._snappy_manifold is None:
            self._snappy_manifold = snappy.Manifold(self.name)
        return self._snappy_manifold

def calculate_hyperbolic_volume(knot: Knot) -> float:
    if 'hyperbolic_volume' in knot.invariants:
        return knot.invariants['hyperbolic_volume']
    
    # --- THIS IS THE FIX ---
    # The variable is 'knot', not 'self'.
    if knot.name == '0_1':
        volume = 0.0
    else:
        manifold = knot.get_snappy_manifold()
        try: volume = float(manifold.volume())
        except RuntimeError: volume = 0.0
    knot.invariants['hyperbolic_volume'] = volume
    return volume
