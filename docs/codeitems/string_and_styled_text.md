## Syntax
Strings can use either single or double quotes and compile directly to DiamondFire String items.

```tc
default:SendMessage("double quote string", 'single quote string');
```

Prefixing any string with `s` will turn it into a Styled Text.
```tc
default:SendMessage(s"<rainbow><b>Hello world!");
```

## Color Codes (Ampersand Conversion)

When ampersands (`&`) are immediately proceeded by a character that makes a valid [formatting code](https://minecraft.wiki/w/Formatting_codes), they are automatically converted to section symbols (`§`) to make that formatting code functional. To prevent ampersands from being converted at all, they can be escaped (see [Escape Sequences](#escape-sequences)).

```tc
# this message will show up green:
default:SendMessage("&acolored text"); # colored text

# this message will show up white:
default:SendMessage("\&aun-colored text"); # &aun-colored text

# this ampersand doesn't need to be escaped at all:
default:SendMessage("good & evil"); # good & evil
```

Ampersand conversion does NOT occur in Styled Text.
```tc
# this & will not get converted even though &a is a color code:
default:SendMessage(s"&aawesome message"); # &aawesome message
```

## Escape Sequences
Quotes, ampersands, and backslashes themselves can all be escaped by immediately proceeding them with a backslash.

```tc
default:SendMessage('jeff\'s',"\"amazing\"","creation"); #jeff's "amazing" creation
default:SendMessage("/ iron\&diamonds \\"); #/ iron&diamonds \
```

Newlines can be inserted using \n
```tc
default:SendMessage("%default's stats:\nCoins: %var(%default coins)\nLevel: %var(%default level)");
```

### Unicode Characters
Unicode characters be inserted using the `\u` escape code. This is especially useful when working with custom UI elements.

!!! warning
    Unicode escape sequences are evaluated at compile time. Due to this, the following is invalid:
    ```tc title="This will NOT compile!"
    line characterCode = "2620";

    default:SendMessage("\u%var(characterCode)");
    ```


#### Four Digits
Four digit unicode characters can be inserted using `\uXXXX`, where each X is a hexadecimal digit.
```tc
default:SendMessage("\u2620 You died!") # ☠ You died!
```

#### More or Less Digits
Unicode characters with more or less than 4 digits can be inserted using `\u{}`, with any number of hexadecimal digits inside the braces.

```tc
default:SendMessage("\u{1F525}"); # 🔥
default:SendMessage("\u{44}\u{46}"); # DF
```
