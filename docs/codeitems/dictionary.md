## Syntax
Dictionaries are created by enclosing key-value pairs in curly braces and seperating them with commas. Keys must be strings. Values can be expressions but keys cannot.

```tc
line itemData = {
    "name" = "Void Sword",
    "damage" = 14 * global,
    "rarity" = "Rare",
};
```

Dictionaries can hold a maximum of 5,000 values. Nested lists/dictionaries and their values count towards that total.

## Indexing
To access values inside of a dictionary, use the [Indexing Operation](../language_features/expressions.md#indexing-operation).

## Iteration
To iterate over a dictionary, use a for .. in loop.
```tc title="Example"
for (line key, line value in {"name" = "Greg", "age" = 32}) {
    default:SendMessage(line key,"is equal to",line value);
}
```
Note that when using a variable of an unknown type (like a global variable declared in another file) its type must be manually specified in order to iterate over it.
```tc title="Example"
for (line key, line value in global dataDeclaredElsewhere: dict) {
    default:SendMessage(line key,"is equal to",line value);
}
```

## Nesting
Lists and dictionaries can be nested. However, it's important keep in mind that DiamondFire tends to pass lists and dictionaries as copies not references so behavior regarding nested data may not be intuitive.

```tc title="Example"
line itemData = {
    "name" = "Diamond Sword",
    "enchantments" = {
        "sharpness" = 5
    }
};

# this variable will grab a COPY!
line enchantments = line itemData["enchantments"]: dict;
default:SendMessage(line enchantments); # {sharpness: 5}

# modifications to the copy will NOT modify the original list
line enchantments["knockback"] = 2;
default:SendMessage(line enchantments); # {sharpness: 5, knockback: 2}
default:SendMessage(line itemData["enchantments"]); # {sharpness: 5}
```

## Operations
### + (Addition)
#### `txt` + `dict`: `txt`
Converts the right Dictionary into a String then adds it onto the end of the left Styled Text.
```tc
s"Settings: " + {"theme" = "dark"} = s"Abilities: {theme: dark}"
```

#### `dict` + `txt`: `txt`
Converts the left Dictionary into a String then adds it at the beginning of the right Styled Text.
```tc
{"theme" = "light"} + s" is concerning..." = s"{theme: light} is concerning..."
```