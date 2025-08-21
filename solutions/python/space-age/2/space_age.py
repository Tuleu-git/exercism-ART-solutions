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
    
    def on_mercury(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Mercury'], 2)
    
    def on_venus(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Venus'], 2)
    
    def on_earth(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Earth'], 2)
    
    def on_mars(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Mars'], 2)
    
    def on_jupiter(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Jupiter'], 2)
    
    def on_saturn(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Saturn'], 2)
    
    def on_uranus(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Uranus'], 2)
    
    def on_neptune(self) -> float:
        return round(self.seconds / self.Earth_Year_Seconds / self.RATIOS['Neptune'], 2)