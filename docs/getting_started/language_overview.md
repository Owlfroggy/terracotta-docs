## Scripts
Every Terracotta script represents one line of codeblocks in DiamondFire. In other words, each script represents exactly one function, process, or event. These scripts are seperated into two parts: Headers that appear at the top of the file and the code that appears below them. 

Headers determine the type of codeline (e.g. whether a line starts with a PLAYER_EVENT block or a FUNCTION block) and any additional information about it (e.g. the cancel scythe or parameters).

```tc title="Example Event"
# header section
LAGSLAYER_CANCEL;
PLAYER_EVENT Jump;

# code section
game:CancelEvent;
```

```tc title="Example Function"
# header section
FUNCTION sendCenteredMessage;
PARAM message: txt;

# code section
default:SendMessage(line message){"Alignment Mode" = "Centered"};
```

## Semantics

Terracotta is a non-whitespace-significant language that relies on semicolons to separate instructions. This means complex lines can be arbitrarily split up however you see fit because it's ultimately the semicolons that differentiate between them.

```tc title="Both of these statements are valid."
default:DisplayParticleEffect(par("Block",{"Amount" = 10, "Material" = "diamond_block"}));
default:DisplayParticleEffect(
    par(
        "Block",
        {
            "Amount" = 10, 
            "Material" = "diamond_block"
        }
    )
);
```

Anything that involves sectioning off chunks of code (like if statements or loops) does so with curly braces.
```tc title="Example"
if (default?HasPlotPermission{"Permission" = "Owner"}) {
    default:SendMessage("You are the owner!");
}
```
```tc title="Example"
while (default.AttackCooldownTicks > 0) {
    default:GivePotionEffect(pot("Slowness"));
    wait;
}
default:ClearPotionEffects;
```

## Expressions
Nearly every place in Terracotta that accepts a value accepts an expression. This means equations and even other action calls can be inlined, avoiding the need to use temporary variables.

```tc title="Example"
FUNCTION coloredParticleTrail;
PARAM hue: num;

default:DisplayParticleEffect(
    par(
        var:SetToRandom("Entity Effect","Dust"),
        {
            "Amount" = num:Random(1,5),
            "Color" = var:SetToHSBColor(line hue,100,100)
        }
    ),
    loc:ShiftAllAxes(default.Location,0,0.1,0)
);
```
More detailed information on Expressions can be found [here](../language_features/expressions.md).

## Comments
Single-line comments are created using `#`. There is currently no syntax for multi-line comments other than using multiple single-line comments.
```tc
# Sends a message to the player
# TODO: Add color codes
default:SendMessage("Hello world!"); # End-of-line comment

# Code can be commented out to disable it:
#default:PlaySound(snd("Pling"));
```
####
Next: Read more on [Expressions](../language_features/expressions.md), learn about [Item Libraries](), see how [Actions](../codeblocks/action.md) and [Variables](../codeitems/variable.md) work, or just start messing around and reference these docs as needed!