# Terracotta

!!! warning "WIP"
    These docs are very work in progress! If you have any questions about Terracotta not answered by this incomplete documentation, ask in [the Discord server](https://discord.gg/at9uBFXPxy).

[DiamondFire](https://www.mcdiamondfire.com) is a Minecraft server where you can make your own minigames using block code.

I do not like block code.

Terracotta is a text-based programming language that compiles to DiamondFire templates with the goal of *actually* making plot development easier. Unlike previous text-to-df languages, Terracotta makes no compromises when it comes to functionality or convenience. Everything you can do with DiamondFire blocks is just as easy or easier in Terracotta.

To get started, visit [Installation Guide](getting_started/installation_guide.md) then [Plot Setup](getting_started/plot_setup.md).

## Why Terracotta is awesome

- Expressions. Almost anywhere you can put a value in Terracotta, you can write an expression. You never have to think about %math again!

- Automatic codeline splitting. Codelines that are too long for your plot will be automatically split into 
multiple functions.

- Intellisense/autocomplete support. Remembering specific names of actions sucks, so you can get autocomplete to do it for you. Also supports completion of variable names, function names, action tags, potion effect ids, etc.

- Item libraries. Items can be edited right in your Minecraft client then easily referenced in code. In-lined NBT *is* in fact a war crime.

- Human-compatable syntax. Terracotta looks and feels like an actual programming language, not like bytecode.

- Automated template placement. Going from Terracotta code to a playable plot is as easy as pressing `f5`. (thanks CodeClient!)

And of course, being a text based programming language, you get all sorts of nice things you don't get through normal DiamondFire like comments, copy+paste, improved readability, etc.