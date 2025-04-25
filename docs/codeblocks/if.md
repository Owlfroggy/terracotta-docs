For information on how to write conditions, see [Conditional Expressions](../language_features/expressions.md#conditional-expressions).

## If Statements
If statements use the `if` keyword followed by a condition wrapped in parentheses:
```tc
if (condition) {
    # code
}
```
Because there are no logic operators yet, if statements can only check one condition at a time.

## Else
Else statements can be placed immediately after an if statement using the `else` keyword:
```tc
if (condition) {
    # code
} else {
    # other code
}
```
As of now there is no 'else if' functionality, but this is likely to change in the future.