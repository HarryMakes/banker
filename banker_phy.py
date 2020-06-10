from migen import *


class Banker(Module):
    def __init__(self, platform):
        # cd_sys = ClockDomain("sys")
        # self.clock_domains += cd_sys
        # platform.add_period_constraint(cd_sys.clk, t_clk*link.n_div)

        blinker = Signal(25)
        self.comb += [
            platform.request("user_led", 0).eq(blinker[24])
        ]
        self.sync += [
            blinker.eq(blinker + 1)
        ]


if __name__ == "__main__":
    from banker import Platform
    platform = Platform()
    banker = Banker(platform)
    platform.build(banker, build_name="banker")
