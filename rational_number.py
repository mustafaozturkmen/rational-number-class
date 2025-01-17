class RationalNumber:
    def __init__(self, numerator, denominator):
        if isinstance(numerator, float):
            temp = 10 ** len(str(numerator).split('.')[1])
            numerator = int(numerator * temp)
            denominator = temp * denominator

        if isinstance(denominator, float):
            temp = 10 ** len(str(denominator).split('.')[1])
            denominator = int(temp * denominator)
            numerator = numerator * temp

        if not (isinstance(denominator, int) and isinstance(numerator, int)):
            raise TypeError(f"Expected types for numerator and denominator are 'float' and 'int'")

        # Keep denominator nonzero and positive
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator

        self.numerator = numerator
        self.denominator = denominator

        self.simplify()

    def __add__(self, other):
        other = self._convert_to_rational(other)
        if not isinstance(other, RationalNumber):
            raise TypeError(f"unsupported operand type(s) for +: 'rational_number' and '{type(other).__name__}'")
        new_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __mul__(self, other):
        other = self._convert_to_rational(other)
        if not isinstance(other, RationalNumber):
            raise TypeError(f"unsupported operand type(s) for *: 'rational_number' and '{type(other).__name__}'")
        new_numerator = self.numerator*other.numerator
        new_denominator = self.denominator*other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __sub__(self, other):
        other = self._convert_to_rational(other)
        if not isinstance(other, RationalNumber):
            raise TypeError(f"unsupported operand type(s) for -: 'rational_number' and '{type(other).__name__}'")
        return self + other*RationalNumber(-1, 1)

    def __truediv__(self, other):
        other = self._convert_to_rational(other)
        if not isinstance(other, RationalNumber):
            raise TypeError(f"unsupported operand type(s) for /: 'rational_number' and '{type(other).__name__}'")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a RationalNumber with a numerator of zero.")
        new_numerator = self.numerator*other.denominator
        new_denominator = self.denominator*other.numerator
        return RationalNumber(new_numerator, new_denominator)

    def _convert_to_rational(self, value):
        if isinstance(value, int):
            return RationalNumber(value, 1)
        if isinstance(value, float):
            denominator = 10 ** len(str(value).split('.')[1])
            numerator = int(value * denominator)
            return RationalNumber(numerator, denominator)
        return value

    def simplify(self):
        gcd = self.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = self.numerator//gcd
        self.denominator = self.denominator//gcd

    def gcd(self, a, b):
        max_num = max(a, b)
        min_num = min(a, b)
        if min_num == 0:
            return max_num
        diff = max_num - (max_num//min_num)*min_num
        return self.gcd(diff, min_num)

    def __int__(self):
        return int(self.numerator//self.denominator)

    def __float__(self):
        return self.numerator/self.denominator

    def __str__(self):
        return f"{int(self.numerator)}/{int(self.denominator)}"
