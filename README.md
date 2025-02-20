# Botshot-Roulette

This is a decision tree builder for the game "Buckshot Roulette". Ideally, this classifier will help the user decide what action to take on their turn (shoot self/shoot dealer/use item)
The rules for the game are as follows:

## Game Rules

* There are two rational actors: the "player" (that which we control) and the "dealer" (our opponent). Each has a certain amount of "charges" (i.e. when one is shot, they lose a charge)
* Between them rests a shotgun, which is loaded with between 4 and 8 shells in a random order, some of which are live and others are blank. Both players know the total number of shells, as well as the total numbers of blank and live rounds; what they do not know is the order in which they are loaded.
* Players alternate turns in control of the gun; they may either:
  * Shoot themself: should the bullet be a blank, they get another turn;
  * Shoot the opponent: if the bullet is a live round, it reduces the opponent's "charges" by 1; if not, the opponent is unaffected.
  * Use an item: See descriptions of items below. Items do not end the player's turn when used unless explicitly mentioned.
* This repeats until a player runs out of charges. If the gun runs out of bullets, it is reloaded in the same manner as decribed above. Regardless of who fired the last shot, the player (not the dealer) will always start the new load-out with control of the gun. New items are given with each new load-out.

## Item Descriptions:

### Basic Items:

* **Cigarettes:** Using this item regenerates a "charge", allowing the user to absorb one more shot.
* **Hand Saw:** Using this item causes the next shot from the gun to do double damage, taking two "charges". This is true for either shooting oneself or shooting the opponent. This does not affect blanks.
* **Beer:** Using this _ejects_ the current shell from the gun without shooting it. After using this, the seen shell is no longer in play.
* **Magnifying Glass:** Allows the user to check the current shell that is about to be shot.
* **Handcuffs:** Forces the opponent to skip their next turn.

### "Double or Nothing" Mode:
(This list is included in addition to those mentioned above)
* **Expired Medicine:** Using this item grants a 50% chance to regain 2 charges, or a 50% chance to lose one charge.
* **Phone:** Using this item tells the user the state of a shell (i.e. if it is live or not) of some random shell later in the load-out (ex. "The sixth shell is a blank")
* **Adrenaline:** Using this item allows the user to steal an item from the opponent.
* **Inverter:** Using this item swaps the polarity of the shell currently in the chamber (i.e. if the next round is a blank, it is now a live round, and vice-versa).


## Goal of the Project:
Create a tool to optimize play to maximize chance of victory.
