## Syntax
Any identifier starting with a digit, a period, or a `.` will be treated as a number. Numbers can also contain underscores between digits which can provide visual clarity without affecting the value of the number.

```tc
# These are all valid numbers:
1 0.5 .5 -1 -.823 1_000_000
```

The compiler will not prevent you from including more than 3 decimal places in a number, however the extra digits will be truncated when processed by DiamondFire due to its precision limit.

```tc
global PI = 3.14159;
default:SendMessage(global PI); # 3.141
```

There is currently no way to manually write %math expressions. For equations, Terracotta's [Expressions](../language_features/expressions.md) should be used.

## Operations
### + (Addition)
#### `num` + `num`: `num`
Adds the left and right Numbers together.
```tc
2 + 2 = 4 # Not 5
```

#### `num` + `str`: `str`
Converts the left Number into a String then adds it onto the beginning of the left String.
```tc
15 + " killstreak!" = "15 killstreak!"
```

#### `num` + `txt`: `txt`
Converts the left Number into a String then adds it at the beginning of the right Styled Text.
```tc
15 + s" <red>seconds left!" = s"15 <red>seconds left!"
```

#### `str` + `num`: `str`
Converts the right Number into a String then adds it onto the end of the right String.
```tc
"Coins: " + 5 = "Coins: 5"
```

#### `txt` + `num`: `txt`
Converts the right Number into a String then adds it onto the end of the left Styled Text.
```tc
s"Your level: " + 20 = s"Your level: 20"
```

### - (Subtraction)

#### `num` - `num`: `num`
Subtracts the right Number from the left Number.
```tc
10 - 6 = 4
```

### * (Multiplication)

#### `num` * `num`: `num`
Multiplies the two Numbers together.
```tc
4 * 5 = 20
```

### / (Division)

#### `num` / `num`: `num`
Divides the left Number by the right Number.
```tc   
2 / 4 = 0.5
```

### ^ (Exponentiation)

#### `num` ^ `num`: `num`
Raises the left Number to the power of the right Number.
```tc
2 ^ 10 = 1024
```

### % (Modulus)
Returns the modulus of the left Number and the right Number.
```tc
43 % 20 = 3
```