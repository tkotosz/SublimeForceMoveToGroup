# SublimeForceMoveToGroup
Sublime Plugin to force move view to group

By default sublime has key binding to switch between groups:

ctrl+1: focus group 0

ctrl+2: focus group 1

... and so on until ctrl+9

in addition to this it has key binding to move the current view (tab) to a group:

ctrl+shift+1: move to group 0

ctrl+shift+2: move to group 1

... and so on until ctrl+shift+9

The problem is that ctrl+shift+num only moves the file to the given group if the groups exists. Also if you move the last file out of the group then it still leaves the group open. There are key bindings for creating a new group or closing one, but using 4 different key binding for create, close, move and switch sounds a bit weird.

So this `SublimeForceMoveToGroup` command automates group create and close for you.

For example you can setup the following key-bindings:
```
{ "keys": ["ctrl+shift+1"], "command": "force_move_to_group", "args": { "group": 0 } },
{ "keys": ["ctrl+shift+2"], "command": "force_move_to_group", "args": { "group": 1 } },
```
This will override the default "move_to_group" bindings. Then you are good to go.

If you have a few tabs open then just pick one then "ctrl+shift+2", then that tab will move to new group so you can view it side-by-side with other files. You can switch between the left and right group with ctrl+1 and ctrl+2 (default key bindings) and you can move any tab from right to left with "ctrl+shift+2" and from left to right with "ctrl+shift+1". I think it is much easier to remember "ctrl+num" for navigating between groups and "ctrl+shift+num" to move tabs between groups.
Oh and also if you you move the last tab from left to right (so no more tab left in group 2) then it will automatically close that empty group. :)
