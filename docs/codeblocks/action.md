## Syntax
Action syntax is as follows:
```tc
target:Action(arguments){tags};
```

### Arguments

Arguments are values seperated by commas. Arguments with no value are converted to empty slots.
```tc
default:SendMessage("Hello","world!");
default:SendMessage(  ,"Slot 2 string",  ,  ,"Slot 5 string");
```

### Tags

Tag syntax can be thought of as a dictionary:
```tc
default:SendMessage("Tags!"){"Alignment Mode" = "Centered", "Inherit Styles" = "True"};
```
To use a variable as the tag value, a default must be provided immediately after:
```tc
default:SendMessage("Tags!"){"Alignment Mode" = global messageMode ? "Centered"};
```
If you are using the vscode extension, you can use the autocomplete shortcut (`ctrl+space` by default) to quickly insert tag names and values.

Arguments and tags are both optional and can be left out, making all of these valid action calls:
```tc
default:StopSounds(snd["Pling"]);
default:StopSounds{"Sound Source" = "Jukebox/Note Blocks"};
default:StopSounds;
```

## Player Actions

Player actions use the following targets:

- `default`
- `killer`
- `damager`
- `shooter`
- `victim`
- `allPlayers`
- `selection`

```tc title="Examples"
default:GivePotionEffect(pot["Saturation"]){"Effect Particles" = "None", "Overwrite Effect" = "False"};

default:SetVisualShoulderParrot{"Shoulder" = "Left", "Type" = "Cyan"};

allPlayers:SendMessage(s"<green>%default<white>has joined!");

selection:SetToCreativeMode;

victim:Heal(game.EventDamage/2);

shooter:GiveItems(item["Arrow"]);
```


## Entity Actions

Entity actions use the following targets:

- `selectionEntity`
- `defaultEntity`
- `killerEntity`
- `damagerEntity`
- `shooterEntity`
- `victimEntity`
- `allEntities`
- `allMobs`
- `projectile`
- `lastEntity`

```tc title="Examples"
defaultEntity:Teleport(default.Location + vec[0,10,0]);

defaultEntity:EatGrass;

selectionEntity:Damage(5);

projectile:SetArrowNoClip{"Has NoClip" = "Enable"};

allMobs:FaceLocation(default.Location)

lastEntity:SetTag("owner","%default");
```

## Game Actions

Game actions use the `game` target. 

```tc title="Examples"
game:SpawnMob(item["zombie_spawn_egg"],game.EventBlockLocation);

game:CancelEvent;

game:SummonLightning(victim.Location);

game:SetBlock(loc[10,50,10],item["beacon"]);
```

