import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_20 = sp.local("utils_20", 1)
    utils_21 = sp.local("utils_21", sp.list([]))
    sp.if utils_20.value == 0:
      utils_21.value.push('0')
    sp.while utils_20.value > 0:
      utils_21.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_20.value % 10])
      utils_20.value //= 10
    utils_22 = sp.local("utils_22", sp.concat(utils_21.value))
    sp.if True:
      utils_22.value = '-' + utils_22.value
    sp.verify(utils_22.value == '-1')
    utils_23 = sp.local("utils_23", 1)
    utils_24 = sp.local("utils_24", sp.list([]))
    sp.if utils_23.value == 0:
      utils_24.value.push('0')
    sp.while utils_23.value > 0:
      utils_24.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_23.value % 10])
      utils_23.value //= 10
    utils_25 = sp.local("utils_25", sp.concat(utils_24.value))
    sp.if False:
      utils_25.value = '-' + utils_25.value
    sp.verify(utils_25.value == '1')
    sp.verify(self.string_of_int(2) == '2')
    utils_26 = sp.local("utils_26", '1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_26.value = sp.slice('1', 1, sp.as_nat(sp.len('1') - 1)).open_some(message = '')
    utils_27 = sp.local("utils_27", 0)
    sp.for utils_28 in sp.range(0, sp.len(utils_26.value)):
      utils_27.value = (10 * utils_27.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_26.value, utils_28, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_27.value *= -1
    sp.verify(utils_27.value == 1)
    utils_29 = sp.local("utils_29", '-1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_29.value = sp.slice('-1', 1, sp.as_nat(sp.len('-1') - 1)).open_some(message = '')
    utils_30 = sp.local("utils_30", 0)
    sp.for utils_31 in sp.range(0, sp.len(utils_29.value)):
      utils_30.value = (10 * utils_30.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_29.value, utils_31, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_30.value *= -1
    sp.verify(utils_30.value == (-1))
    sp.verify(self.int_of_string('2') == 2)
    compute_utils_326 = sp.local("compute_utils_326", sp.len(sp.bytes('0x0100')))
    utils_32 = sp.local("utils_32", 0)
    sp.for utils_33 in sp.range(0, compute_utils_326.value):
      compute_utils_329 = sp.local("compute_utils_329", sp.slice(sp.bytes('0x0100'), utils_33, 1).open_some(message = sp.unit))
      compute_utils_330 = sp.local("compute_utils_330", sp.as_nat(compute_utils_326.value - (utils_33 + 1)) * 2)
      utils_32.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_330.value, 16, 1)
    sp.verify(utils_32.value == 256)
    sp.verify(self.int_of_bytes(sp.bytes('0x0100')) == 256)
    utils_34 = sp.local("utils_34", 0)
    utils_35 = sp.local("utils_35", sp.list([]))
    sp.for utils_36 in sp.range(0, sp.len('a b')):
      sp.if sp.slice('a b', utils_36, 1).open_some() == ' ':
        utils_35.value.push(sp.slice('a b', utils_34.value, sp.as_nat(utils_36 - utils_34.value)).open_some())
        utils_34.value = utils_36 + 1
    sp.if sp.len('a b') > 0:
      utils_35.value.push(sp.slice('a b', utils_34.value, sp.as_nat(sp.len('a b') - utils_34.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_35.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a', 'b']), sp.TList(sp.TString))))
    utils_37 = sp.local("utils_37", 0)
    utils_38 = sp.local("utils_38", sp.list([]))
    sp.for utils_39 in sp.range(0, sp.len('b,a')):
      sp.if sp.slice('b,a', utils_39, 1).open_some() == ',':
        utils_38.value.push(sp.slice('b,a', utils_37.value, sp.as_nat(utils_39 - utils_37.value)).open_some())
        utils_37.value = utils_39 + 1
    sp.if sp.len('b,a') > 0:
      utils_38.value.push(sp.slice('b,a', utils_37.value, sp.as_nat(sp.len('b,a') - utils_37.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_38.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['b', 'a']), sp.TList(sp.TString))))
    sp.verify(sp.pack(sp.set_type_expr(self.string_split(sp.record(separator = ',,', text = 'a,b')), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a,b']), sp.TList(sp.TString))))
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('a', 'abc') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('b', 'abc') == False)
    sp.verify(self.string_starts_with(sp.record(prefix = 'a', text = 'abc')) == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'c') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'b') == False)
    sp.verify(self.string_ends_with(sp.record(postfix = 'c', text = 'abc')) == True)
    utils_40_hist = sp.local("utils_40_hist", {})
    sp.for utils_41_x in sp.list([1, 2, 3, 4, 5]):
      sp.if utils_40_hist.value.contains(utils_41_x):
        utils_40_hist.value[utils_41_x] += 1
      sp.else:
        utils_40_hist.value[utils_41_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(sp.list([1, 2, 3, 4, 5])))
    utils_42_result = sp.local("utils_42_result", 0)
    utils_43_half = sp.local("utils_43_half", compute_utils_90.value // 2)
    utils_44_use_average = sp.local("utils_44_use_average", (utils_43_half.value * 2) == compute_utils_90.value)
    utils_45_i = sp.local("utils_45_i", 0)
    sp.for utils_46_x in utils_40_hist.value.items():
      sp.if utils_44_use_average.value:
        sp.if utils_45_i.value < utils_43_half.value:
          utils_42_result.value = utils_46_x.key
          utils_45_i.value += utils_46_x.value
          sp.if utils_45_i.value > utils_43_half.value:
            utils_44_use_average.value = False
        sp.else:
          utils_42_result.value += utils_46_x.key
          utils_42_result.value //= 2
          utils_44_use_average.value = False
          utils_45_i.value += utils_46_x.value
      sp.else:
        sp.if utils_45_i.value <= utils_43_half.value:
          utils_42_result.value = utils_46_x.key
          utils_45_i.value += utils_46_x.value
    sp.verify(utils_42_result.value == 3)
    utils_47_hist = sp.local("utils_47_hist", {})
    sp.for utils_48_x in sp.list([1, 2, 2, 3]):
      sp.if utils_47_hist.value.contains(utils_48_x):
        utils_47_hist.value[utils_48_x] += 1
      sp.else:
        utils_47_hist.value[utils_48_x] = 1
    compute_utils_90i = sp.local("compute_utils_90i", sp.len(sp.list([1, 2, 2, 3])))
    utils_49_result = sp.local("utils_49_result", 0)
    utils_50_half = sp.local("utils_50_half", compute_utils_90i.value // 2)
    utils_51_use_average = sp.local("utils_51_use_average", (utils_50_half.value * 2) == compute_utils_90i.value)
    utils_52_i = sp.local("utils_52_i", 0)
    sp.for utils_53_x in utils_47_hist.value.items():
      sp.if utils_51_use_average.value:
        sp.if utils_52_i.value < utils_50_half.value:
          utils_49_result.value = utils_53_x.key
          utils_52_i.value += utils_53_x.value
          sp.if utils_52_i.value > utils_50_half.value:
            utils_51_use_average.value = False
        sp.else:
          utils_49_result.value += utils_53_x.key
          utils_49_result.value //= 2
          utils_51_use_average.value = False
          utils_52_i.value += utils_53_x.value
      sp.else:
        sp.if utils_52_i.value <= utils_50_half.value:
          utils_49_result.value = utils_53_x.key
          utils_52_i.value += utils_53_x.value
    sp.verify(utils_49_result.value == 2)
    sp.verify(self.math_median(sp.list([1, 2, 2, 5])) == 2)
    compute_utils_118 = sp.local("compute_utils_118", 3 - sp.len(sp.bytes('0x11')))
    utils_54_bytes = sp.local("utils_54_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_54_bytes.value) < sp.as_nat(compute_utils_118.value):
      utils_54_bytes.value = sp.bytes('0x00') + utils_54_bytes.value
    sp.verify((utils_54_bytes.value + sp.bytes('0x11')) == sp.bytes('0x000011'))
    compute_utils_126 = sp.local("compute_utils_126", 3 - sp.len(sp.bytes('0x11')))
    utils_55_bytes = sp.local("utils_55_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_55_bytes.value) < sp.as_nat(compute_utils_126.value):
      utils_55_bytes.value = sp.bytes('0x00') + utils_55_bytes.value
    sp.verify((sp.bytes('0x11') + utils_55_bytes.value) == sp.bytes('0x110000'))
    sp.verify(True, 'NUMBER_TOO_BIG')
    utils_56_bytes = sp.local("utils_56_bytes", sp.bytes('0x'))
    utils_57_value = sp.local("utils_57_value", 54)
    sp.while utils_57_value.value != 0:
      utils_56_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_57_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_56_bytes.value
      utils_57_value.value = utils_57_value.value >> 8
    sp.verify(utils_56_bytes.value == sp.bytes('0x36'))
    sp.verify(sp.slice(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'), 6, sp.as_nat(sp.len(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')) - 6)).open_some(message = 'Could not encode string to bytes.') == sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858'))
    sp.verify(sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')) < 28948022309329048855892746252171976963317496166410141009864396001978282409984, 'NUMBER_TOO_BIG')
    utils_58_bytes = sp.local("utils_58_bytes", sp.bytes('0x'))
    utils_59_value = sp.local("utils_59_value", sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')))
    sp.while utils_59_value.value != 0:
      utils_58_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_59_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_58_bytes.value
      utils_59_value.value = utils_59_value.value >> 8
    lengthBytes = sp.local("lengthBytes", utils_58_bytes.value)
    sp.while sp.len(lengthBytes.value) < 4:
      lengthBytes.value = sp.bytes('0x00') + lengthBytes.value
    sp.verify(sp.unpack(sp.concat(sp.list([sp.bytes('0x05'), sp.bytes('0x01'), lengthBytes.value, sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')])), sp.TString).open_some(message = 'Could not decode bytes to string') == 'TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    sp.verify(((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC'))) == False)
    sp.verify((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')))

  @sp.private_lambda()
  def int_of_bytes(_x0):
    compute_smartpy_utils_326 = sp.local("compute_smartpy_utils_326", sp.len(_x0))
    utils_54 = sp.local("utils_54", 0)
    sp.for utils_55 in sp.range(0, compute_smartpy_utils_326.value):
      compute_smartpy_utils_329 = sp.local("compute_smartpy_utils_329", sp.slice(_x0, utils_55, 1).open_some(message = sp.unit))
      compute_smartpy_utils_330 = sp.local("compute_smartpy_utils_330", sp.as_nat(compute_smartpy_utils_326.value - (utils_55 + 1)) * 2)
      utils_54.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_smartpy_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_smartpy_utils_330.value, 16, 1)
    sp.result(utils_54.value)

  @sp.private_lambda()
  def int_of_string(_x1):
    utils_4 = sp.local("utils_4", _x1)
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_4.value = sp.slice(_x1, 1, sp.as_nat(sp.len(_x1) - 1)).open_some(message = '')
    utils_5 = sp.local("utils_5", 0)
    sp.for utils_6 in sp.range(0, sp.len(utils_4.value)):
      utils_5.value = (10 * utils_5.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_4.value, utils_6, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_5.value *= -1
    sp.result(utils_5.value)

  @sp.private_lambda()
  def math_median(_x2):
    utils_7_hist = sp.local("utils_7_hist", {})
    sp.for utils_8_x in _x2:
      sp.if utils_7_hist.value.contains(utils_8_x):
        utils_7_hist.value[utils_8_x] += 1
      sp.else:
        utils_7_hist.value[utils_8_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(_x2))
    utils_9_result = sp.local("utils_9_result", 0)
    utils_10_half = sp.local("utils_10_half", compute_utils_90.value // 2)
    utils_11_use_average = sp.local("utils_11_use_average", (utils_10_half.value * 2) == compute_utils_90.value)
    utils_12_i = sp.local("utils_12_i", 0)
    sp.for utils_13_x in utils_7_hist.value.items():
      sp.if utils_11_use_average.value:
        sp.if utils_12_i.value < utils_10_half.value:
          utils_9_result.value = utils_13_x.key
          utils_12_i.value += utils_13_x.value
          sp.if utils_12_i.value > utils_10_half.value:
            utils_11_use_average.value = False
        sp.else:
          utils_9_result.value += utils_13_x.key
          utils_9_result.value //= 2
          utils_11_use_average.value = False
          utils_12_i.value += utils_13_x.value
      sp.else:
        sp.if utils_12_i.value <= utils_10_half.value:
          utils_9_result.value = utils_13_x.key
          utils_12_i.value += utils_13_x.value
    sp.result(utils_9_result.value)

  @sp.private_lambda()
  def math_pow(_x3):
    sp.result(sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(_x3.exponent, _x3.base, 1))

  @sp.private_lambda()
  def string_ends_with(_x4):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")(_x4.text, _x4.postfix))

  @sp.private_lambda()
  def string_of_int(_x5):
    utils_14 = sp.local("utils_14", abs(_x5))
    utils_15 = sp.local("utils_15", sp.list([]))
    sp.if utils_14.value == 0:
      utils_15.value.push('0')
    sp.while utils_14.value > 0:
      utils_15.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_14.value % 10])
      utils_14.value //= 10
    utils_16 = sp.local("utils_16", sp.concat(utils_15.value))
    sp.if _x5 < 0:
      utils_16.value = '-' + utils_16.value
    sp.result(utils_16.value)

  @sp.private_lambda()
  def string_split(_x6):
    utils_17 = sp.local("utils_17", 0)
    utils_18 = sp.local("utils_18", sp.list([]))
    sp.for utils_19 in sp.range(0, sp.len(_x6.text)):
      sp.if sp.slice(_x6.text, utils_19, 1).open_some() == _x6.separator:
        utils_18.value.push(sp.slice(_x6.text, utils_17.value, sp.as_nat(utils_19 - utils_17.value)).open_some())
        utils_17.value = utils_19 + 1
    sp.if sp.len(_x6.text) > 0:
      utils_18.value.push(sp.slice(_x6.text, utils_17.value, sp.as_nat(sp.len(_x6.text) - utils_17.value)).open_some())
    sp.result(utils_18.value.rev())

  @sp.private_lambda()
  def string_starts_with(_x7):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")(_x7.prefix, _x7.text))

sp.add_compilation_target("test", Contract())