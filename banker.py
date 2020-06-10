from migen.build.generic_platform import *
from migen.build.lattice import LatticePlatform


_io = [
    ("clk25", 0, Pins("K9"), IOStandard("LVCMOS33")),

    ("user_led", 0, Pins("H3"), IOStandard("LVCMOS25")),

    # ("cbsel", 0, Pins("K11 P13"), IOStandard("LVCMOS33")),
    # ("cfg_reload", 0, Pins("R16"), IOStandard("LVCMOS33")),

    # ("i2c", 0,
    #     Subsignal("scl", Pins("M12")),
    #     Subsignal("sda", Pins("T16")),
    #     IOStandard("LVCMOS33"),
    # ),

    # ("spiflash", 0,
    #     Subsignal("cs_n", Pins("R12")),
    #     Subsignal("sck", Pins("R11")),
    #     Subsignal("mosi", Pins("P12")),
    #     Subsignal("miso", Pins("P11")),
    #     IOStandard("LVCMOS33"),
    # ),

    # # yosys/nextpnr get confused if these are not broken up
    # ("eem0_n", 0, Pins("J5")),
    # ("eem0_p", 0, Pins("G1")),
    # ("eem0_n", 1, Pins("K4")),
    # ("eem0_p", 1, Pins("M1")),
    # ("eem0_n", 2, Pins("K1")),
    # ("eem0_p", 2, Pins("K3")),
    # ("eem0_n", 3, Pins("J4")),
    # ("eem0_p", 3, Pins("H2")),
    # ("eem0_n", 4, Pins("H4")),
    # ("eem0_p", 4, Pins("G2")),
    # ("eem0_n", 5, Pins("G4")),
    # ("eem0_p", 5, Pins("E3")),
    # ("eem0_n", 6, Pins("F4")),
    # ("eem0_p", 6, Pins("D2")),
    # ("eem0_n", 7, Pins("E4")),
    # ("eem0_p", 7, Pins("B2")),
    # ("eem1_n", 0, Pins("J3")),
    # ("eem1_p", 0, Pins("H1")),
    # ("eem1_n", 1, Pins("L4")),
    # ("eem1_p", 1, Pins("L1")),
    # ("eem1_n", 2, Pins("J2")),
    # ("eem1_p", 2, Pins("J1")),
    # ("eem1_n", 3, Pins("H3")),
    # ("eem1_p", 3, Pins("F2")),
    # ("eem1_n", 4, Pins("H5")),
    # ("eem1_p", 4, Pins("E2")),
    # ("eem1_n", 5, Pins("G5")),
    # ("eem1_p", 5, Pins("D1")),
    # ("eem1_n", 6, Pins("C1")),
    # ("eem1_p", 6, Pins("C2")),
    # ("eem1_n", 7, Pins("F5")),
    # ("eem1_p", 7, Pins("B1")),
]


class Platform(LatticePlatform):
    default_clk_name = "clk25"
    default_clk_period = 40.

    def __init__(self):
        LatticePlatform.__init__(self, "ice40-hx8k-ct256", _io,
                                 toolchain="icestorm")
