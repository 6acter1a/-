import math
class ReactionSimulator:
    def __init__(self, order, a0, at, time):
        self.order = order  
        self.a0 = a0        
        self.at = at        
        self.time = time    
    def calculate_rate(self):
        if self.order == 0:
            rate = (self.a0 - self.at) / self.time
        elif self.order == 1:
            if self.at <= 0 or self.a0 <= 0:
                return None
            k = (1 / self.time) * math.log(self.a0 / self.at)
            rate = k * self.at  
        elif self.order == 2:
            if self.at <= 0 or self.a0 <= 0:
                return None
            k = (1 / self.at - 1 / self.a0) / self.time
            rate = k * (self.at ** 2)  
        else:
            return None
        return round(rate, 6)