from Combat import *

c = Combat()
c.AddPlayer(Player("Andrzej1", 10, 100, 0, Item("Sword", 30, 15, 30)))
c.AddPlayer(Player("Andrzej2", 10, 100, 0, Item("Sword", 30, 15, 30)))
c.AddOpponent(Player("Anrzej", 10, 100, 0, Item("Sword", 30, 15, 30)))
c.Fight()