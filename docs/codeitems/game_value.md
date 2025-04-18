## Syntax
If action syntax is like calling a method on a target, game value syntax is like accessing a property:
```tc
target.Value
```

Values in the `Event Values` and `Plot Values` category can be accessed with the `game` target.
```tc title="Example"
game.EventItem
game.DamageEventCause
game.ServerTPS
game.PlayerCount
```

Values that apply to entities can be accessed using the following targets:

- `selectedEntity`
- `defaultEntity`
- `killerEntity`
- `damagerEntity`
- `shooterEntity`
- `victimEntity`
- `projectile`
- `lastEntity`

```tc title="Example"
selectedEntity.SaddleItem
victimEntity.CurrentHealth
lastEntity.UUID
```

Values that apply to players can be accessed using the following targets:

- `default`
- `killer`
- `damager`
- `shooter`
- `victim`
- `selected`

```tc title="Example"
default.Name
victim.EyeLocation
selected.AttackCooldownTicks
```