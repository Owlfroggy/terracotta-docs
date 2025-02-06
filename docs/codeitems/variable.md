## Syntax

Variables are accessed by a scope keyword followed by a name.
```tc
global gameVariable
saved savedVariable
local localVariable
line lineVariable
```

In DiamondFire, variables do not need to be declared, so they don't need to be declared in Terracotta either. Think of variables in Terracotta as one-to-one representations of variable code items.

This means that whenever a variable is being referenced, you must provide its scope. This holds true even if a variable of that name has been referenced with a given scope already.

```tc
local message = "Hello world!";

# specifying the scope here is REQUIRED!
default:SendMessage(local message);

# any scope can be used
default:SendMessage(local message, global message);
```

## String Names
To use text codes or special characters in variable names, wrap the variable name in a string and wrap the string in square brackets.

```tc
global ["%var(team) playerCount"] = game.SelectionSize;
saved ["%uuid gamesPlayed"] += 1;
```

!!! warning "This string value does not accept expressions! It must be a single string literal."

## Types

Variable types only matter when using variables in [Expressions](../language_features/expressions.md). For any other uses like inserting them into arguments, types do not matter. As of now, there is no strict typing mode.

Terracotta has a level of type inference built in. Types can be inferred in the following scenarios:

??? info "Type inference scenarios (click to expand)"
    1. Setting a variable to a value
    ```tc
    # type is inferred as vector for future uses of the variable
    global var = vec[1,2,3];
    ```
    
    2. Setting a variable to the result of a function
    ```tc
    # type is inferred as string for future uses of the variable
    global blockData = var:GetAllBlockData(default.TargetBlockLocation);
    ```

    3. Any action that has a return type controlled by tags
    ```tc
    # type is inferred as item for future uses of the variable
    global itemType = item:GetMaterial(default.MainHandItem){"Return Value Type" = "Item"};
    ```
    ```tc
    # type is inferred as string for future uses of the variable
    global itemType = item:GetMaterial(default.MainHandItem){"Return Value Type" = "Item Name (Golden Apple)"};
    ```

    4. SetToRandom if all arguments are the same type
    ```tc
    # type is inferred as location for future uses of the variable
    global teleportLoc = var:SetToRandom(loc[10,50,10], loc[52,27,88], global spawnLoc: loc);
    ```
    ```tc
    # type remains unknown
    global teleportLoc = var:SetToRandom(50,"fifty");
    ```
    
    5. Inside if var?IsType
    ```tc
    if (var?IsType(saved ["%uuid trail"]){"Variable Type" = "Particle"}) {
        # type is inferred as particle inside this if block
    }
    # outside the if block, type remains unknown
    ```

    6. Accessing parameter values
    ```tc
    FUNCTION DisplayEffect;
    PARAM effect: par;
    # type is inferred as particle for future uses of the line variable 'effect'
    ```
    

In many cases, like accessing globals created in other scripts, that's not enough. So, anywhere a variable is referenced, it can specify its expected type by putting `: <type>` after the variable name.

```tc
line definitelyAString: str
```

When specified in an expression, the type hint is local to that one use of the variable.

```tc
FUNCTION GoToSpawn;

default:Teleport(global spawnLocation: loc + vec[0,1,0]);
wait(20);

# this will fail to compile because the compiler doesn't know the type of spawnLocation
default:Teleport(global spawnLocation + vec[0,10,0]);
```

Types can be given to variables on their own and will persist for the rest of the file unless overridden.

```tc
FUNCTION GoToSpawn;

# spawnLocation will have type 'loc' for the rest of the script
global spawnLocation: loc;

default:Teleport(global spawnLocation + vec[0,1,0]);
wait(20);
default:Teleport(global spawnLocation + vec[0,10,0]);
```