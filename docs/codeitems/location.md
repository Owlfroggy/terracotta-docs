## Syntax
Locations are created using the `loc` constructor. Like all constructors in Terracotta, the values passed into the constructor are [Expressions](../language_features/expressions.md) and can take full advantage of their features.

```tc
loc[X: num, Y: num, Z: num, Pitch: num*, Yaw: num*]
```

`Pitch` and `Yaw` are optional and will default to `0` if omitted.

## Operations

### + (Addition)

#### `loc` + `vec`: `loc`
Adds the XYZ coordinates of the right Vector to the XYZ coordinates of the left Location, leaving Pitch and Yaw untouched.
```tc
loc[10, 50, 10, 90, 180] + vec[1, 2, 3] = loc[11, 52, 13, 90, 180]
```

#### `loc` + `txt`: `txt`
Converts the left Location into a String then adds it at the beginning of the right Styled Text.
```tc
loc[10, 50, 10] + s" is the spawn point!" = s"[10, 50, 10] is the spawn point!"
```

#### `txt` + `loc`: `txt`
Converts the right Location into a String then adds it at the end of the left Styled Text.
```tc
s"The spawn point is: " + loc[10, 50, 10] = s"The spawn point is: [10, 50, 10]"
```

### - (Subtraction)
#### `loc` - `vec`: `loc`
Subtracts the XYZ coordinates of the right Vector from the XYZ coordinates of the left Location, leaving Pitch and Yaw untouched.
```tc
loc[10, 50, 10, 90, 180] - vec[1, 2, 3] = loc[9, 48, 7, 90, 180]
```