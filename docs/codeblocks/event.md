## Syntax
A script can be declared as a player or entity event by including its corresponding header at the top of it. 

```tc
PLAYER_EVENT EventName
ENTITY_EVENT EventName
```

A single project cannot have multiple files declared as the same event.

## Lagslayer-Cancel

If an event is clickable with the cancel scythe, the `LAGSLAYER_CANCEL` header can be included to automatically cancel it if the plot code is halted due to lagslayer. This header can be placed either before or after the main event header.

```tc
PLAYER_EVENT Jump;
LAGSLAYER_CANCEL;

game:CancelEvent;
```