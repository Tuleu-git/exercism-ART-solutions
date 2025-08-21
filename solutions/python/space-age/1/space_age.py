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

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    def on_mercury(self):
        return round(self.seconds / 31_557_600 / RATIOS['Mercury'], 2)
    def on_venus(self):
        return round(self.seconds / 31_557_600 / RATIOS['Venus'], 2)
    def on_earth(self):
        return round(self.seconds / 31_557_600 / RATIOS['Earth'], 2)
    def on_mars(self):
        return round(self.seconds / 31_557_600 / RATIOS['Mars'], 2)
    def on_jupiter(self):
        return round(self.seconds / 31_557_600 / RATIOS['Jupiter'], 2)
    def on_saturn(self):
        return round(self.seconds / 31_557_600 / RATIOS['Saturn'], 2)
    def on_uranus(self):
        return round(self.seconds / 31_557_600 / RATIOS['Uranus'], 2)
    def on_neptune(self):
        return round(self.seconds / 31_557_600 / RATIOS['Neptune'], 2)
