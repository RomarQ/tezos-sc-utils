import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_21 = sp.local("utils_21", 1)
    utils_22 = sp.local("utils_22", sp.list([]))
    sp.if utils_21.value == 0:
      utils_22.value.push('0')
    sp.while utils_21.value > 0:
      utils_22.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_21.value % 10])
      utils_21.value //= 10
    utils_23 = sp.local("utils_23", sp.concat(utils_22.value))
    sp.if True:
      utils_23.value = '-' + utils_23.value
    sp.verify(utils_23.value == '-1')
    utils_24 = sp.local("utils_24", 1)
    utils_25 = sp.local("utils_25", sp.list([]))
    sp.if utils_24.value == 0:
      utils_25.value.push('0')
    sp.while utils_24.value > 0:
      utils_25.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_24.value % 10])
      utils_24.value //= 10
    utils_26 = sp.local("utils_26", sp.concat(utils_25.value))
    sp.if False:
      utils_26.value = '-' + utils_26.value
    sp.verify(utils_26.value == '1')
    sp.verify(self.string_of_int(2) == '2')
    utils_27 = sp.local("utils_27", '1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_27.value = sp.slice('1', 1, sp.as_nat(sp.len('1') - 1)).open_some(message = '')
    utils_28 = sp.local("utils_28", 0)
    sp.for utils_29 in sp.range(0, sp.len(utils_27.value)):
      utils_28.value = (10 * utils_28.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_27.value, utils_29, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_28.value *= -1
    sp.verify(utils_28.value == 1)
    utils_30 = sp.local("utils_30", '-1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_30.value = sp.slice('-1', 1, sp.as_nat(sp.len('-1') - 1)).open_some(message = '')
    utils_31 = sp.local("utils_31", 0)
    sp.for utils_32 in sp.range(0, sp.len(utils_30.value)):
      utils_31.value = (10 * utils_31.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_30.value, utils_32, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_31.value *= -1
    sp.verify(utils_31.value == (-1))
    sp.verify(self.int_of_string('2') == 2)
    utils_33 = sp.local("utils_33", sp.len(sp.bytes('0x0100')))
    utils_34 = sp.local("utils_34", 0)
    sp.for utils_35 in sp.range(0, utils_33.value):
      compute_utils_342 = sp.local("compute_utils_342", sp.slice(sp.bytes('0x0100'), utils_35, 1).open_some(message = sp.unit))
      compute_utils_343 = sp.local("compute_utils_343", sp.as_nat(utils_33.value - (utils_35 + 1)) * 2)
      utils_34.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_utils_342.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_utils_343.value, 16, 1)
    sp.verify(utils_34.value == 256)
    sp.verify(self.int_of_bytes(sp.bytes('0x0100')) == 256)
    utils_36 = sp.local("utils_36", 0)
    utils_37 = sp.local("utils_37", sp.list([]))
    sp.for utils_38 in sp.range(0, sp.len('a b')):
      sp.if sp.slice('a b', utils_38, 1).open_some() == ' ':
        utils_37.value.push(sp.slice('a b', utils_36.value, sp.as_nat(utils_38 - utils_36.value)).open_some())
        utils_36.value = utils_38 + 1
    sp.if sp.len('a b') > 0:
      utils_37.value.push(sp.slice('a b', utils_36.value, sp.as_nat(sp.len('a b') - utils_36.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_37.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a', 'b']), sp.TList(sp.TString))))
    utils_39 = sp.local("utils_39", 0)
    utils_40 = sp.local("utils_40", sp.list([]))
    sp.for utils_41 in sp.range(0, sp.len('b,a')):
      sp.if sp.slice('b,a', utils_41, 1).open_some() == ',':
        utils_40.value.push(sp.slice('b,a', utils_39.value, sp.as_nat(utils_41 - utils_39.value)).open_some())
        utils_39.value = utils_41 + 1
    sp.if sp.len('b,a') > 0:
      utils_40.value.push(sp.slice('b,a', utils_39.value, sp.as_nat(sp.len('b,a') - utils_39.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_40.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['b', 'a']), sp.TList(sp.TString))))
    sp.verify(sp.pack(sp.set_type_expr(self.string_split(sp.record(separator = ',,', text = 'a,b')), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a,b']), sp.TList(sp.TString))))
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('a', 'abc') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('b', 'abc') == False)
    sp.verify(self.string_starts_with(sp.record(prefix = 'a', text = 'abc')) == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'c') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'b') == False)
    sp.verify(self.string_ends_with(sp.record(postfix = 'c', text = 'abc')) == True)
    utils_42_hist = sp.local("utils_42_hist", {})
    sp.for utils_43_x in sp.list([1, 2, 3, 4, 5]):
      sp.if utils_42_hist.value.contains(utils_43_x):
        utils_42_hist.value[utils_43_x] += 1
      sp.else:
        utils_42_hist.value[utils_43_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(sp.list([1, 2, 3, 4, 5])))
    utils_44_result = sp.local("utils_44_result", 0)
    utils_45_half = sp.local("utils_45_half", compute_utils_90.value // 2)
    utils_46_use_average = sp.local("utils_46_use_average", (utils_45_half.value * 2) == compute_utils_90.value)
    utils_47_i = sp.local("utils_47_i", 0)
    sp.for utils_48_x in utils_42_hist.value.items():
      sp.if utils_46_use_average.value:
        sp.if utils_47_i.value < utils_45_half.value:
          utils_44_result.value = utils_48_x.key
          utils_47_i.value += utils_48_x.value
          sp.if utils_47_i.value > utils_45_half.value:
            utils_46_use_average.value = False
        sp.else:
          utils_44_result.value += utils_48_x.key
          utils_44_result.value //= 2
          utils_46_use_average.value = False
          utils_47_i.value += utils_48_x.value
      sp.else:
        sp.if utils_47_i.value <= utils_45_half.value:
          utils_44_result.value = utils_48_x.key
          utils_47_i.value += utils_48_x.value
    sp.verify(utils_44_result.value == 3)
    utils_49_hist = sp.local("utils_49_hist", {})
    sp.for utils_50_x in sp.list([1, 2, 2, 3]):
      sp.if utils_49_hist.value.contains(utils_50_x):
        utils_49_hist.value[utils_50_x] += 1
      sp.else:
        utils_49_hist.value[utils_50_x] = 1
    compute_utils_90i = sp.local("compute_utils_90i", sp.len(sp.list([1, 2, 2, 3])))
    utils_51_result = sp.local("utils_51_result", 0)
    utils_52_half = sp.local("utils_52_half", compute_utils_90i.value // 2)
    utils_53_use_average = sp.local("utils_53_use_average", (utils_52_half.value * 2) == compute_utils_90i.value)
    utils_54_i = sp.local("utils_54_i", 0)
    sp.for utils_55_x in utils_49_hist.value.items():
      sp.if utils_53_use_average.value:
        sp.if utils_54_i.value < utils_52_half.value:
          utils_51_result.value = utils_55_x.key
          utils_54_i.value += utils_55_x.value
          sp.if utils_54_i.value > utils_52_half.value:
            utils_53_use_average.value = False
        sp.else:
          utils_51_result.value += utils_55_x.key
          utils_51_result.value //= 2
          utils_53_use_average.value = False
          utils_54_i.value += utils_55_x.value
      sp.else:
        sp.if utils_54_i.value <= utils_52_half.value:
          utils_51_result.value = utils_55_x.key
          utils_54_i.value += utils_55_x.value
    sp.verify(utils_51_result.value == 2)
    sp.verify(self.math_median(sp.list([1, 2, 2, 5])) == 2)
    compute_utils_118 = sp.local("compute_utils_118", 3 - sp.len(sp.bytes('0x11')))
    utils_56_bytes = sp.local("utils_56_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_56_bytes.value) < sp.as_nat(compute_utils_118.value):
      utils_56_bytes.value = sp.bytes('0x00') + utils_56_bytes.value
    sp.verify((utils_56_bytes.value + sp.bytes('0x11')) == sp.bytes('0x000011'))
    compute_utils_126 = sp.local("compute_utils_126", 3 - sp.len(sp.bytes('0x11')))
    utils_57_bytes = sp.local("utils_57_bytes", sp.bytes('0x'))
    sp.while sp.len(utils_57_bytes.value) < sp.as_nat(compute_utils_126.value):
      utils_57_bytes.value = sp.bytes('0x00') + utils_57_bytes.value
    sp.verify((sp.bytes('0x11') + utils_57_bytes.value) == sp.bytes('0x110000'))
    utils_58_value = sp.local("utils_58_value", 54, sp.TNat)
    utils_59_left_nibble = sp.local("utils_59_left_nibble", sp.none)
    utils_60_bytes = sp.local("utils_60_bytes", sp.list([]))
    sp.while utils_58_value.value != 0:
      match_pair_utils_155_fst, match_pair_utils_155_snd = sp.match_tuple(sp.ediv(utils_58_value.value, 16).open_some(), "match_pair_utils_155_fst", "match_pair_utils_155_snd")
      utils_58_value.value = match_pair_utils_155_fst
      with utils_59_left_nibble.value.match_cases() as arg:
        with arg.match('Some') as Some:
          utils_59_left_nibble.value = sp.none
          sp.verify(((match_pair_utils_155_snd << 4) | Some) < 256, 'NUMBER_TOO_BIG')
          utils_60_bytes.value.push(sp.slice(sp.pack(sp.mul(sp.to_int((match_pair_utils_155_snd << 4) | Some), sp.bls12_381_fr('0x01'))), 6, 1).open_some())
        with arg.match('None') as None:
          utils_59_left_nibble.value = sp.some(match_pair_utils_155_snd)

    with utils_59_left_nibble.value.match('Some') as Some:
      utils_59_left_nibble.value = sp.none
      sp.verify((0 | Some) < 256, 'NUMBER_TOO_BIG')
      utils_60_bytes.value.push(sp.slice(sp.pack(sp.mul(sp.to_int(0 | Some), sp.bls12_381_fr('0x01'))), 6, 1).open_some())
    sp.verify(sp.concat(utils_60_bytes.value) == sp.bytes('0x36'))
    sp.verify(sp.slice(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'), 6, sp.as_nat(sp.len(sp.pack('TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')) - 6)).open_some(message = 'Could not encode string to bytes.') == sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858'))
    utils_61_value = sp.local("utils_61_value", sp.len(sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')), sp.TNat)
    utils_62_left_nibble = sp.local("utils_62_left_nibble", sp.none)
    utils_63_bytes = sp.local("utils_63_bytes", sp.list([]))
    sp.while utils_61_value.value != 0:
      match_pair_utils_155_fst, match_pair_utils_155_snd = sp.match_tuple(sp.ediv(utils_61_value.value, 16).open_some(), "match_pair_utils_155_fst", "match_pair_utils_155_snd")
      utils_61_value.value = match_pair_utils_155_fst
      with utils_62_left_nibble.value.match_cases() as arg:
        with arg.match('Some') as Some:
          utils_62_left_nibble.value = sp.none
          sp.verify(((match_pair_utils_155_snd << 4) | Some) < 256, 'NUMBER_TOO_BIG')
          utils_63_bytes.value.push(sp.slice(sp.pack(sp.mul(sp.to_int((match_pair_utils_155_snd << 4) | Some), sp.bls12_381_fr('0x01'))), 6, 1).open_some())
        with arg.match('None') as None:
          utils_62_left_nibble.value = sp.some(match_pair_utils_155_snd)

    with utils_62_left_nibble.value.match('Some') as Some:
      utils_62_left_nibble.value = sp.none
      sp.verify((0 | Some) < 256, 'NUMBER_TOO_BIG')
      utils_63_bytes.value.push(sp.slice(sp.pack(sp.mul(sp.to_int(0 | Some), sp.bls12_381_fr('0x01'))), 6, 1).open_some())
    lengthBytes = sp.local("lengthBytes", sp.concat(utils_63_bytes.value))
    sp.while sp.len(lengthBytes.value) < 4:
      lengthBytes.value = sp.bytes('0x00') + lengthBytes.value
    sp.verify(sp.unpack(sp.concat(sp.list([sp.bytes('0x05'), sp.bytes('0x01'), lengthBytes.value, sp.bytes('0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858')])), sp.TString).open_some(message = 'Could not decode bytes to string') == 'TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    sp.verify(((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC'))) == False)
    sp.verify((sp.address('KT1XvNYseNDJJ6Kw27qhSEDF8ys8JhDopzfG') >= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')) & (sp.address('KT18amZmM5W7qDWVt2pH6uj7sCEd3kbzLrHT') <= sp.address('KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ')))

  @sp.private_lambda()
  def int_of_bytes(_x0):
    utils_57 = sp.local("utils_57", sp.len(_x0))
    utils_58 = sp.local("utils_58", 0)
    sp.for utils_59 in sp.range(0, utils_57.value):
      compute_smartpy_utils_342 = sp.local("compute_smartpy_utils_342", sp.slice(_x0, utils_59, 1).open_some(message = sp.unit))
      compute_smartpy_utils_343 = sp.local("compute_smartpy_utils_343", sp.as_nat(utils_57.value - (utils_59 + 1)) * 2)
      utils_58.value += sp.as_nat(sp.to_int(sp.unpack((sp.bytes('0x050a00000020') + compute_smartpy_utils_342.value) + sp.bytes('0x00000000000000000000000000000000000000000000000000000000000000'), sp.TBls12_381_fr).open_some(message = sp.unit))) * sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(compute_smartpy_utils_343.value, 16, 1)
    sp.result(utils_58.value)

  @sp.private_lambda()
  def int_of_string(_x2):
    utils_5 = sp.local("utils_5", _x2)
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x2):
      utils_5.value = sp.slice(_x2, 1, sp.as_nat(sp.len(_x2) - 1)).open_some(message = '')
    utils_6 = sp.local("utils_6", 0)
    sp.for utils_7 in sp.range(0, sp.len(utils_5.value)):
      utils_6.value = (10 * utils_6.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_5.value, utils_7, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x2):
      utils_6.value *= -1
    sp.result(utils_6.value)

  @sp.private_lambda()
  def math_median(_x4):
    utils_8_hist = sp.local("utils_8_hist", {})
    sp.for utils_9_x in _x4:
      sp.if utils_8_hist.value.contains(utils_9_x):
        utils_8_hist.value[utils_9_x] += 1
      sp.else:
        utils_8_hist.value[utils_9_x] = 1
    compute_utils_90 = sp.local("compute_utils_90", sp.len(_x4))
    utils_10_result = sp.local("utils_10_result", 0)
    utils_11_half = sp.local("utils_11_half", compute_utils_90.value // 2)
    utils_12_use_average = sp.local("utils_12_use_average", (utils_11_half.value * 2) == compute_utils_90.value)
    utils_13_i = sp.local("utils_13_i", 0)
    sp.for utils_14_x in utils_8_hist.value.items():
      sp.if utils_12_use_average.value:
        sp.if utils_13_i.value < utils_11_half.value:
          utils_10_result.value = utils_14_x.key
          utils_13_i.value += utils_14_x.value
          sp.if utils_13_i.value > utils_11_half.value:
            utils_12_use_average.value = False
        sp.else:
          utils_10_result.value += utils_14_x.key
          utils_10_result.value //= 2
          utils_12_use_average.value = False
          utils_13_i.value += utils_14_x.value
      sp.else:
        sp.if utils_13_i.value <= utils_11_half.value:
          utils_10_result.value = utils_14_x.key
          utils_13_i.value += utils_14_x.value
    sp.result(utils_10_result.value)

  @sp.private_lambda()
  def math_pow(_x6):
    sp.result(sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(_x6.exponent, _x6.base, 1))

  @sp.private_lambda()
  def string_ends_with(_x8):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")(_x8.text, _x8.postfix))

  @sp.private_lambda()
  def string_of_int(_x10):
    utils_15 = sp.local("utils_15", abs(_x10))
    utils_16 = sp.local("utils_16", sp.list([]))
    sp.if utils_15.value == 0:
      utils_16.value.push('0')
    sp.while utils_15.value > 0:
      utils_16.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_15.value % 10])
      utils_15.value //= 10
    utils_17 = sp.local("utils_17", sp.concat(utils_16.value))
    sp.if _x10 < 0:
      utils_17.value = '-' + utils_17.value
    sp.result(utils_17.value)

  @sp.private_lambda()
  def string_split(_x12):
    utils_18 = sp.local("utils_18", 0)
    utils_19 = sp.local("utils_19", sp.list([]))
    sp.for utils_20 in sp.range(0, sp.len(_x12.text)):
      sp.if sp.slice(_x12.text, utils_20, 1).open_some() == _x12.separator:
        utils_19.value.push(sp.slice(_x12.text, utils_18.value, sp.as_nat(utils_20 - utils_18.value)).open_some())
        utils_18.value = utils_20 + 1
    sp.if sp.len(_x12.text) > 0:
      utils_19.value.push(sp.slice(_x12.text, utils_18.value, sp.as_nat(sp.len(_x12.text) - utils_18.value)).open_some())
    sp.result(utils_19.value.rev())

  @sp.private_lambda()
  def string_starts_with(_x14):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")(_x14.prefix, _x14.text))

sp.add_compilation_target("test", Contract())