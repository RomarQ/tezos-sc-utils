import smartpy as sp

tstorage = sp.TUnit
tparameter = sp.TVariant(test = sp.TUnit).layout("test")
tprivates = { "int_of_string": sp.TLambda(sp.TString, sp.TInt), "math_median": sp.TLambda(sp.TList(sp.TNat), sp.TNat), "math_pow": sp.TLambda(sp.TRecord(base = sp.TNat, exponent = sp.TNat).layout(("base", "exponent")), sp.TNat), "string_ends_with": sp.TLambda(sp.TRecord(postfix = sp.TString, text = sp.TString).layout(("postfix", "text")), sp.TBool), "string_of_int": sp.TLambda(sp.TInt, sp.TString), "string_split": sp.TLambda(sp.TRecord(separator = sp.TString, text = sp.TString).layout(("separator", "text")), sp.TList(sp.TString)), "string_starts_with": sp.TLambda(sp.TRecord(prefix = sp.TString, text = sp.TString).layout(("prefix", "text")), sp.TBool) }
tviews = { }
