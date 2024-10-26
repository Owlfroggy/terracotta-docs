Selections in Terracotta work 1:1 with how they work in DiamondFire.

Selections can be created using the `select` keyword followed by an action. They can be filtered by using the `filter` keyword.

```tc
select AllPlayers;
filter Randomly(2);

global ["%selected isHunter"] = 1;
```

For selection actions that use a condition, put the condition immediately after the action name. Note that `player` and `entity` targets must be used in order to access if player or if entity conditions.

```tc
select PlayersByCondition player?IsLookingAtBlock(item["emerald_block"]);
filter ByCondition global ["%default isInGame"] == 1;

selection:SendMessage("You live!");

select Inverse;
filter ByCondition global ["%default isInGame"] == 1;

selection:Damage(999);
```

To reset the selection (equivalent to the block Select Object -> Reset) use:
```tc
select Nothing;
```