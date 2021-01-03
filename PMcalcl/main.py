import math


class uncertainNumber (object):

    def __init__(self, number, uncertainty=0.0, deg_unc=None, *args, **kwargs):
        if isinstance(number, (tuple,list)):
            if len(number) >= 2:
                uncertainty = number[1]
                number = number[0]
            elif len(number) == 1:
                number = number[0]
            else:
                raise TypeError("Not consistent types - tuple must contain 2 elements")

        self.deg_un = deg_unc
        self.unc = self.round_up(abs(uncertainty), un=True) if uncertainty != 0 or not self.need_ch(uncertainty) else uncertainty
        self.deg_un = self.deg_un if not self.deg_un is None else self.deg(self.unc)
        self.num = number if number == 0 or uncertainty == 0 else round(number, self.deg_un)

    def __round__(self, n=None):
        return self._round(self.num, n)

    def _round(self, num, n=0):
        return round(num, n - self.deg(num))

    def round_up(self, num, n=None, un=False):
        dg = -self.deg(num)
        dg10 = 10 ** dg
        if un == True:
            self.deg_un = dg
            num = round(num, 4+dg)
        if n in {None, 0}:
            num = math.ceil(num * dg10)/dg10 if num > 0 else math.floor(num * dg10)/dg10
        else:
            n10 = 10 ** n
            num = math.ceil(num * n10 * dg10) / dg10 / n10 if num > 0 else math.floor(num * n10 * dg10) / dg10 / n10
        return num

    def deg(self, num):
        return int(math.log10(abs(num))) if num != 0 else -math.inf

    def need_ch(self, num):
        return round(num, 1 - int(math.log10(abs(num)))) == num

    def fixit(self, other, op="this operation"):
        if isinstance(other, uncertainNumber):
            return other
        if isinstance(other, (float, int)):
            return uncertainNumber(other)
        elif isinstance(other, (tuple, list)):
            return uncertainNumber(other[0], other[1])
        else:
            self._illegal(op)
            raise TypeError('other must be of type int, float, array or tuple')

    def __add__(self, other):
        other = self.fixit(other, "+")
        return uncertainNumber(self.num + other.num,
                       self.unc + other.unc)

    def __radd__(self, other):  # defines other + self
        other = self.fixit(other, "+")
        return self.__add__(other)

    def __iadd__(self, other):
        other = self.fixit(other, "+")
        self.num += other.num
        self.unc += other.unc
        self.__init__(self.num, self.unc)

    def __sub__(self, other):
        other = self.fixit(other, "-")
        return uncertainNumber(self.num - other.num,
                       self.unc + other.unc)

    def __rsub__(self, other):  # defines other + self
        other = self.fixit(other, "-")
        return uncertainNumber(other.num - self.num,
                               self.unc + other.unc)

    def __isub__(self, other):
        other = self.fixit(other, "-")
        self.num -= other.num
        self.unc += other.unc
        self.__init__(self.num, self.unc)

    def __mul__(self, other):
        other = self.fixit(other, "*")
        _product = self.num * other.num
        return uncertainNumber(_product,
                               _product * (self.unc / self.num + other.unc / other.num))

    def __rmul__(self, other):  # defines other + self
        other = self.fixit(other, "*")
        return self.__mul__(other)

    def __imul__(self, other):
        other = self.fixit(other, "*")
        sn = self.num
        self.num *= other.num
        self.unc = self.num * (self.unc / sn + other.unc / other.num)
        self.__init__(self.num, self.unc)

    def __div__(self, other):
        other = self.fixit(other, "/")
        _div = self.num / other.num
        return uncertainNumber(_div,
                               _div * (self.unc / self.num + other.unc / other.num))

    def __rdiv__(self, other):  # defines other + self
        other = self.fixit(other, "/")
        _div = other.num / self.num
        return uncertainNumber(_div,
                               _div * (self.unc / self.num + other.unc / other.num))

    def __idiv__(self, other):
        other = self.fixit(other, "+")
        sn = self.num
        self.num /= other.num
        self.unc = self.num * (self.unc / sn + other.unc / other.num)
        self.__init__(self.num, self.unc)

    def __abs__(self):
        return abs(self.num)

    def __neg__(self):  # defines -c (c is uncertainNumber)
        return uncertainNumber(-self.num, self.unc)

    def __eq__(self, other):
        return self.num == other.num and self.unc == other.unc

    def ae(self, other):
        return (self.num + self.unc >= other.num and self.num - self.unc <= other.num) or (other.num + other.unc >= self.num and other.num - other.unc <= self.num)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "%g \u00b1 %g" % (self.num, self.unc)

    def __repr__(self):
        return 'uncertainNumber ' + str(self)

    def __pow__(self, power):
        power = self.fixit(power, "**")
        return uncertainNumber(self,)

    def __rpow__(self, base):
        base = self.fixit(base, "**")
        return

    def __ipow__(self, power):
        power = self.fixit(power, "**")
        return self.__pow__(power)

    def __gt__(self, other):
        other = self.fixit(other, ">")
        return self.num - self.unc > other.num + other.unc

    def __ge__(self, other):
        other = self.fixit(other, ">=")
        return self.num - self.unc >= other.num - other.unc

    def __lt__(self, other):
        other = self.fixit(other, "<")
        return self.num + self.unc < other.num - other.unc

    def __le__(self, other):
        other = self.fixit(other, "<=")
        return self.num + self.unc <= other.num + other.unc

    def _illegal(self, op):
        print('illegal operation "%s" for uncertain number' % op)


un = uncertainNumber

if __name__ == "__main__":
    o = un