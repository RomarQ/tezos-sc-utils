import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_0 = sp.local("utils_0", sp.len(sp.bytes('0xff')))
    utils_1 = sp.local("utils_1", 0)
    sp.for utils_2 in sp.range(0, utils_0.value):
      compute_utils_329 = sp.local("compute_utils_329", sp.slice(sp.bytes('0xff'), utils_2, 1).open_some(message = sp.unit))
      compute_utils_330 = sp.local("compute_utils_330", sp.as_nat(utils_0.value - (utils_2 + 1)) * 2)
      utils_1.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_330.value, 16, 1)
    sp.verify(utils_1.value == 255)
    utils_3 = sp.local("utils_3", sp.len(sp.bytes('0xffff')))
    utils_4 = sp.local("utils_4", 0)
    sp.for utils_5 in sp.range(0, utils_3.value):
      compute_utils_329 = sp.local("compute_utils_329", sp.slice(sp.bytes('0xffff'), utils_5, 1).open_some(message = sp.unit))
      compute_utils_330 = sp.local("compute_utils_330", sp.as_nat(utils_3.value - (utils_5 + 1)) * 2)
      utils_4.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_330.value, 16, 1)
    sp.verify(utils_4.value == 65535)

sp.add_compilation_target("test", Contract())