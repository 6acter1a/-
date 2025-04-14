import math

class ReactionSimulator:
    def __init__(self, order, a0, at, time):
        self.order = order  # 반응차수
        self.a0 = a0        # 초기 농도 [A]₀
        self.at = at        # 시간 t 후 농도 [A]t
        self.time = time    # 경과 시간 t

    def calculate_rate(self):
        if self.order == 0:
            # 0차 반응 속도는 일정
            rate = (self.a0 - self.at) / self.time
        elif self.order == 1:
            # 1차 반응: v = k[A] → k = (1/t) ln([A]₀/[A]t), v = k[A]
            if self.at <= 0 or self.a0 <= 0:
                return None
            k = (1 / self.time) * math.log(self.a0 / self.at)
            rate = k * self.at  # 속도 = k * [A]t
        elif self.order == 2:
            # 2차 반응: 1/[A] = 1/[A]₀ + kt → k = (1/[A]t - 1/[A]₀)/t
            if self.at <= 0 or self.a0 <= 0:
                return None
            k = (1 / self.at - 1 / self.a0) / self.time
            rate = k * (self.at ** 2)  # 속도 = k * [A]^2
        else:
            return None
        return round(rate, 6)