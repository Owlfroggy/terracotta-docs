## Defining Functions
A script can be declared as a function by including the `FUNCTION` header at the top of it. Function names can be given special characters using the same syntax as variables.
```tc
FUNCTION FunctionName;
# code here
```

```tc
FUNCTION ["function with special chars!!"];
# code here
```

### Parameters
Parameters can be added to the function using the `PARAM` header. The order the headers are listed will be the order the arguments appear in when calling. Parameter names can be given special characters using the same sytax as variables.

```tc
PARAM paramName: type;
PARAM ["parameter with special chars!!"]: type;
```

Parameters can be made optional, plural, or both by putting the `optional` and `plural` keywords before the type.

```tc
FUNCTION killPlayer;
PARAM killCauses: plural str;
PARAM assisterUUID: optional str;
PARAM itemsToDrop: optional plural item;
```

Optional parameters can specify a default value by placing an equal sign and the value after the type.

```tc
FUNCTION startGame;
PARAM gameMode: optional str = "deathmatch";
```

To access the values passed into a parameter, use a line variable of the same name.
```tc
FUNCTION sendRedMessage;
PARAM message: str;

default:SendMessage("&c" + line message);
```

!!! warning "Limiations"
    Due to the quirks of DiamondFire, parameters have a few limitations that are uncommon to encounter but still important to know:
    
    - Functions cannot have more than 26 parameters.
    - Parameters that are both optional *and* plural cannot specify default values.
    - Parameters typed as lists or dictionaries cannot specify default values.
    - Parameters typed as variables cannot have the optional or plural modifiers applied.    


### Return Value
Functions can specify a return type using the `RETURNS` header. This also allows the function to be used in [expressions](../language_features/expressions.md). 

If a `RETURNS` header is present, a value can be placed after the `return` keyword to return it.

```tc
FUNCTION getRandomNumber;
RETURNS num;

return num:Random(1,10);
```

## Calling Functions
Functions can be called using the `call` keyword followed by the function's name. 

```tc
call FunctionName;
call ["function with special chars!!"];
```

Arguments can be provided inside parentheses following the function name.
```tc
call startGame("elimination");
```

If a function returns a value, it can be used in expressions.

```tc
line result = call getRandomNumber(1,10);
saved ["%uuid xp"] += saved ["%uuid xpBoost"] * call getRandomNumber(20,30);
```