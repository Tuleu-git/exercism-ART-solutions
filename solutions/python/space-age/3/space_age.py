class SpaceAge:
    
    Earth_Year_Seconds = 31_557_600
    RATIOS = {
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Earth': 1.0,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }
    
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds
    
    def __getattr__(self, attr: str) -> float:
        return lambda: round(self.seconds / self.Earth_Year_Seconds / self.RATIOS[attr[3:].title()], 2)