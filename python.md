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

# Numbers

## Basic Arithmetic

### Use Case

Performing basic arithmetic operations and conversions between different types.

```python
x = 2
y = 3
z = 4

x + y  # 5
(x + y) * z  # 20
40 + 2.34  # 42.34

# 'hitesh' + 9  # TypeError: can only concatenate str (not "int") to str
int(33.4)  # 33
float(69)  # 69.0

'chai' + 'code'  # 'chaicode'
(x, y, z)  # (2, 3, 4)
x + 1, y * 2  # (3, 6)
y % 2  # 1
z ** 2  # 16
2 ** 1000  # 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
result = 1 / 3.0
result  # 0.3333333333333333

repr('chai')  # "'chai'"
str('chai')  # 'chai'
print('chai')  # chai

1 < 2  # True
5.0 == 5.0  # True
4.0 != 5.0  # True
x, y, z  # (2, 3, 4)
x < y < z  # True
(x < y) and (y < z)  # True
1 == 2 < 3  # False
1 == 2 and 2 < 3  # False
```

```python
import math

math.floor(3.5)  # 3
math.floor(-3.5)  # -4
math.floor(3.6)  # 3
math.trunc(2.8)  # 2
math.trunc(-2.8)  # -2
```

## Large Numbers

Handling large integers and performing operations on them.

```python
python
999999999999999999999999999999999999999999999999999 + 1  # 1000000000000000000000000000000000000000000000000000
999999999999999999999999999999999999999999999999999 * 2.1  # 2.1e+51
```

```python
## Complex Numbers

Working with complex numbers and performing arithmetic operations.

2 + 1j  # (2+1j)
(2 + 1j) * 3  # (6+3j)
```

## Understanding different number systems and converting between them.

```python
0o20  # 16 (octal)
0xFF  # 255 (hexadecimal)
0b1000  # 8 (binary)
oct(64)  # '0o100'
hex(64)  # '0x40'
bin(64)  # '0b1000000'
int('64', 8)  # 52 (octal to decimal)
int('64', 16)  # 100 (hexadecimal to decimal)
int('1000', 2)  # 8 (binary to decimal)
```

## Bitwise Operations

Performing bitwise operations on integers.

```python
Copy code
x = 1
x << 2  # 4
x | 2  # 3
x & 3  # 1
```

## Random Module

Generating random numbers and performing random operations on lists.

```python

import random

random.random()  # random float between 0.0 and 1.0
random.randint(1, 10)  # random integer between 1 and 10

l1 = ['lemon', 'masala', 'ginger', 'mint']
random.choice(l1)  # random element from l1
random.shuffle(l1)  # shuffle l1 in place
l1  # shuffled list
```

## Floating Point Precision

Handling precision issues with floating point arithmetic and using the decimal module for accurate calculations.

```python
Copy code
0.1 + 0.1 + 0.4  # 0.6000000000000001
0.1 + 0.1 + 0.1  # 0.30000000000000004
0.1 + 0.1 + 0.1 - 0.3  # 5.551115123125783e-17

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')  # Decimal('0.3')

```

## Fractions Module

Using the fractions module to work with rational numbers.

```python
from fractions import Fraction

myFra = Fraction(2, 7)
myFra  # Fraction(2, 7)
```

## Sets

Performing set operations like union, intersection, and difference.

```python
setone = {1, 2, 3, 4}
settwo = {1, 3}
setone & settwo  # {1, 3}
setone | settwo  # {1, 2, 3, 4}
setone - settwo  # {2, 4}
setone - {1, 2, 3, 4}  # set()

```

## Boolean Types

Understanding boolean types and their interactions with integers.

```python

type({})  # <class 'dict'>
type(True)  # <class 'bool'>
True == 1  # True
False == 0  # True
True is 1  # False (SyntaxWarning: "is" with 'int' literal. Did you mean "=="?)
True + 4  # 5
```

````markdown
# Python Strings and Their Methods

## Basic String Assignment and Printing

```python
chai = "Lemon Chai"
print(chai)  # Output: Lemon Chai

chai = "Masala Chai"
chai  # Output: 'Masala Chai'
```
````

## String Indexing and Slicing

