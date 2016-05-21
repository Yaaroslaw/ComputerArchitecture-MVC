

class Day(object):
    def __init__(self, pressure, temperature, wind, number):
        self.pressure = pressure
        self.temperature = temperature
        self.wind = wind
        self.number = number

    def __str__(self):
        return "Day: number: {}, {} Celsius, pressure:{}, wind:{}".format(self.number, self.temperature, self.pressure, self.wind)


    def __eq__(self, other):
        return self.temperature == other.temperature and self.wind == other.wind





























