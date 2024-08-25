this is obviously heavily work in progress

# very good and awesome documentation

# THIS CHANGE IS DEPLOYED VIA GITHUB ACTIONS!

```tc
FUNCTION numbergame;

"\u{13487137887} dingus \n akjshdg"

dict:Get:num;

line i: num = saved ["%default number"];

default:SendMessage("The number game!! compiled with terracotta");

repeat Forever {
    line i += 1;
    line rainbowIndex += 1;

    line timeUnit = "Seconds";
    default:SendActionBar(s"The number: <green>" + line i);

    if (default ? IsSprinting) {
        line rngResult = num:Random(1, 20);

        #fish mode
        if (default ? IsSwimming) {
            #increase the number EVEN FASTER!
            line i += 12345678912345;

            default:SetRemainingAir(line rngResult * 30);

            line msg = txt:ParseExpression("<blue>" + "!"*line rngResult + "    <aqua>FISHMODE!!!!!! <rainbow:%var(rainbowIndex)>" + line i + "    <blue>" + "!"*line rngResult);
        }
        #normal sprint mode 
        else {
            line msg = txt:ParseExpression("<light_purple>" + "!"*line rngResult + "    <white>The number: <rainbow:%var(rainbowIndex)>" + line i + "    <light_purple>" + "!"*line rngResult);
        }

        default:SendActionBar(line msg: txt);

        line timeUnit = "Ticks"; #FAST
    }

    if (default ? IsSneaking) {
        default:PlaySound(snd["Anvil Land"]);
        default:SendActionBar(s"<red>You have killed the loop!!! How dare you");
        break;
    }

    if (line i < 0) {
        line rngResult = num:Random(1, 200);
        line msg = txt:ParseExpression("<red><obfuscated>" + "!"*line rngResult + "    <reset><dark_red>what have you done... <#FF0000>" + line i + "    <red><obfuscated>" + "!"*line rngResult);
        default:SendActionBar(line msg: txt);
    }

    saved ["%default number"] = line i;

    #reset code
    if (default ? IsStandingOnBlock("nether_wart_block")) {
        #launching code
        default:LaunchTowardLocation(loc:Align(default.Location - vec[0,1,0]), -100);
        default:GivePotionEffect(pot["Slow Falling",1,2 * 20]);

        if (line i < 0) {
            default:SendActionBar("&c&lFIRST, FIX YOUR MISTAKES");
            line timeUnit = "Seconds";
        } else {
            line i = 0;
            default:SendMessage("You have been reset");
            default:SendActionBar; #clear action bar
        }
    }

    wait(1){"Time Unit" = line timeUnit ? "Seconds"};
}
```

```tc
#100% accurate nether gen open sourced????
LAGSLAYER_CANCEL; PLAYER_EVENT Join;

default:SetToCreativeMode;

#var declarations
saved netherSpawnLoc: loc;
call setupVars;


# fake loading screen
local loadTime = 3*20;

default:SendTitle("&aGenerating...","real not clickbait",local loadTime);
default:GivePotionEffect(pot["Mining Fatigue",255,4*20]){"Show Icon" = "False","Effect Particles" = "None"};
default:GivePotionEffect(pot["Invisibility",255,4*20]){"Show Icon" = "False","Effect Particles" = "None"};
default:GivePotionEffect(pot["Blindness",1,4*20]){"Show Icon" = "False","Effect Particles" = "None"};
start loadLoop;

#teleport to nether
wait(0.5*20);
default:Teleport(global overworldPortalLoc);

wait(5);

#teleport to spawn 
wait(2*20); #wait until player has been shoved back into plot bounds to avoid messing with getNetherLoc()
call getNetherLoc(line shiftedLoc, global netherSpawnLoc);
default:Teleport(line shiftedLoc);
default:SendTitle("","");

default:SetToAdventureMode;
default:SetAllowFlight{"Allow Flight" = "Enable"};
default:GivePotionEffect(pot["Fire Resistance"]){"Effect Particles" = "None","Show Icon" = "False"};

wait(5);

start interactionEntity;

line poweredByLoc: loc;
call getNetherLoc(line poweredByLoc, loc[345,84,338]);
global hasSpawnedEntities = 1;
game:SpawnTextDisplay(line poweredByLoc,"POWERED BY:");
lastEntity:SetDisplayScale(5,5,5);
lastEntity:SetDisplayBillboard{"Billboard Type" = "Fixed"};
lastEntity:SetTextDisplayBackground("#000000",0);
lastEntity:SetTextDisplayTextShadow{"Text Shadow" = "Disable"};
lastEntity:SetDisplayRotationFromEulerAngles(0,180,0);
lastEntity:SetDisplayBrightness(15,15);
```


```tc
FUNCTION DispText;
PARAM text: txt;
PARAM spawnAt: loc;
PARAM size: optional plural any = vec[1,1,1];;

if (var?IsType(line size){"Variable Type" = "Number"}) {
    line size = vec[line size,line size,line size];
}


game:SpawnTextDisplay(line spawnAt,line text);
lastEntity:SetDisplayScale(line size);
lastEntity:SetDisplayRotationFromEulerAngles(loc:GetCoordinate(line spawnAt){"Coordinate" = "Pitch"},loc:GetCoordinate(line spawnAt){"Coordinate" = "Yaw"},0);
lastEntity:SetTextDisplayBackground("#000000",0);
lastEntity:SetTextDisplayTextShadow{"Text Shadow" = "Disable"};
lastEntity:SetDisplayBillboard{"Billboard Type" = "Fixed"};
lastEntity:SetTextDisplayLineWidth(3785);
```