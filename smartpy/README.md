# SmartPy Utilities

## Usage

```py
import smartpy as sp

Utils = sp.io.import_script_from_url("https://raw.githubusercontent.com/RomarQ/tezos-sc-utils/main/smartpy/utils.py")

class Contract(sp.Contract):

    @sp.entry_point
    def test(self):
        # Converts an int to a string (fails if invalid)
        sp.verify(Utils.String.of_int(-1) == "-1")
        # Converts a string to an int (fails if invalid)
        sp.verify(Utils.Int.of_string("1") == 1)
        # Splits a string
        sp.verify_equal(Utils.String.split("a b", " "), ["a","b"])
        # Checks if a string starts with a given substring
        sp.verify(Utils.String.starts_with("abc", "a") == True)
        # Checks if a string ends with a given substring
        sp.verify(Utils.String.ends_with("abc", "c") == True)
        # Computes the median
        sp.verify(Utils.Math.median([1, 2, 3, 4, 5]) == 3)
```

## Documentation

- Bytes

    - **of_string(str)**

        ```py
        Utils.Bytes.of_string("TEST_STRING") # "0x544553545f535452494e47"
        ```

    - **of_nat(number)**

        ```py
        Utils.Bytes.of_nat(56) # "0x36"
        ```

- String

    - **of_bytes(bytes)**

        ```py
        Utils.String.of_bytes(sp.bytes("0x544553545f535452494e47")) # "TEST_STRING"
        ```

    - **of_int(number)**

        ```py
        Utils.String.of_int(1) # "1"
        ```

    - **split(str, token)**

        ```py
        Utils.String.split("a b", " ") # ["a","b"]
        ```

    - **starts_with(str, substr)**

        ```py
        Utils.String.starts_with("ab", "a") # True
        ```

    - **ends_with(str, substr)**

        ```py
        Utils.String.ends_with("ab", "b") # True
        ```

- Int

    - **of_string(str)**

        ```py
        Utils.Int.of_string("1") # 1
        ```

    - **of_bytes(b)**

        ```py
        Utils.Int.of_bytes(sp.bytes("0x0100")) # 256
        ```

- Address

    - **is_kt1(address)**

        ```py
        Utils.Address.is_kt1(sp.address("tz28QJHLyqvaY2rXAoFZTbxrXeD88NA8wscC")) # False
        Utils.Address.is_kt1(sp.address("KT18hYjnko76SBVv6TaCT4kU6B32mJk6JWLZ")) # True
        ```


- Math

    - **median(list)**

        ```py
        Utils.Math.median([1, 2, 3, 4, 5]) # 3
        ```
