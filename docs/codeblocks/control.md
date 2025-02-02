Instead of taking the form of `block:Action` like most other actions, all parts of the control block's functionality get their own keywords.

## Wait
Wait exists as a standalone function.
```tc
wait(10){"Time Unit" = "Minutes"};
default:SendMessage("Bored yet?");
```

Like other functions in Terracotta, neither arguments nor tags are required. Leaving out arguments will default to a wait time of 1; leaving out tags will default to a unit of ticks.

```tc
repeat Forever {
    allPlayers:DisplayParticleEffect(par["Flame"],default.Location);
    wait; #waits for one tick
}
```

## Return
Return uses the `return` keyword. For information on how to return values, see [Return Value](function.md#return-value).

```tc
if (num:Random(1,2) == 2) {
    return;
}

default:SendMessage("You got lucky!");
```

## End Thread
End Thread uses the `endthread` keyword.

```tc
repeat Forever {
    if (not selectionEntity?Exists) {
        endthread;
    }
    selectionEntity:Heal(100);
}
```

## Continue (Skip Iteration)
The `continue` word acts as a SkipIteration control block.

```tc
for (local i on Range(1,10)) {
    if (local i == 7) {
        continue;
    }
    default:SendMessage(local i);
}
```

The continue keyword does not need to be within a loop. When placed at the top level of a function, it will skip an iteration of the loop that called that function. If the continue keyword is contained by no loops at all, it will do nothing.

```tc
FUNCTION SkipLogic;
if (local i == 7) {
    continue;
}
```

```tc
FUNCTION Loop;

for (local i on Range(1,10)) {
    #this behaves exactly the same as the earlier continue example
    call SkipLogic;
    default:SendMessage(local i);
}
```

## Break (Stop Repeat)
The `break` keyword acts as a StopRepeat control block.

```tc
for (local i on Range(1,10)) {
    if (local i == 7) {
        break;
    }
    default:SendMessage(local i);
}
```

All the same placement rules that apply to `continue` apply to `break`.