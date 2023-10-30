
"""
@Author = virus
@Version = 1.0.0
"""

class Zettabyte(int):
    def __init__(self, i: int):
        self.i = i

    def to_bit(self):
        return self * 8_000_000_000_000_000_000_000

    def to_byte(self):
        return self * 1_000_000_000_000_000_000_000

    def to_kilobit(self):
        return self * 8_000_000_000_000_000_000

    def to_kilobyte(self):
        return self * 8_000_000_000_000_000

    def to_megabit(self):
        return self * 8_000_000_000_000_000

    def to_megabyte(self):
        return self * 8_000_000_000_000

    def to_gigabit(self):
        return self * 8_000_000_000

    def to_gigabyte(self):
        return self * 8_000_000

    def to_terabit(self):
        return self * 8_000

    def to_terabyte(self):
        return self * 1_000

    def to_petabit(self):
        return self / 125

    def to_petabyte(self):
        return self / 125_000

    def to_exabit(self):
        return self / 125_000_000

    def to_exabyte(self):
        return self / 125_000_000_000

    def to_zettabit(self):
        return self * 8

    def to_yottabit(self):
        return self * 1_000

    def to_yottabyte(self):
        return self / 1_000