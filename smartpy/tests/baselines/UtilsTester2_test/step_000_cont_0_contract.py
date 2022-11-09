import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_18 = sp.local("utils_18", 1)
    utils_19 = sp.local("utils_19", sp.list([]))
    sp.if utils_18.value == 0:
      utils_19.value.push('0')
    sp.while utils_18.value > 0:
      utils_19.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_18.value % 10])
      utils_18.value //= 10
    utils_20 = sp.local("utils_20", sp.concat(utils_19.value))
    sp.if True:
      utils_20.value = '-' + utils_20.value
    sp.verify(utils_20.value == '-1')
    utils_21 = sp.local("utils_21", 1)
    utils_22 = sp.local("utils_22", sp.list([]))
    sp.if utils_21.value == 0:
      utils_22.value.push('0')
    sp.while utils_21.value > 0:
      utils_22.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_21.value % 10])
      utils_21.value //= 10
    utils_23 = sp.local("utils_23", sp.concat(utils_22.value))
    sp.if False:
      utils_23.value = '-' + utils_23.value
    sp.verify(utils_23.value == '1')
    sp.verify(self.string_of_int(2) == '2')
    utils_24 = sp.local("utils_24", '1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_24.value = sp.slice('1', 1, sp.as_nat(sp.len('1') - 1)).open_some(message = '')
    utils_25 = sp.local("utils_25", 0)
    sp.for utils_26 in sp.range(0, sp.len(utils_24.value)):
      utils_25.value = (10 * utils_25.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_24.value, utils_26, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_25.value *= -1
    sp.verify(utils_25.value == 1)
    utils_27 = sp.local("utils_27", '-1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_27.value = sp.slice('-1', 1, sp.as_nat(sp.len('-1') - 1)).open_some(message = '')
    utils_28 = sp.local("utils_28", 0)
    sp.for utils_29 in sp.range(0, sp.len(utils_27.value)):
      utils_28.value = (10 * utils_28.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_27.value, utils_29, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_28.value *= -1
    sp.verify(utils_28.value == (-1))
    sp.verify(self.int_of_string('2') == 2)
    compute_utils_309 = sp.local("compute_utils_309", sp.len(sp.bytes('0x0100')))
    utils_30 = sp.local("utils_30", 0)
    sp.for utils_31 in sp.range(0, compute_utils_309.value):
      compute_utils_312 = sp.local("compute_utils_312", sp.slice(sp.bytes('0x0100'), utils_31, 1).open_some(message = sp.unit))
      compute_utils_313 = sp.local("compute_utils_313", sp.as_nat(compute_utils_309.value - (utils_31 + 1)) * 2)
      utils_30.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_312.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_313.value, 16, 1)
    sp.verify(utils_30.value == 256)
    sp.verify(self.int_of_bytes(sp.bytes('0x0100')) == 256)
    utils_32 = sp.local("utils_32", 0)
    utils_33 = sp.local("utils_33", sp.list([]))
    sp.for utils_34 in sp.range(0, sp.len('a b')):
      sp.if sp.slice('a b', utils_34, 1).open_some() == ' ':
        utils_33.value.push(sp.slice('a b', utils_32.value, sp.as_nat(utils_34 - utils_32.value)).open_some())
        utils_32.value = utils_34 + 1
    sp.if sp.len('a b') > 0:
      utils_33.value.push(sp.slice('a b', utils_32.value, sp.as_nat(sp.len('a b') - utils_32.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_33.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a', 'b']), sp.TList(sp.TString))))
    utils_35 = sp.local("utils_35", 0)
    utils_36 = sp.local("utils_36", sp.list([]))
    sp.for utils_37 in sp.range(0, sp.len('b,a')):
      sp.if sp.slice('b,a', utils_37, 1).open_some() == ',':
        utils_36.value.push(sp.slice('b,a', utils_35.value, sp.as_nat(utils_37 - utils_35.value)).open_some())
        utils_35.value = utils_37 + 1
    sp.if sp.len('b,a') > 0:
      utils_36.value.push(sp.slice('b,a', utils_35.value, sp.as_nat(sp.len('b,a') - utils_35.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_36.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['b', 'a']), sp.TList(sp.TString))))
    sp.verify(sp.pack(sp.set_type_expr(self.string_split(sp.record(separator = ',,', text = 'a,b')), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a,b']), sp.TList(sp.TString))))
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('a', 'abc') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('b', 'abc') == False)
    sp.verify(self.string_starts_with(sp.record(prefix = 'a', text = 'abc')) == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'c') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'b') == False)
    sp.verify(self.string_ends_with(sp.record(postfix = 'c', text = 'abc')) == True)
    utils_38_hist = sp.local("utils_38_hist", {})
    sp.for utils_39_x in sp.list([1, 2, 3, 4, 5]):
      sp.if utils_38_hist.value.contains(utils_39_x):
        utils_38_hist.value[utils_39_x] += 1
      sp.else:
        utils_38_hist.value[utils_39_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(sp.list([1, 2, 3, 4, 5])))
    utils_40_result = sp.local("utils_40_result", 0)
    utils_41_half = sp.local("utils_41_half", compute_utils_90.value // 2)
    utils_42_use_average = sp.local("utils_42_use_average", (utils_41_half.value * 2) == compute_utils_90.value)
    utils_43_i = sp.local("utils_43_i", 0)
    sp.for utils_44_x in utils_38_hist.value.items():
      sp.if utils_42_use_average.value:
        sp.if utils_43_i.value < utils_41_half.value:
          utils_40_result.value = utils_44_x.key
          utils_43_i.value += utils_44_x.value
          sp.if utils_43_i.value > utils_41_half.value:
            utils_42_use_average.value = False
        sp.else:
          utils_40_result.value += utils_44_x.key
          utils_40_result.value //= 2
          utils_42_use_average.value = False
          utils_43_i.value += utils_44_x.value
      sp.else:
        sp.if utils_43_i.value <= utils_41_half.value:
          utils_40_result.value = utils_44_x.key
          utils_43_i.value += utils_44_x.value
    sp.verify(utils_40_result.value == 3)
    utils_45_hist = sp.local("utils_45_hist", {})
    sp.for utils_46_x in sp.list([1, 2, 2, 3]):
      sp.if utils_45_hist.value.contains(utils_46_x):
        utils_45_hist.value[utils_46_x] += 1
      sp.else:
        utils_45_hist.value[utils_46_x] = 1
    compute_utils_90i = sp.local("compute_utils_90i", sp.len(sp.list([1, 2, 2, 3])))
    utils_47_result = sp.local("utils_47_result", 0)
    utils_48_half = sp.local("utils_48_half", compute_utils_90i.value // 2)
    utils_49_use_average = sp.local("utils_49_use_average", (utils_48_half.value * 2) == compute_utils_90i.value)
    utils_50_i = sp.local("utils_50_i", 0)
    sp.for utils_51_x in utils_45_hist.value.items():
      sp.if utils_49_use_average.value:
        sp.if utils_50_i.value < utils_48_half.value:
          utils_47_result.value = utils_51_x.key
          utils_50_i.value += utils_51_x.value
          sp.if utils_50_i.value > utils_48_half.value:
            utils_49_use_average.value = False
        sp.else:
          utils_47_result.value += utils_51_x.key
          utils_47_result.value //= 2
          utils_49_use_average.value = False
          utils_50_i.value += utils_51_x.value
      sp.else:
        sp.if utils_50_i.value <= utils_48_half.value:
          utils_47_result.value = utils_51_x.key
          utils_50_i.value += utils_51_x.value
    sp.verify(utils_47_result.value == 2)
    sp.verify(self.math_median(sp.list([1, 2, 2, 5])) == 2)
    sp.verify(True, 'NUMBER_TOO_BIG')
    utils_52_bytes = sp.local("utils_52_bytes", sp.bytes('0x'))
    utils_53_value = sp.local("utils_53_value", 54)
    sp.while utils_53_value.value != 0:
      utils_52_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_53_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_52_bytes.value
      utils_53_value.value = utils_53_value.value >> 8
    sp.verify(utils_52_bytes.value == sp.bytes('0x36'))
    sp.verify(sp.slice(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'), 6, sp.as_nat(sp.len(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')) - 6)).open_some(message = 'Could not encode string to bytes.') == sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858'))
    sp.verify(sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')) < 28948022309329048855892746252171976963317496166410141009864396001978282409984, 'NUMBER_TOO_BIG')
    utils_54_bytes = sp.local("utils_54_bytes", sp.bytes('0x'))
    utils_55_value = sp.local("utils_55_value", sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')))
    sp.while utils_55_value.value != 0:
      utils_54_bytes.value = sp.slice(sp.pack(sp.mul(sp.to_int(utils_55_value.value), sp.bls12_381_fr('0x01'))), 6, 1).open_some() + utils_54_bytes.value
      utils_55_value.value = utils_55_value.value >> 8
    lengthBytes = sp.local("lengthBytes", utils_54_bytes.value)
    sp.while sp.len(lengthBytes.value) < 4:
      lengthBytes.value = sp.bytes('0x00') + lengthBytes.value
    sp.verify(sp.unpack(sp.concat(sp.list([sp.bytes('0x05'), sp.bytes('0x01'), lengthBytes.value, sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')])), sp.TString).open_some(message = 'Could not decode bytes to string') == 'TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    sp.verify(((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC'))) == False)
    sp.verify((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')))

  @sp.private_lambda()
  def int_of_bytes(_x0):
    compute_smartpy_utils_309 = sp.local("compute_smartpy_utils_309", sp.len(_x0))
    utils_54 = sp.local("utils_54", 0)
    sp.for utils_55 in sp.range(0, compute_smartpy_utils_309.value):
      compute_smartpy_utils_312 = sp.local("compute_smartpy_utils_312", sp.slice(_x0, utils_55, 1).open_some(message = sp.unit))
      compute_smartpy_utils_313 = sp.local("compute_smartpy_utils_313", sp.as_nat(compute_smartpy_utils_309.value - (utils_55 + 1)) * 2)
      utils_54.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_smartpy_utils_312.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_smartpy_utils_313.value, 16, 1)
    sp.result(utils_54.value)

  @sp.private_lambda()
  def int_of_string(_x1):
    utils_2 = sp.local("utils_2", _x1)
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_2.value = sp.slice(_x1, 1, sp.as_nat(sp.len(_x1) - 1)).open_some(message = '')
    utils_3 = sp.local("utils_3", 0)
    sp.for utils_4 in sp.range(0, sp.len(utils_2.value)):
      utils_3.value = (10 * utils_3.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_2.value, utils_4, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x1):
      utils_3.value *= -1
    sp.result(utils_3.value)

  @sp.private_lambda()
  def math_median(_x2):
    utils_5_hist = sp.local("utils_5_hist", {})
    sp.for utils_6_x in _x2:
      sp.if utils_5_hist.value.contains(utils_6_x):
        utils_5_hist.value[utils_6_x] += 1
      sp.else:
        utils_5_hist.value[utils_6_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(_x2))
    utils_7_result = sp.local("utils_7_result", 0)
    utils_8_half = sp.local("utils_8_half", compute_utils_90.value // 2)
    utils_9_use_average = sp.local("utils_9_use_average", (utils_8_half.value * 2) == compute_utils_90.value)
    utils_10_i = sp.local("utils_10_i", 0)
    sp.for utils_11_x in utils_5_hist.value.items():
      sp.if utils_9_use_average.value:
        sp.if utils_10_i.value < utils_8_half.value:
          utils_7_result.value = utils_11_x.key
          utils_10_i.value += utils_11_x.value
          sp.if utils_10_i.value > utils_8_half.value:
            utils_9_use_average.value = False
        sp.else:
          utils_7_result.value += utils_11_x.key
          utils_7_result.value //= 2
          utils_9_use_average.value = False
          utils_10_i.value += utils_11_x.value
      sp.else:
        sp.if utils_10_i.value <= utils_8_half.value:
          utils_7_result.value = utils_11_x.key
          utils_10_i.value += utils_11_x.value
    sp.result(utils_7_result.value)

  @sp.private_lambda()
  def math_pow(_x3):
    sp.result(sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(_x3.exponent, _x3.base, 1))

  @sp.private_lambda()
  def string_ends_with(_x4):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")(_x4.text, _x4.postfix))

  @sp.private_lambda()
  def string_of_int(_x5):
    utils_12 = sp.local("utils_12", abs(_x5))
    utils_13 = sp.local("utils_13", sp.list([]))
    sp.if utils_12.value == 0:
      utils_13.value.push('0')
    sp.while utils_12.value > 0:
      utils_13.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_12.value % 10])
      utils_12.value //= 10
    utils_14 = sp.local("utils_14", sp.concat(utils_13.value))
    sp.if _x5 < 0:
      utils_14.value = '-' + utils_14.value
    sp.result(utils_14.value)

  @sp.private_lambda()
  def string_split(_x6):
    utils_15 = sp.local("utils_15", 0)
    utils_16 = sp.local("utils_16", sp.list([]))
    sp.for utils_17 in sp.range(0, sp.len(_x6.text)):
      sp.if sp.slice(_x6.text, utils_17, 1).open_some() == _x6.separator:
        utils_16.value.push(sp.slice(_x6.text, utils_15.value, sp.as_nat(utils_17 - utils_15.value)).open_some())
        utils_15.value = utils_17 + 1
    sp.if sp.len(_x6.text) > 0:
      utils_16.value.push(sp.slice(_x6.text, utils_15.value, sp.as_nat(sp.len(_x6.text) - utils_15.value)).open_some())
    sp.result(utils_16.value.rev())

  @sp.private_lambda()
  def string_starts_with(_x7):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")(_x7.prefix, _x7.text))

sp.add_compilation_target("test", Contract())