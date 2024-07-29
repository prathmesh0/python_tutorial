# Data Types/Object Types

## Number

- Examples: `123`, `3.14`, `0b11`
- Libraries:
  - `Decimal()`
  - `Fraction()`

## String

- Examples: `"bob"`, `"Bob's"`

## List

- Examples: `[1, 2, [2, "three"], 54]`, `list(range(10))`

---

# Python Commands and Notes

## Basic Arithmetic Operations

- Addition: `12 + 12` results in `24`
- Multiplication: `12 * 33` results in `396`
- Float Multiplication: `2.3 * 2` results in `4.6`
- Exponentiation:
  - `2 ** 2` results in `4`
  - `2 ** 4` results in `16`
  - `2 ** 100` results in `1267650600228229401496703205376`

## Math Module

- Pi Value: `math.pi` results in `3.141592653589793`

## Random Module

- Random Float: `random.random()` could result in a value like `0.25288615074346665`
- Random Choice: `random.choice([1, 2, 3, 4, 5])` could result in a value like `3`

## String Operations

- String Length: `len(username)` where `username = "Chaiaurcode"` results in `11`
- String Indexing:
  - `username[0]` where `username = "Chaiaurcode"` results in `'C'`
  - `username[-1]` where `username = "Chaiaurcode"` results in `'e'`
- String Slicing: `username[1:3]` where `username = "Chaiaurcode"` results in `'ha'`
- Immutable Strings: Trying to change `username[0] = "A"` raises `TypeError: 'str' object does not support item assignment`

## String Methods

- Available Methods: `dir(username)` where `username = "Chaiaurcode"` results in a list of methods such as:
  - `capitalize`, `casefold`, `center`, `count`, `encode`, `endswith`, `expandtabs`, `find`, `format`, `format_map`, `index`, `isalnum`, `isalpha`, `isascii`, `isdecimal`, `isdigit`, `isidentifier`, `islower`, `isnumeric`, `isprintable`, `isspace`, `istitle`, `isupper`, `join`, `ljust`, `lower`, `lstrip`, `maketrans`, `partition`, `removeprefix`, `removesuffix`, `replace`, `rfind`, `rindex`, `rjust`, `rpartition`, `rsplit`, `rstrip`, `split`, `splitlines`, `startswith`, `strip`, `swapcase`, `title`, `translate`, `upper`, `zfill`

## List Operations

- Creating a List: `myList = [123, "chai", 9.23]`
- Accessing a List: `myList` results in `[123, 'chai', 9.23]`
- List Length: `len(myList)` results in `3`

## Dictionary Operations

- Creating a Dictionary: `myD = {'one': 1, 'two': 2, 'three': 3}`
- Accessing a Dictionary:
- `myD` results in `{'one': 1, 'two': 2, 'three': 3}`
- `myD[two]` raises `NameError: name 'two' is not defined`
- `myD['two']` results in `2`

## Tuple Operations

- Creating a Tuple: `myTup = (1, 2, 3)`
- Accessing a Tuple:
- `myTup[0]` results in `1`
- Tuple Length: `len(myTup)` results in `3`

### Importing sys Module

- `import sys`

### Reference Counts

- `sys.getrefcount(24601)` results in `3`
- `sys.getrefcount('pop')` results in `4294967295`
- `sys.getrefcount('9')` results in `4294967295`

### Variable Assignment

- Assigning different values to a variable `a`:

```python
a = 3
a = 'chaiaurcode'
a = 3.14
a = 5
b = 2


a  # results in 5
b  # results in 2
a = a + 2  # a becomes 7

# List References and Copies

# List References
myListOne = [1, 2, 3]
myListTwo = myListOne
myListOne = 'chai'  # myListOne changes, myListTwo remains [1, 2, 3]

# Modifying Lists
myListOne = [1, 2, 3]
myListOne[0] = 44  # myListOne becomes [44, 2, 3], myListTwo remains [1, 2, 3]

l1 = [1, 2, 3]
l2 = l1
l1[0] = 44  # l1 and l2 both become [44, 2, 3]

# Separate Copies
p1 = [1, 2, 3]
p2 = p1
p2 = [1, 2, 3]  # p1 and p2 are now different
p1[0] = 55  # p1 becomes [55, 2, 3], p2 remains [1, 2, 3]

h1 = [1, 2, 3]
h2 = h1[:]  # h2 is a shallow copy of h1
h1[0] = 66  # h1 becomes [66, 2, 3], h2 remains [1, 2, 3]

import copy
h2 = copy.copy(h1)  # another way to make a shallow copy

# Comparisons
# Comparing References and Values
n = [1, 2, 3]
m = n
m == n  # True
m is n  # True

n = [1, 2, 3]
m = [1, 2, 3]
m == n  # True
m is n  # False
```
