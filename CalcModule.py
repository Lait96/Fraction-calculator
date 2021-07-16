import GCDandLCM as GL


class FractionCalc:
    def __init__(self, i1, i2, i3):
        def InFraction(i1f, i2f, i3f):
            if i1f:
                i2f += i1f * i3f
            return [i2f, i3f]

        self.fraction = InFraction(i1, i2, i3)
        self.DivisionResult = self.fraction[0] / self.fraction[1]

    def beautiful_return(self):

        def isInt(n):
            return int(n) == float(n)

        self.DivisionResult = self.fraction[0] / self.fraction[1]
        if isInt(self.DivisionResult):
            return int(self.DivisionResult)
        gcd = GL.gcd(self.fraction[0], self.fraction[1])
        if gcd > 1:
            self.fraction = list(map(lambda x: x // gcd,
                                     self.fraction))
        if self.fraction[0] > self.fraction[1]:
            self.fraction = [self.fraction[0] // self.fraction[1],
                             self.fraction[0] % self.fraction[1],
                             self.fraction[1]]
        return self.fraction

    def CommonDenominator(self, other):
        if self.fraction[1] != other.fraction[1]:
            self.fraction, other.fraction = GL.lcm(self.fraction,
                                                   other.fraction)

    def __add__(self, other):
        self.CommonDenominator(other)
        self.fraction = [self.fraction[0] + other.fraction[0],
                         self.fraction[1]]
        return self.beautiful_return()

    def __sub__(self, other):
        self.CommonDenominator(other)
        self.fraction = [self.fraction[0] - other.fraction[0],
                         self.fraction[1]]
        return self.beautiful_return()