import smartpy as sp

Utils = sp.io.import_script_from_url("file:smartpy/utils.py")

class Test(sp.Contract):
    def __init__(self):
        self.init()

    @sp.entry_point
    def test(self):
        sp.verify(Utils.Int.of_bytes(sp.bytes("0xFF")) == 255)
        sp.verify(Utils.Int.of_bytes(sp.bytes("0xFFFF")) == 65535)

@sp.add_test(name = "issue_1_test")
def test1():
    scenario = sp.test_scenario()

    c1 = Test()
    scenario += c1

    c1.test()
