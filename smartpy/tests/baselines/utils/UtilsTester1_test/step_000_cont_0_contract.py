import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_19 = sp.local("utils_19", 1)
    utils_20 = sp.local("utils_20", sp.list([]))
    sp.if utils_19.value == 0:
      utils_20.value.push('0')
    sp.while utils_19.value > 0:
      utils_20.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_19.value % 10])
      utils_19.value //= 10
    utils_21 = sp.local("utils_21", sp.concat(utils_20.value))
    sp.if True:
      utils_21.value = '-' + utils_21.value
    sp.verify(utils_21.value == '-1')
    utils_22 = sp.local("utils_22", 1)
    utils_23 = sp.local("utils_23", sp.list([]))
    sp.if utils_22.value == 0:
      utils_23.value.push('0')
    sp.while utils_22.value > 0:
      utils_23.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_22.value % 10])
      utils_22.value //= 10
    utils_24 = sp.local("utils_24", sp.concat(utils_23.value))
    sp.if False:
      utils_24.value = '-' + utils_24.value
    sp.verify(utils_24.value == '1')
    sp.verify(self.string_of_int(2) == '2')
    utils_25 = sp.local("utils_25", '1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_25.value = sp.slice('1', 1, sp.as_nat(sp.len('1') - 1)).open_some(message = '')
    utils_26 = sp.local("utils_26", 0)
    sp.for utils_27 in sp.range(0, sp.len(utils_25.value)):
      utils_26.value = (10 * utils_26.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_25.value, utils_27, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_26.value *= -1
    sp.verify(utils_26.value == 1)
    utils_28 = sp.local("utils_28", '-1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_28.value = sp.slice('-1', 1, sp.as_nat(sp.len('-1') - 1)).open_some(message = '')
    utils_29 = sp.local("utils_29", 0)
    sp.for utils_30 in sp.range(0, sp.len(utils_28.value)):
      utils_29.value = (10 * utils_29.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_28.value, utils_30, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_29.value *= -1
    sp.verify(utils_29.value == (-1))
    sp.verify(self.int_of_string('2') == 2)
    utils_0 = sp.local("utils_0", sp.len(sp.bytes('0x0100')))
    utils_1 = sp.local("utils_1", 0)
    sp.for utils_2 in sp.range(0, utils_0.value):
      compute_utils_329 = sp.local("compute_utils_329", sp.slice(sp.bytes('0x0100'), utils_2, 1).open_some(message = sp.unit))
      compute_utils_330 = sp.local("compute_utils_330", sp.as_nat(utils_0.value - (utils_2 + 1)) * 2)
      utils_1.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_330.value, 16, 1)
    sp.verify(utils_1.value == 256)
    sp.verify(self.int_of_bytes(sp.bytes('0x0100')) == 256)
    utils_31 = sp.local("utils_31", 0)
    utils_32 = sp.local("utils_32", sp.list([]))
    sp.for utils_33 in sp.range(0, sp.len('a b')):
      sp.if sp.slice('a b', utils_33, 1).open_some() == ' ':
        utils_32.value.push(sp.slice('a b', utils_31.value, sp.as_nat(utils_33 - utils_31.value)).open_some())
        utils_31.value = utils_33 + 1
    sp.if sp.len('a b') > 0:
      utils_32.value.push(sp.slice('a b', utils_31.value, sp.as_nat(sp.len('a b') - utils_31.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_32.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a', 'b']), sp.TList(sp.TString))))
    utils_34 = sp.local("utils_34", 0)
    utils_35 = sp.local("utils_35", sp.list([]))
    sp.for utils_36 in sp.range(0, sp.len('b,a')):
      sp.if sp.slice('b,a', utils_36, 1).open_some() == ',':
        utils_35.value.push(sp.slice('b,a', utils_34.value, sp.as_nat(utils_36 - utils_34.value)).open_some())
        utils_34.value = utils_36 + 1
    sp.if sp.len('b,a') > 0:
      utils_35.value.push(sp.slice('b,a', utils_34.value, sp.as_nat(sp.len('b,a') - utils_34.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_35.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['b', 'a']), sp.TList(sp.TString))))
    sp.verify(sp.pack(sp.set_type_expr(self.string_split(sp.record(separator = ',,', text = 'a,b')), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a,b']), sp.TList(sp.TString))))
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('a', 'abc') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('b', 'abc') == False)
    sp.verify(self.string_starts_with(sp.record(prefix = 'a', text = 'abc')) == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'c') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'b') == False)
    sp.verify(self.string_ends_with(sp.record(postfix = 'c', text = 'abc')) == True)
    utils_37_hist = sp.local("utils_37_hist", {})
    sp.for utils_38_x in sp.list([1, 2, 3, 4, 5]):
      sp.if utils_37_hist.value.contains(utils_38_x):
        utils_37_hist.value[utils_38_x] += 1
      sp.else:
        utils_37_hist.value[utils_38_x] = 1
    compute_smartpy_utils_90 = sp.local("compute_smartpy_utils_90", sp.len(sp.list([1, 2, 3, 4, 5])))
    utils_39_result = sp.local("utils_39_result", 0)
    utils_40_half = sp.local("utils_40_half", compute_smartpy_utils_90.value // 2)
    utils_41_use_average = sp.local("utils_41_use_average", (utils_40_half.value * 2) == compute_smartpy_utils_90.value)
    utils_42_i = sp.local("utils_42_i", 0)
    sp.for utils_43_x in utils_37_hist.value.items():
      sp.if utils_41_use_average.value:
        sp.if utils_42_i.value < utils_40_half.value:
          utils_39_result.value = utils_43_x.key
          utils_42_i.value += utils_43_x.value
          sp.if utils_42_i.value > utils_40_half.value:
            utils_41_use_average.value = False
        sp.else:
          utils_39_result.value += utils_43_x.key
          utils_39_result.value //= 2
          utils_41_use_average.value = False
          utils_42_i.value += utils_43_x.value
      sp.else:
        sp.if utils_42_i.value <= utils_40_half.value:
          utils_39_result.value = utils_43_x.key
          utils_42_i.value += utils_43_x.value
    sp.verify(utils_39_result.value == 3)
    utils_44_hist = sp.local("utils_44_hist", {})
    sp.for utils_45_x in sp.list([1, 2, 2, 3]):
      sp.if utils_44_hist.value.contains(utils_45_x):
        utils_44_hist.value[utils_45_x] += 1
      sp.else:
        utils_44_hist.value[utils_45_x] = 1
    compute_smartpy_utils_90i = sp.local("compute_smartpy_utils_90i", sp.len(sp.list([1, 2, 2, 3])))
    utils_46_result = sp.local("utils_46_result", 0)
    utils_47_half = sp.local("utils_47_half", compute_smartpy_utils_90i.value // 2)
    utils_48_use_average = sp.local("utils_48_use_average", (utils_47_half.value * 2) == compute_smartpy_utils_90i.value)
    utils_49_i = sp.local("utils_49_i", 0)
    sp.for utils_50_x in utils_44_hist.value.items():
      sp.if utils_48_use_average.value:
        sp.if utils_49_i.value < utils_47_half.value:
          utils_46_result.value = utils_50_x.key
          utils_49_i.value += utils_50_x.value
          sp.if utils_49_i.value > utils_47_half.value:
            utils_48_use_average.value = False
        sp.else:
          utils_46_result.value += utils_50_x.key
          utils_46_result.value //= 2
          utils_48_use_average.value = False
          utils_49_i.value += utils_50_x.value
      sp.else:
        sp.if utils_49_i.value <= utils_47_half.value:
          utils_46_result.value = utils_50_x.key
          utils_49_i.value += utils_50_x.value
    sp.verify(utils_46_result.value == 2)
    sp.verify(self.math_median(sp.list([1, 2, 2, 5])) == 2)
    compute_utils_118 = sp.local("compute_utils_118", 3 - sp.len(sp.bytes('0x11')))
    utils_3_bytes = sp.local("utils_3_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_3_bytes.value) < sp.as_nat(compute_utils_118.value):
      utils_3_bytes.value = sp.bytes('0x00') + utils_3_bytes.value
    sp.verify((utils_3_bytes.value + sp.bytes('0x11')) == sp.bytes('0x000011'))
    compute_utils_126 = sp.local("compute_utils_126", 3 - sp.len(sp.bytes('0x11')))
    utils_4_bytes = sp.local("utils_4_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_4_bytes.value) < sp.as_nat(compute_utils_126.value):
      utils_4_bytes.value = sp.bytes('0x00') + utils_4_bytes.value
    sp.verify((sp.bytes('0x11') + utils_4_bytes.value) == sp.bytes('0x110000'))
    sp.verify(True, 'NUMBER_TOO_BIG')
    utils_51_bytes = sp.local("utils_51_bytes", sp.bytes('0x'))
    utils_52_value = sp.local("utils_52_value", 54)
    sp.while utils_52_value.value != 0:
      utils_51_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_52_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_51_bytes.value
      utils_52_value.value = utils_52_value.value >> 8
    sp.verify(utils_51_bytes.value == sp.bytes('0x36'))
    sp.verify(sp.slice(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'), 6, sp.as_nat(sp.len(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')) - 6)).open_some(message = 'Could not encode string to bytes.') == sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858'))
    sp.verify(sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')) < 28948022309329048855892746252171976963317496166410141009864396001978282409984, 'NUMBER_TOO_BIG')
    utils_53_bytes = sp.local("utils_53_bytes", sp.bytes('0x'))
    utils_54_value = sp.local("utils_54_value", sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')))
    sp.while utils_54_value.value != 0:
      utils_53_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_54_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_53_bytes.value
      utils_54_value.value = utils_54_value.value >> 8
    lengthBytes = sp.local("lengthBytes", utils_53_bytes.value)
    sp.while sp.len(lengthBytes.value) < 4:
      lengthBytes.value = sp.bytes('0x00') + lengthBytes.value
    sp.verify(sp.unpack(sp.concat(sp.list([sp.bytes('0x05'), sp.bytes('0x01'), lengthBytes.value, sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')])), sp.TString).open_some(message = 'Could not decode bytes to string') == 'TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    sp.verify(((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC'))) == False)
    sp.verify((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')))

  @sp.private_lambda()
  def int_of_bytes(_x0):
    utils_0 = sp.local("utils_0", sp.len(_x0))
    utils_1 = sp.local("utils_1", 0)
    sp.for utils_2 in sp.range(0, utils_0.value):
      compute_smartpy_utils_329 = sp.local("compute_smartpy_utils_329", sp.slice(_x0, utils_2, 1).open_some(message = sp.unit))
      compute_smartpy_utils_330 = sp.local("compute_smartpy_utils_330", sp.as_nat(utils_0.value - (utils_2 + 1)) * 2)
      utils_1.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_smartpy_utils_329.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_smartpy_utils_330.value, 16, 1)
    sp.result(utils_1.value)

  @sp.private_lambda()
  def int_of_string(_x1):
    utils_3 = sp.local("utils_3", _x1)
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_3.value = sp.slice(_x1, 1, sp.as_nat(sp.len(_x1) - 1)).open_some(message = '')
    utils_4 = sp.local("utils_4", 0)
    sp.for utils_5 in sp.range(0, sp.len(utils_3.value)):
      utils_4.value = (10 * utils_4.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_3.value, utils_5, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_4.value *= -1
    sp.result(utils_4.value)

  @sp.private_lambda()
  def math_median(_x2):
    utils_6_hist = sp.local("utils_6_hist", {})
    sp.for utils_7_x in _x2:
      sp.if utils_6_hist.value.contains(utils_7_x):
        utils_6_hist.value[utils_7_x] += 1
      sp.else:
        utils_6_hist.value[utils_7_x] = 1
    compute_smartpy_utils_90 = sp.local("compute_smartpy_utils_90", sp.len(_x2))
    utils_8_result = sp.local("utils_8_result", 0)
    utils_9_half = sp.local("utils_9_half", compute_smartpy_utils_90.value // 2)
    utils_10_use_average = sp.local("utils_10_use_average", (utils_9_half.value * 2) == compute_smartpy_utils_90.value)
    utils_11_i = sp.local("utils_11_i", 0)
    sp.for utils_12_x in utils_6_hist.value.items():
      sp.if utils_10_use_average.value:
        sp.if utils_11_i.value < utils_9_half.value:
          utils_8_result.value = utils_12_x.key
          utils_11_i.value += utils_12_x.value
          sp.if utils_11_i.value > utils_9_half.value:
            utils_10_use_average.value = False
        sp.else:
          utils_8_result.value += utils_12_x.key
          utils_8_result.value //= 2
          utils_10_use_average.value = False
          utils_11_i.value += utils_12_x.value
      sp.else:
        sp.if utils_11_i.value <= utils_9_half.value:
          utils_8_result.value = utils_12_x.key
          utils_11_i.value += utils_12_x.value
    sp.result(utils_8_result.value)

  @sp.private_lambda()
  def math_pow(_x3):
    sp.result(sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(_x3.exponent, _x3.base, 1))

  @sp.private_lambda()
  def string_ends_with(_x4):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")(_x4.text, _x4.postfix))

  @sp.private_lambda()
  def string_of_int(_x5):
    utils_13 = sp.local("utils_13", abs(_x5))
    utils_14 = sp.local("utils_14", sp.list([]))
    sp.if utils_13.value == 0:
      utils_14.value.push('0')
    sp.while utils_13.value > 0:
      utils_14.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_13.value % 10])
      utils_13.value //= 10
    utils_15 = sp.local("utils_15", sp.concat(utils_14.value))
    sp.if _x5 < 0:
      utils_15.value = '-' + utils_15.value
    sp.result(utils_15.value)

  @sp.private_lambda()
  def string_split(_x6):
    utils_16 = sp.local("utils_16", 0)
    utils_17 = sp.local("utils_17", sp.list([]))
    sp.for utils_18 in sp.range(0, sp.len(_x6.text)):
      sp.if sp.slice(_x6.text, utils_18, 1).open_some() == _x6.separator:
        utils_17.value.push(sp.slice(_x6.text, utils_16.value, sp.as_nat(utils_18 - utils_16.value)).open_some())
        utils_16.value = utils_18 + 1
    sp.if sp.len(_x6.text) > 0:
      utils_17.value.push(sp.slice(_x6.text, utils_16.value, sp.as_nat(sp.len(_x6.text) - utils_16.value)).open_some())
    sp.result(utils_17.value.rev())

  @sp.private_lambda()
  def string_starts_with(_x7):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")(_x7.prefix, _x7.text))

sp.add_compilation_target("test", Contract())