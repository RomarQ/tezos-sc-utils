import smartpy as sp

import smartpy_utils as utils
# Or
Utils = sp.io.import_script_from_url("file:smartpy/utils.py")

class UtilsTester1(sp.Contract):

    @sp.private_lambda()
    def string_of_int(self, n):
        sp.result(utils.String.of_int(n))

    @sp.private_lambda()
    def int_of_string(self, s):
        sp.result(utils.Int.of_string(s))

    @sp.private_lambda()
    def string_split(self, params):
        sp.result(utils.String.split(params.text, params.separator))

    @sp.private_lambda()
    def string_starts_with(self, params):
        sp.result(utils.String.starts_with(params.text, params.prefix))

    @sp.private_lambda()
    def string_ends_with(self, params):
        sp.result(utils.String.ends_with(params.text, params.postfix))

    @sp.private_lambda()
    def math_pow(self, params):
        sp.result(utils.Math.pow(params.base, params.exponent))

    @sp.private_lambda()
    def math_median(self, l):
        sp.result(utils.Math.median(l))

    @sp.entry_point
    def test(self):
        sp.verify(utils.String.of_int(-1) == "-1")
        sp.verify(utils.String.of_int(1) == "1")
        sp.verify(self.string_of_int(2) == "2")

        sp.verify(utils.Int.of_string("1") == 1)
        sp.verify(utils.Int.of_string("-1") == -1)
        sp.verify(self.int_of_string("2") == 2)

        sp.verify_equal(utils.String.split("a b", " "), ["a","b"])
        sp.verify_equal(utils.String.split("b,a", ","), ["b","a"])
        sp.verify_equal(self.string_split(sp.record(text="a,b", separator=",,")), ["a,b"])

        sp.verify(utils.String.starts_with("abc", "a") == True)
        sp.verify(utils.String.starts_with("abc", "b") == False)
        sp.verify(self.string_starts_with(sp.record(text="abc", prefix="a")) == True)

        sp.verify(utils.String.ends_with("abc", "c") == True)
        sp.verify(utils.String.ends_with("abc", "b") == False)
        sp.verify(self.string_ends_with(sp.record(text="abc", postfix="c")) == True)

        sp.verify(utils.Math.median([1, 2, 3, 4, 5]) == 3)
        sp.verify(utils.Math.median([1, 2, 2, 3]) == 2)
        sp.verify(self.math_median([1, 2, 2, 5]) == 2)

        sp.verify(utils.Bytes.of_nat(54) == sp.bytes("0x36"))
        sp.verify(utils.Bytes.of_string("TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == sp.bytes("0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858"))
        sp.verify(utils.String.of_bytes(sp.bytes("0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858")) == "TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        sp.verify(utils.Address.is_kt1(sp.address("tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC")) == False)
        sp.verify(utils.Address.is_kt1(sp.address("KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ"))) # true

class UtilsTester2(sp.Contract):

    @sp.private_lambda()
    def string_of_int(self, n):
        sp.result(Utils.String.of_int(n))

    @sp.private_lambda()
    def int_of_string(self, s):
        sp.result(Utils.Int.of_string(s))

    @sp.private_lambda()
    def string_split(self, params):
        sp.result(Utils.String.split(params.text, params.separator))

    @sp.private_lambda()
    def string_starts_with(self, params):
        sp.result(Utils.String.starts_with(params.text, params.prefix))

    @sp.private_lambda()
    def string_ends_with(self, params):
        sp.result(Utils.String.ends_with(params.text, params.postfix))

    @sp.private_lambda()
    def math_pow(self, params):
        sp.result(Utils.Math.pow(params.base, params.exponent))

    @sp.private_lambda()
    def math_median(self, l):
        sp.result(Utils.Math.median(l))

    @sp.entry_point
    def test(self):
        sp.verify(Utils.String.of_int(-1) == "-1")
        sp.verify(Utils.String.of_int(1) == "1")
        sp.verify(self.string_of_int(2) == "2")

        sp.verify(Utils.Int.of_string("1") == 1)
        sp.verify(Utils.Int.of_string("-1") == -1)
        sp.verify(self.int_of_string("2") == 2)

        sp.verify_equal(Utils.String.split("a b", " "), ["a","b"])
        sp.verify_equal(Utils.String.split("b,a", ","), ["b","a"])
        sp.verify_equal(self.string_split(sp.record(text="a,b", separator=",,")), ["a,b"])

        sp.verify(Utils.String.starts_with("abc", "a") == True)
        sp.verify(Utils.String.starts_with("abc", "b") == False)
        sp.verify(self.string_starts_with(sp.record(text="abc", prefix="a")) == True)

        sp.verify(Utils.String.ends_with("abc", "c") == True)
        sp.verify(Utils.String.ends_with("abc", "b") == False)
        sp.verify(self.string_ends_with(sp.record(text="abc", postfix="c")) == True)

        sp.verify(Utils.Math.median([1, 2, 3, 4, 5]) == 3)
        sp.verify(Utils.Math.median([1, 2, 2, 3]) == 2)
        sp.verify(self.math_median([1, 2, 2, 5]) == 2)

        sp.verify(Utils.Bytes.of_nat(54) == sp.bytes("0x36"))
        sp.verify(Utils.Bytes.of_string("TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == sp.bytes("0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858"))
        sp.verify(Utils.String.of_bytes(sp.bytes("0x544553545f535452494e475f585858585858585858585858585858585858585858585858585858585858585858585858585858585858")) == "TEST_STRING_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        sp.verify(Utils.Address.is_kt1(sp.address("tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC")) == False)
        sp.verify(Utils.Address.is_kt1(sp.address("KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ"))) # true

@sp.add_test(name = "UtilsTester1_test")
def test1():
    scenario = sp.test_scenario()

    c1 = UtilsTester1()
    scenario += c1

    c1.test()

@sp.add_test(name = "UtilsTester2_test")
def test2():
    scenario = sp.test_scenario()

    c1 = UtilsTester2()
    scenario += c1

    c1.test()

sp.add_compilation_target("UtilsTester1_compilation", UtilsTester1())
sp.add_compilation_target("UtilsTester2_compilation", UtilsTester2())



# Overrides

import inspect

def get_file_line_no(line_no = None):
    if line_no is not None:
        return line_no

    frame = inspect.currentframe().f_back
    while frame:
        fn = frame.f_code.co_filename
        if ("smartpy.py" not in fn
            and "<frozen " not in fn
            and "smartpyc.py" not in fn
            and "init" != fn):
            fn = fn.strip("<>./,' ")
            if '/' in fn:
                fn = fn[fn.rindex("/") + 1:]
            elif ':' in fn:
                fn = fn[fn.rindex(":") + 1:]
            return sp.LineNo(fn, frame.f_lineno)
        frame = frame.f_back
    return sp.LineNo("", -1)

sp.get_file_line_no = get_file_line_no
