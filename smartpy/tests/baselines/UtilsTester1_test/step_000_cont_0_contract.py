import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TUnit)
    self.init()

  @sp.entry_point
  def test(self):
    utils_16 = sp.local("utils_16", 1)
    utils_17 = sp.local("utils_17", sp.list([]))
    sp.if utils_16.value == 0:
      utils_17.value.push('0')
    sp.while utils_16.value > 0:
      utils_17.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_16.value % 10])
      utils_16.value //= 10
    utils_18 = sp.local("utils_18", sp.concat(utils_17.value))
    sp.if True:
      utils_18.value = '-' + utils_18.value
    sp.verify(utils_18.value == '-1')
    utils_19 = sp.local("utils_19", 1)
    utils_20 = sp.local("utils_20", sp.list([]))
    sp.if utils_19.value == 0:
      utils_20.value.push('0')
    sp.while utils_19.value > 0:
      utils_20.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_19.value % 10])
      utils_19.value //= 10
    utils_21 = sp.local("utils_21", sp.concat(utils_20.value))
    sp.if False:
      utils_21.value = '-' + utils_21.value
    sp.verify(utils_21.value == '1')
    sp.verify(self.string_of_int(2) == '2')
    utils_22 = sp.local("utils_22", '1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_22.value = sp.slice('1', 1, sp.as_nat(sp.len('1') - 1)).open_some(message = '')
    utils_23 = sp.local("utils_23", 0)
    sp.for utils_24 in sp.range(0, sp.len(utils_22.value)):
      utils_23.value = (10 * utils_23.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_22.value, utils_24, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '1'):
      utils_23.value *= -1
    sp.verify(utils_23.value == 1)
    utils_25 = sp.local("utils_25", '-1')
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_25.value = sp.slice('-1', 1, sp.as_nat(sp.len('-1') - 1)).open_some(message = '')
    utils_26 = sp.local("utils_26", 0)
    sp.for utils_27 in sp.range(0, sp.len(utils_25.value)):
      utils_26.value = (10 * utils_26.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_25.value, utils_27, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', '-1'):
      utils_26.value *= -1
    sp.verify(utils_26.value == (-1))
    sp.verify(self.int_of_string('2') == 2)
    utils_28 = sp.local("utils_28", 0)
    utils_29 = sp.local("utils_29", sp.list([]))
    sp.for utils_30 in sp.range(0, sp.len('a b')):
      sp.if sp.slice('a b', utils_30, 1).open_some() == ' ':
        utils_29.value.push(sp.slice('a b', utils_28.value, sp.as_nat(utils_30 - utils_28.value)).open_some())
        utils_28.value = utils_30 + 1
    sp.if sp.len('a b') > 0:
      utils_29.value.push(sp.slice('a b', utils_28.value, sp.as_nat(sp.len('a b') - utils_28.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_29.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a', 'b']), sp.TList(sp.TString))))
    utils_31 = sp.local("utils_31", 0)
    utils_32 = sp.local("utils_32", sp.list([]))
    sp.for utils_33 in sp.range(0, sp.len('b,a')):
      sp.if sp.slice('b,a', utils_33, 1).open_some() == ',':
        utils_32.value.push(sp.slice('b,a', utils_31.value, sp.as_nat(utils_33 - utils_31.value)).open_some())
        utils_31.value = utils_33 + 1
    sp.if sp.len('b,a') > 0:
      utils_32.value.push(sp.slice('b,a', utils_31.value, sp.as_nat(sp.len('b,a') - utils_31.value)).open_some())
    sp.verify(sp.pack(sp.set_type_expr(utils_32.value.rev(), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['b', 'a']), sp.TList(sp.TString))))
    sp.verify(sp.pack(sp.set_type_expr(self.string_split(sp.record(separator = ',,', text = 'a,b')), sp.TList(sp.TString))) == sp.pack(sp.set_type_expr(sp.list(['a,b']), sp.TList(sp.TString))))
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('a', 'abc') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('b', 'abc') == False)
    sp.verify(self.string_starts_with(sp.record(prefix = 'a', text = 'abc')) == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'c') == True)
    sp.verify(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")('abc', 'b') == False)
    sp.verify(self.string_ends_with(sp.record(postfix = 'c', text = 'abc')) == True)
    utils_34_hist = sp.local("utils_34_hist", {})
    sp.for utils_35_x in sp.list([1, 2, 3, 4, 5]):
      sp.if utils_34_hist.value.contains(utils_35_x):
        utils_34_hist.value[utils_35_x] += 1
      sp.else:
        utils_34_hist.value[utils_35_x] = 1
    compute_smartpy_utils_90i = sp.local("compute_smartpy_utils_90i", sp.len(sp.list([1, 2, 3, 4, 5])))
    utils_36_result = sp.local("utils_36_result", 0)
    utils_37_half = sp.local("utils_37_half", compute_smartpy_utils_90i.value // 2)
    utils_38_use_average = sp.local("utils_38_use_average", (utils_37_half.value * 2) == compute_smartpy_utils_90i.value)
    utils_39_i = sp.local("utils_39_i", 0)
    sp.for utils_40_x in utils_34_hist.value.items():
      sp.if utils_38_use_average.value:
        sp.if utils_39_i.value < utils_37_half.value:
          utils_36_result.value = utils_40_x.key
          utils_39_i.value += utils_40_x.value
          sp.if utils_39_i.value > utils_37_half.value:
            utils_38_use_average.value = False
        sp.else:
          utils_36_result.value += utils_40_x.key
          utils_36_result.value //= 2
          utils_38_use_average.value = False
          utils_39_i.value += utils_40_x.value
      sp.else:
        sp.if utils_39_i.value <= utils_37_half.value:
          utils_36_result.value = utils_40_x.key
          utils_39_i.value += utils_40_x.value
    sp.verify(utils_36_result.value == 3)
    utils_41_hist = sp.local("utils_41_hist", {})
    sp.for utils_42_x in sp.list([1, 2, 2, 3]):
      sp.if utils_41_hist.value.contains(utils_42_x):
        utils_41_hist.value[utils_42_x] += 1
      sp.else:
        utils_41_hist.value[utils_42_x] = 1
    compute_smartpy_utils_90 = sp.local("compute_smartpy_utils_90", sp.len(sp.list([1, 2, 2, 3])))
    utils_43_result = sp.local("utils_43_result", 0)
    utils_44_half = sp.local("utils_44_half", compute_smartpy_utils_90.value // 2)
    utils_45_use_average = sp.local("utils_45_use_average", (utils_44_half.value * 2) == compute_smartpy_utils_90.value)
    utils_46_i = sp.local("utils_46_i", 0)
    sp.for utils_47_x in utils_41_hist.value.items():
      sp.if utils_45_use_average.value:
        sp.if utils_46_i.value < utils_44_half.value:
          utils_43_result.value = utils_47_x.key
          utils_46_i.value += utils_47_x.value
          sp.if utils_46_i.value > utils_44_half.value:
            utils_45_use_average.value = False
        sp.else:
          utils_43_result.value += utils_47_x.key
          utils_43_result.value //= 2
          utils_45_use_average.value = False
          utils_46_i.value += utils_47_x.value
      sp.else:
        sp.if utils_46_i.value <= utils_44_half.value:
          utils_43_result.value = utils_47_x.key
          utils_46_i.value += utils_47_x.value
    sp.verify(utils_43_result.value == 2)
    sp.verify(self.math_median(sp.list([1, 2, 2, 5])) == 2)

  @sp.private_lambda()
  def int_of_string(_x0):
    utils_0 = sp.local("utils_0", _x0)
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x0):
      utils_0.value = sp.slice(_x0, 1, sp.as_nat(sp.len(_x0) - 1)).open_some(message = '')
    utils_1 = sp.local("utils_1", 0)
    sp.for utils_2 in sp.range(0, sp.len(utils_0.value)):
      utils_1.value = (10 * utils_1.value) + {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[sp.slice(utils_0.value, utils_2, 1).open_some()]
    sp.if sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")('-', _x0):
      utils_1.value *= -1
    sp.result(utils_1.value)

  @sp.private_lambda()
  def math_median(_x1):
    utils_3_hist = sp.local("utils_3_hist", {})
    sp.for utils_4_x in _x1:
      sp.if utils_3_hist.value.contains(utils_4_x):
        utils_3_hist.value[utils_4_x] += 1
      sp.else:
        utils_3_hist.value[utils_4_x] = 1
    compute_smartpy_utils_90 = sp.local("compute_smartpy_utils_90", sp.len(_x1))
    utils_5_result = sp.local("utils_5_result", 0)
    utils_6_half = sp.local("utils_6_half", compute_smartpy_utils_90.value // 2)
    utils_7_use_average = sp.local("utils_7_use_average", (utils_6_half.value * 2) == compute_smartpy_utils_90.value)
    utils_8_i = sp.local("utils_8_i", 0)
    sp.for utils_9_x in utils_3_hist.value.items():
      sp.if utils_7_use_average.value:
        sp.if utils_8_i.value < utils_6_half.value:
          utils_5_result.value = utils_9_x.key
          utils_8_i.value += utils_9_x.value
          sp.if utils_8_i.value > utils_6_half.value:
            utils_7_use_average.value = False
        sp.else:
          utils_5_result.value += utils_9_x.key
          utils_5_result.value //= 2
          utils_7_use_average.value = False
          utils_8_i.value += utils_9_x.value
      sp.else:
        sp.if utils_8_i.value <= utils_6_half.value:
          utils_5_result.value = utils_9_x.key
          utils_8_i.value += utils_9_x.value
    sp.result(utils_5_result.value)

  @sp.private_lambda()
  def math_pow(_x2):
    sp.result(sp.michelson("\n            DUP;\n            PUSH nat 0;\n            COMPARE;\n            NEQ;\n            LOOP\n            {\n                PUSH nat 0;\n                PUSH nat 2;\n                DUP 3;\n                EDIV;\n                IF_NONE\n                {\n                    UNIT;\n                    FAILWITH;\n                }\n                {\n                    CDR;\n                };\n                COMPARE;\n                NEQ;\n                IF\n                {\n                    SWAP;\n                    DUP;\n                    DUG 2;\n                    DIG 3;\n                    MUL;\n                    DUG 2;\n                }\n                {};\n                PUSH nat 1;\n                SWAP;\n                LSR;\n                SWAP;\n                DUP;\n                MUL;\n                SWAP;\n                DUP;\n                PUSH nat 0;\n                COMPARE;\n                NEQ;\n            };\n            DROP 2;\n            ")(_x2.exponent, _x2.base, 1))

  @sp.private_lambda()
  def string_ends_with(_x3):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DUP 3;\n            SIZE;\n            SWAP;\n            PAIR;\n            DUP;\n            UNPAIR;\n            COMPARE;\n            GE;\n            IF\n            {\n                UNPAIR;\n                DUP 2;\n                SWAP;\n                SUB;\n                ABS; # ABS is secure here because we already validated that (text length is greater or equal to postfix)\n                SLICE;\n                IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            }\n            {\n                DROP 3;\n                PUSH bool False;\n            };\n            ")(_x3.text, _x3.postfix))

  @sp.private_lambda()
  def string_of_int(_x4):
    utils_10 = sp.local("utils_10", abs(_x4))
    utils_11 = sp.local("utils_11", sp.list([]))
    sp.if utils_10.value == 0:
      utils_11.value.push('0')
    sp.while utils_10.value > 0:
      utils_11.value.push({0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}[utils_10.value % 10])
      utils_10.value //= 10
    utils_12 = sp.local("utils_12", sp.concat(utils_11.value))
    sp.if _x4 < 0:
      utils_12.value = '-' + utils_12.value
    sp.result(utils_12.value)

  @sp.private_lambda()
  def string_split(_x5):
    utils_13 = sp.local("utils_13", 0)
    utils_14 = sp.local("utils_14", sp.list([]))
    sp.for utils_15 in sp.range(0, sp.len(_x5.text)):
      sp.if sp.slice(_x5.text, utils_15, 1).open_some() == _x5.separator:
        utils_14.value.push(sp.slice(_x5.text, utils_13.value, sp.as_nat(utils_15 - utils_13.value)).open_some())
        utils_13.value = utils_15 + 1
    sp.if sp.len(_x5.text) > 0:
      utils_14.value.push(sp.slice(_x5.text, utils_13.value, sp.as_nat(sp.len(_x5.text) - utils_13.value)).open_some())
    sp.result(utils_14.value.rev())

  @sp.private_lambda()
  def string_starts_with(_x6):
    sp.result(sp.michelson("\n            DUP;\n            SIZE;\n            DIG 2;\n            SWAP;\n            PUSH nat 0;\n            SLICE;\n            IF_NONE\n                {\n                    DROP;\n                    PUSH bool False;\n                }\n                {\n                    COMPARE;\n                    EQ;\n                };\n            ")(_x6.prefix, _x6.text))

sp.add_compilation_target("test", Contract())