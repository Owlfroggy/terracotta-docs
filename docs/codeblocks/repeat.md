## Repeat Loops
Repeat Forever loops use the `repeat` keyword:
```tc
# this will repeat infinitely unless it contains a break keyword
repeat {
    # code...
}
```

Repeat Multiple loops use the `repeat` keyword followed by the number of times it should repeat wrapped in parentheses:
```tc
# will repeat 10 times
repeat (10) {
    # code...
}
```
The index can be gotten by a variable using the `to` keyword:
```tc
repeat (line index to 3) {
    # code...
}
```

## For Loops
For loops use the `for` keyword and come in two types, `on` and `in`.

### On Loops
For loops using the `on` keyword are used to access Repeat actions like `Repeat On Path` and `Repeat Adjacently`. Their syntax is as follows:
```tc
for (value on Action(args){tags}) {
    # code...
}
```
The following actions are supported:

- `Adjacent`
- `Grid`
- `Path`
- `Range`
- `Sphere`

```tc title="Example"
for (line l on Path(attacker.EyeLocation,victim.Location)) {
    allPlayers:DisplayParticleEffect(par("Flame"));
}
```

```tc title="Example"
for (line i on Range(5,10,2)) {
    default:SendMessage(line i);
}
```

### In Loops
For loops using the `in` keyword are used to iterate over lists and dictionaries. Their syntax is as follows:
```tc
for (value in list) {

}
for (key, value in dict) {

}
```
Lists/dicts can be inlined, or variables can be used.
```tc title="Variable Example"
line data = {
    "key" = "value",
    "apples" = "oranges"
};

for (line k, line v in line data) {
    default:SendMessage(line k, line v);
}
```
```tc title="Inlining Example"
for (line particle in [par("Flame"),par("Cloud")]) {
    allPlayers:DisplayParticleEffect(default.Location,line particle);
}
```

In order for variables of an unknown type to be iterated over, they must have their type manually specified using a [Type Override](../language_features/expressions.md#type-overrides). Additionally, the types of the variables to the left of the `in` keyword can also have their types overridden.

```tc title="Example"
for (line ability in saved ("abilities %uuid"): list) {
    # code...
}
```
```tc title="Example"
for (line skill, line level: num in saved ("skills %uuid"): dict) {
    # code...
}
```

## While Loops

While loops use the `while` keyword followed by a condition wrapped in parentheses:
```tc title="Example"
while (condition) {
    # code...
}
```
The condition will be re-evaluated for every iteration, meaning actions and functions in the condition will be called repeatedly.

For information on how to write conditions, see [Conditional Expressions](../language_features/expressions.md#conditional-expressions). **Note that `player` and `entity` targets must be used in order to access if player or if entity conditions.**

```tc title="Example"
while (num:Random(1,10) != 10) {
    default:SendMessage("Still going!");
    wait;
}
```
```tc title="Example"
while (!player?IsStandingOnBlock(item("obsidian"))) {
    default:Damage(1);
    wait(20);
}
```