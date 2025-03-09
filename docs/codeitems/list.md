## Syntax

Lists are created by enclosing values in square brackets and seperating them with commas. The final value is allowed to have a trailing comma.

```tc
line fruits = ["apple","orange","pear"];

line vegetables = [
    "corn",
    "brocoli",
    "carrot", # this comma is allowed 
];
```

Lists can hold a maximum of 10,000 values. Nested lists/dictionaries and their values count towards that total.

## Indexing
To access values inside of a list, use the [Indexing Operation](../language_features/expressions.md#indexing-operation).

Lists start at index `1`, NOT `0`.

!!! warning "DiamondFire Jank"
    Attempting to set to an index that is out of bounds of the list will instead overwrite the final value.
    ```tc
    line unlocks = ["doubleJump","teleport"];
    line unlocks[3] = "dash"; # overwrites "teleport"

    default:SendMessage(line unlocks); # [doubleJump, dash]
    ```

    To add values to lists, use `list:Append()`
    ```tc
    line unlocks = ["doubleJump","teleport"];
    list:Append(line unlocks,"dash");

    default:SendMessage(line unlocks); # [doubleJump, teleport, dash]
    ```

## Iteration
To iterate over a list, use a for .. in loop.
```tc title="Example"
for (line value in [1,17,400_006]) {
    default:SendMessage(line value);
}
```
Note that when using a variable of an unknown type (like a global varaible declared in another file) its type must be manually specified in order to iterate over it.
```tc title="Example"
for (line value in global numbersDeclaredElsewhere: list) {
    default:SendMessage(line value);
}
```

## Nesting
Lists and dictionaries can be nested. However, it's important keep in mind that DiamondFire tends to pass lists and dictionaries as copies not references so behavior regarding nested data may not be intuitive.

```tc title="Example"
line teamConfigurations = [
    ["red","blue"],
    ["green","yellow"]
];

# this variable will grab a COPY!
line firstEntry = line teamConfigurations[1]: list;
default:SendMessage(line firstEntry); # [red, blue]

# modifications to the copy will NOT modify the original list
line firstEntry[2] = "yellow";
default:SendMessage(line firstEntry); # [red, yellow]
default:SendMessage(line teamConfigurations[1]); # [red, blue]
```

## Operations
### + (Addition)
#### `txt` + `list`: `txt`
Converts the right list into a String then adds it onto the end of the left Styled Text.
```tc
s"Abilities: " + ["doubleJump","dash"] = s"Abilities: [doubleJump, dash]"
```

#### `list` + `txt`: `txt`
Converts the left list into a String then adds it at the beginning of the right Styled Text.
```tc
["Red Team","Blue Team"] + s" have tied the match!" = s"[Red Team, Blue Team] have tied the match!"
```