
def area(l: float, w: float) -> float:
    """Return the area of a rectangle."""
    if l < 0 or w < 0:
        raise ValueError("Length and width must be non-negative.")
    return l * w
