# If the design does not create a "sync" clock domain, it is created by the nMigen build system
# using the platform default clock (and default reset, if any).

from nmigen import *
from nmigen_boards.ulx3s import *


class Blinky(Elaboratable):
    def elaborate(self, platform):
        led   = platform.request("led", 1)
        timer = Signal(26)

        m = Module()
        m.d.sync += timer.eq(timer + 1)
        m.d.comb += led.o.eq(timer[-1])
        return m


if __name__ == "__main__":
    platform = ULX3S_85F_Platform()
    platform.build(Blinky(), do_program=True)
