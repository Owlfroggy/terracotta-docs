To turn a string into a Styled Text, prefix it with `s`.

```tc
default:SendMessage(s"<green><bold>Welcome to", s'<rainbow>awesome skyminer!');
```

[Escape Sequences](string.md/#escape-sequences) work the same in Styled Texts as they do in Strings.

[Ampersand Conversion](string.md/#color-codes-ampersand-conversion) does not occur at all in Styled Texts.
```tc
# this & will not get converted even though &a is a color code:
default:SendMessage(s"&aawesome message"); # &aawesome message
```

## Operations
### + (Addition)
#### `txt` + `any`: `txt`
Converts the right value into a String then adds it onto the end of the left Styled Text.
```tc
s"Spawn point: " + loc(10,50,10) = s"Spawn point: [10,50,10]"
s"Unlocks: " + ["Diamond Sword", "Health Up"] = s"Unlocks: [Diamond Sword, Health Up]"
```

#### `any` + `txt`: `txt`
Converts the left value into a String then adds it at the beginning of the right Styled Text.
```tc
15 + s" <red>seconds left!" = s"15 <red>seconds left!"
```