## Syntax
Vectors are created using the `vec` constructor. Like all constructors in Terracotta, the values passed into the constructor are [Expressions](../language_features/expressions.md) and can take full advantage of their features.

```tc
vec[X: num, Y: num, Z: num]
```

## Operations

### + (Addition)

#### `vec` + `vec`: `vec`
Adds the XYZ coordinates of the Vectors together.
```tc
vec[5,10,15] + vec[3,2,1] = vec[8,12,16]
```

#### `loc` + `vec`: `loc`
Adds the XYZ coordinates of the right Vector to the XYZ coordinates of the left Location, leaving Pitch and Yaw untouched.
```tc
loc[10, 50, 10, 90, 180] + vec[1, 2, 3] = loc[11, 52, 13, 90, 180]
```

#### `vec` + `txt`: `txt`
Converts the left Vector into a String then adds it at the beginning of the right Styled Text.
```tc
vec[0, 42, 0] + s" is a cool vector!" = s"<0, 42, 0> is a cool vector!"
```

#### `txt` + `loc`: `txt`
Converts the right Vector into a String then adds it at the end of the left Styled Text.
```tc
s"Very cool vector: " + vec[0, 42, 0] = s"Very cool vector: <0, 42, 0>"
```

### - (Subtraction)

#### `vec` - `vec`: `vec`
Subtracts the XYZ coordinates of the right Vector from the XYZ coordinates of the left Vector.
```tc
vec[5,10,15] - vec[3,2,1] = vec[2,8,14]
```

#### `loc` - `vec`: `loc`
Subtracts the XYZ coordinates of the right Vector from the XYZ coordinates of the left Location, leaving Pitch and Yaw untouched.
```tc
loc[10, 50, 10, 90, 180] - vec[1, 2, 3] = loc[9, 48, 7, 90, 180]
```

### * (Multiplication)

#### `vec` * `num`: `vec`
Multiplies the length of the left Vector by the right Number.
```tc
vec[2,0,1] * 3 = vec[6,0,3]
```

### / (Division)

#### `vec` / `num`: `vec`
Divides the length of the left Vector by the right Number.
```tc
vec[10,5,0] / 2 = vec[5,2.5,0]
```