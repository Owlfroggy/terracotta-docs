# Expressions

For uses of the Set Variable block not covered by the operators listed below, see [Set Variable](../codeblocks/set_var.md)

You can write an expression *almost* anywhere you can put a value.

```tc title="Examples"
line reward = num:Round(game.PlayerCount * global coinBonus * (global ["%default killstreak"] + 10));

default:Teleport(default.Location + (default.Direction * global ["%default teleportRange"]));

default:GivePotionEffect(pot["Speed", 1, (10*20) + num:Random(0,global maxPotionBonus)]);
```

## Value Operators

!!! info
    Many operators work on more types of code items than just numbers. For more info on which operators work with which code items, check out the code items' respecitve pages under the Code Items category.

Terracotta supports the following operators:

 - `+` - Addition
 - `-` - Subtraction
 - `*` - Multiplication
 - `/` - Division
 - `^` - Exponentiation
 - `%` - Modulo

Operations between constants are evaluated at compile-time, meaning you can use them safely for convenience without having to worry about using CPU. In the below example, `5 * 20` is directly added to the template as the number `100` and never creates any codeblocks. This applies to all code items, not just numbers.

```tc
wait(5 * 20){"Time Unit" = "Ticks"};
```

## Inlined Functions
Any function that returns a value can be used in expressions. Some actions like Set Location Coordinate don't have a return value listed in their description, still return a value anyway. Generally, if an action has `Variable - Variable to set` as its first parameter, it can be inlined.

Custom functions cannot be inlined yet as they cannot specify return types, however this functionality will be added in a future update.

```tc title="Examples"
default:SendMessage("You rolled a " + num:Random(1,6) + "!");

default:GiveItems(item[var:SetToRandom("cooked_porkchop","cooked_beef","golden_carrot"),16]);
```

## Incrementors
Incrementors do an operation to a variable without having to write out `variablename = variablename <operation> <value>`.

```tc title="Incremetors"
global added      += 10;
global subtracted -= 2389;
global multiplied *= 100;
global divided    /= 10;
global exponented ^= 3;
global moduloed   %= 2;
```

## Type Overrides
Terracotta has some type inference built in, so for many situations (especially those involving numbers or variables that are declared inside the file you're working in) you won't have to worry about types. Sometimes though, the type of a value is unknown and must be specified manually in order to use it with operations. This can be done by adding `: <type>` after the value.

In the below case, `spawnLocation`'s type is unknown. For the compilier to know what to do when adding the vector to it, you have to manually specify that it's a location.
```tc
default:Teleport(global spawnLocation: loc + vec[1,10,1]);
```


Specifying the type of a variable every time you use it would suck, so you can also assign a type to variables outside of expressions
```tc
global spawnLocation: loc;

# compilier now knows for both of these lines that `spawnLocation` is a location
default:Teleport(global spawnLocation + vec[0,10,0]);
wait(1){"Time Unit" = "Seconds"};
default:Teleport(global spawnLocation + vec[0,20,0]);
```


Type overrides can also be applied to indexing operations and actions/functions that return multiple types.

```tc
default:Teleport(global spawnLocationDict["main"]: loc + vec[0,10,0]);

line newTag = item:GetTag(global item,"cooltagname"): num + 10;
```


## Indexing Operation

Values in lists and dicts can be accessed via square bracket syntax from within expressions.

```tc
line dict = {
    "very awesome key" = "even more awesome value"
};
default:SendMessage(line dict["very awesome key"]);

line list = [1,2,"buckle my shoe"];
default:SendMessage(line list[3]);
```

!!! warning
    Even though you *can* easily do the same index operation in multiple places, it's not recommended. Every index operation creates more codeblocks, which uses more CPU. For this reason, if you know a value is not going to change, it's best to only index once and store the result in a variable.

    ```tc title="Bad"
    global locations = {
        "spawn" = loc[10,50,10]
    };

    default:SendMessage("Teleporting to location", global locations["spawn"]);
    default:Teleport(global locations["spawn"]);
    ```

    ```tc title="Good"
    global locations = {
        "spawn" = loc[10,50,10]
    };

    line selectedLocation = global locations["spawn"]

    default:SendMessage("Teleporting to location", line selectedLocation);
    default:Teleport(line selectedLocation);
    ```

    It's true that the above example is a bit unnecessary, but in loops or when using indexing operations that treverse multiple levels the saved CPU can really add up.

Indexes can themselves be expressions
```tc
line scores = [23,925,78,873];
default:SendMessage(line teamScores[num:Random(1,4)]);

line teams = {
    "red" = {
        "points" = 12
    },
    "blue" = {
        "points" = 15
    }
};
line teamData = line teams[var:SetToRandom("red","blue")];
```

If the type of a value is unknown, it must be manually specified in order to index into it. The indexing operation can appear directly after the type override; no extra parentheses are needed.
```tc
default:SendMessage(global dict_declared_elsewhere: dict["cool_key"]);
default:SendMessage(global list_declared_elsewhere: list[5]);
```

Multiple levels can be traversed, however you will have to manually specify the type of each level.
```tc
line gameState = {
    "redTeam" = {
        "unlocks" = ["damageBoost","healthBoost"]
    }
};

line firstUnlock = line gameState["redTeam"]:dict["unlocks"]:list[1];
```

## Order of Operations

Unlike a certain expression system used by DiamondFire that **shall not be named**, Terracotta expressions follow a sane order of operations.

Things closer to the top of the list are evaluated before things closer to the bottom. Things on the same line are evaluated left-to-right with the same priority.

- Nested expressions (parentheses), indexing into dicts/lists, and function calls (actions, constructors)
- Exponentiation (`^`)
- Multiplication, division, and modulo (`*`, `/`, `^`)
- Addition and subtraction (`+`, `-`)
- Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`)