```python
first_char = chai[0]
print(first_char)  # Output: M

slice_chai = chai[0:6]
print(slice_chai)  # Output: Masala

chai[-1]  # Output: 'i'

num_list = "0123456789"
num_list[:]  # Output: '0123456789'
num_list[2:5]  # Output: '234'
num_list[0:7]  # Output: '0123456'
num_list[0:7:3]  # Output: '036'
```

## String Methods

```python
print(chai.lower())  # Output: masala chai
print(chai.upper())  # Output: MASALA CHAI

chai = "    Masala Chai  "
print(chai.strip())  # Output: Masala Chai

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))  # Output: Ginger Chai

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))  # Output: ['Lemon', 'Ginger', 'Masala', 'Mint']

chai = "Masala Chai"
print(chai.find("Chai"))  # Output: 7
print(chai.find("chai"))  # Output: -1

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))  # Output: 3

chai_type = "Masala Chai"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))  # Output: I ordered 2 cups of Masala Chai chai

chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))  # Output: LemonMasalaGinger
print(" ".join(chai_variety))  # Output: Lemon Masala Ginger

print(len(chai))  # Output: 11

for letter in chai:
    print(letter)

chai = "He said, \"Masala Chai is awesome\""
print(chai)  # Output: He said, "Masala Chai is awesome"

chai = "Masala\nChai"
print(chai)  # Output: Masala
             #         Chai

chai = r"Masala\nChai"
print(chai)  # Output: Masala\nChai

print("Masala" in chai)  # Output: True
print("Masalaa" in chai)  # Output: False
```





# Python Lists and Their Methods
```markdown
## Creating and Accessing Lists
```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)  # Output: ['Black', 'Green', 'Oolong', 'White']
print(tea_varieties[2])  # Output: Oolong
print(tea_varieties[-1])  # Output: White
print(tea_varieties[1:3])  # Output: ['Green', 'Oolong']
print(tea_varieties[:2])  # Output: ['Black', 'Green']
print(tea_varieties[2:])  # Output: ['Oolong', 'White']
print(tea_varieties[3])  # Output: White
```

## Modifying Lists
```python
tea_varieties[3] = "Herbal"
print(tea_varieties[3])  # Output: Herbal
```

## List Slicing and Assignment
```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties[1:3])  # Output: ['Green', 'Oolong']

# Replacing a slice with another list
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)  # Output: ['Black', 'Lemon', 'Oolong', 'White']

# Replacing a slice with multiple elements
tea_varieties[1:3] = ["Green", "Masala"]
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']

# Inserting elements using slice assignment
tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)  # Output: ['Black', 'test', 'test', 'Green', 'Masala', 'White']

# Removing elements using slice assignment
tea_varieties[1:3] = []
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']
```

## Iterating Over Lists
```python
for tea in tea_varieties:
    print(tea)

# Output:
# Black
# Green
# Masala
# White

for tea in tea_varieties:
    print(tea, end="-")

# Output:
# Black-Green-Masala-White-
```

## Checking Membership in Lists
```python
if "Oolong" in tea_varieties:
    print("I have Oolong tea")

# Output: I have Oolong Tea
```

## List Methods
```python
# Adding elements
tea_varieties.append("Oolong")
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White', 'Oolong']

# Removing elements
tea_varieties.pop()
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']

tea_varieties.remove("Green")
print(tea_varieties)  # Output: ['Black', 'Masala', 'White']

# Inserting elements
tea_varieties.insert(1, "Green")
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']

# Copying lists
tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy.append("Lemon")
print(tea_varieties_copy)  # Output: ['Black', 'Green', 'Masala', 'White', 'Lemon']
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']
```

## List Comprehensions
```python
squared_num = [x**2 for x in range(10)]
print(squared_num)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_num = [y**3 for y in range(11)]
print(cube_num)  # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

## Common List Operations
```python
len(tea_varieties)  # Output: 4

tea_varieties.extend(["Mint", "Chamomile"])
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White', 'Mint', 'Chamomile']

sorted_tea_varieties = sorted(tea_varieties)
print(sorted_tea_varieties)  # Output: ['Black', 'Chamomile', 'Green', 'Masala', 'Mint', 'White']

tea_varieties.sort()
print(tea_varieties)  # Output: ['Black', 'Chamomile', 'Green', 'Masala', 'Mint', 'White']

tea_varieties.reverse()
print(tea_varieties)  # Output: ['White', 'Mint', 'Masala', 'Green', 'Chamomile', 'Black']
```
